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

# ================================
# Utils for AssignmentStatement.py
# ================================

# Variables
operator_regex = re.compile(r'[\+\-\*/]')

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

# Formatting error
format_error = lambda error: f'\nInvalid format! {error}. Please try again or CRTL+C to return back to main menu.\n'

# Check for consecutive operands etc. "++" or "/*"
def check_consecutive_operators(expression):
    """
    Check if there are consecutive operators in the expression.

    :param expression: The expression to check.
    :return: True if consecutive operators are found, False otherwise.
    """
    operators = set('+-*/')

    for i in range(len(expression) - 1):
        char1, char2 = expression[i], expression[i + 1]

        # Check if both characters are operators
        if char1 in operators and char2 in operators:
            # Check for valid exponentiation (char1 should be '*' and char2 should be '*')
            if char1 == '*' and char2 == '*':
                continue  # Valid exponentiation, skip to the next iteration
            else:
                # Provide information about the location of consecutive operators
                start_index = max(0, i - 10)
                end_index = min(len(expression), i + 11)
                snippet = expression[start_index:end_index]

                # Print an error message with the specific location
                print(format_error(f"There should not be consecutive operators. Found in: ...{snippet}..."))
                return True

    return False



# Check for incomplete expressions
def check_incomplete_expression(expression):    
    # Check if expression starts or ends with an operator
    # Check if expression has at least one operator
    # Check that it is an expression (e.g. x=a+2, c=apple+banana) and not an incomplete expession (e.g. a=b)
    if contain_operator(expression[0]) or contain_operator(expression[-1]) or not contain_operator(expression) or len(tokenize(expression)) == 1:
        return True


# =================================================
# Utils for AssignmentStatement.py and ParseTree.py
# =================================================

# Tokenize expression
def tokenize(expression):
    tokens = re.findall(r'(\b\w+\b|\S)', expression)
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