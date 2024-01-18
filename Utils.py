# =================================================================================================
# ST1507 DATA STRUCTURES AND ALGORITHM (AI) CA2 ASSIGNMENT: ASSIGNMENT STATEMENT EVALUATOR & SORTER
# NAME: EDWARD TAN YUAN CHONG; ASHWIN RAJ
# CLASS: DAAA/FT/2B/04
# ADM NO: 2214407; 2239716
# =================================================================================================
# FILENAME: Utils.py
# =================================================================================================

# Import Data Structures
from DataStructures.Stack import Stack
# Import Modules
import re
import os

# ================================
# Utils for AssignmentStatement.py
# ================================

# Operator regex
operator_regex = re.compile(r'[\+\-\*/]')
# Variable regex
variable_regex = re.compile("^[A-Za-z]+$") # Check for only letters in variable

# Formatting error
format_error = lambda error, var="": f"\nInvalid format{' for variable ' + var if var else ''}! {error}. Please try again or CRTL+C to return back to main menu.\n"

# Check for existence of operators
def contain_operator(string):
    return bool(operator_regex.search(string))
    
# Check for matching parenthesis
def check_parenthesis(expression):
    # Instantiate Stack
    stack = Stack()
    # For each character in expression
    for char in expression:
        # If character is opening parenthesis, push into stack
        if char == '(':
            stack.push(char)
        # If character is closing parenthesis
        elif char == ')':
            # And the stack is empty, means that there is an unmatched parenthesis, hence return True
            if stack.is_empty():
                return True
            # Else, pop the corresponding opening parenthesis from the stack
            stack.pop()
    # If stack is not empty, there are unmatched opening parentheses
    return not stack.is_empty()

# Check for consecutive operands etc. "++" or "/*"
def check_consecutive_operators(expression):
    # Check for an operand without operands on both sides
    previous_char = ""
    # For each character in expression
    for char in expression:
        # If character is an operator
        if contain_operator(char):
            # And if previous character is empty, or is an operand, return True
            if previous_char == "" or previous_char in '+-':
                return True
        # Set previous character of next character as current character
        previous_char = char
    # After looping through all characters, and no return True has occured, this means there are no consecutive operands, hence return False
    return False

# Check for equal sign
def check_eq_sign(statement):
    # Get count of number of equal signs
    count_of_equal_signs = statement.count("=")
    # Check if there is an equal sign
    if count_of_equal_signs != 1:
        print(format_error("Please include at least/only one '=' in the statement"))
        return False
    return True

# Get key and value from statement
def get_key_and_value(statement):
    return [x.strip() for x in statement.split('=')]

# Validate and process key and value
def validate_and_process_statement(key, value):
    # Check if key or value is empty
    if not key or not value:
        print(format_error("Both left-hand side and right-hand side of the statement should not be empty",key))
        return False, value

    # Check if expression is incomplete
    if check_incomplete_expression(value):
        print(format_error("Expression is incomplete",key))
        return False, value

    # Check for consecutive operators
    if check_consecutive_operators(value):
        print(format_error("There should not be consecutive operators",key))
        return False, value

    # Check if variable is referencing itself
    if key in tokenize(value):
        print(format_error("Variable should not reference itself",key))
        return False, value

    # Check if key matches regex to only contain letters
    if not variable_regex.match(key):
        print(format_error("Variable names should only contain letters",key))
        return False, value

    # Check for any unmatched parenthesis
    if check_parenthesis(value):
        print(format_error("Please resolve any unmatched parenthesis",key))
        return False, value

    # Encapsulate value with parentheses if not already
    if not (value.startswith("(") and value.endswith(")")):
        value = f"({value})"

    return True, value


# Check for incomplete expressions
def check_incomplete_expression(expression):    
    # Check if expression starts or ends with an operator
    # Check if expression has at least one operator
    # Check that it is an expression (e.g. x=a+2, c=apple+banana) and not an incomplete expession (e.g. a=b)
    if contain_operator(expression[0]) or contain_operator(expression[-1]) or not contain_operator(expression) or len(tokenize(expression)) == 1:
        return True
    
# Handle file operations
def handle_file(question:str, mode:str)->str:
    # Get user input on input file path
    file_path = input(question)
    # Validate file extension
    if not file_path.endswith(".txt"):
        raise ValueError(f'\n{file_path} is an invalid file type. Expected a .txt file.\n')
    # Validate file existence for reading
    if mode == 'r' and not os.path.exists(file_path):
        raise FileNotFoundError(f'\nFile path "{file_path}" does not exist.\n')
    # If no errors, return file path
    return file_path
    
def write_file(file_path:str, content:str):
    try:
        # Open file
        with open(file_path, 'w') as file:
            # Write content to file
            file.write(content)
    # Catch exceptions and raise error
    except Exception:
        raise FileNotFoundError(f'\nError occurred with file "{file_path}."\n')


def read_file(file_path:str)->str:
    try:
        # Open file
        with open(file_path, 'r') as file:
            # Read lines of file
            return file.readlines()
    # Catch exceptions and raise error
    except Exception:
        raise FileNotFoundError(f'\nError occurred with file "{file_path}."\n')

    
def file_operation(file_path: str, mode: str, content: str = None) -> str:
    # Try and except to catch errors
    try:
        # Open file
        with open(file_path, mode, encoding='utf-8') as file:
            # If mode is write
            if mode == 'w':
                file.write(content)
            # Else mode is read
            else:
                return file.readlines()
    except Exception:
        raise FileNotFoundError(f'\nError occurred with file "{file_path}."\n')

# =================================================
# Utils for AssignmentStatement.py and ParseTree.py
# =================================================

# Tokenize expression
def tokenize(expression):
    # \b\w+\b matches whole words.
    # \*\* matches the ** operator.
    # // matches the // operator.
    # \S matches any non-whitespace character, covering other operators and single characters.
    tokens = re.findall(r'(\b\w+\b|\*\*|//|\S)', expression)
    return tokens

# ======================
# Utils for 
# ======================
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    sorted_list = []
    left_index, right_index = 0, 0

    # Iterate over both lists to merge them in sorted order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1

    # Add any remaining elements from the left list
    while left_index < len(left):
        sorted_list.append(left[left_index])
        left_index += 1

    # Add any remaining elements from the right list
    while right_index < len(right):
        sorted_list.append(right[right_index])
        right_index += 1

    return sorted_list