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
operators = ['+','-','/','*']
operator_regex = re.compile(r'[\+\-\*/]')
    
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
    # Check for an operand without operands on both sides
    previous_char = ""
    # For each character in expression
    for char in expression:
        # If character is an operand
        if char in operators:
            # And if previous character is empty, or is an operand, return True
            if previous_char == "" or previous_char in operators:
                return True
        # Set previous character of next character as current character
        previous_char = char
    # After looping through all characters, and no return True has occured, this means there are no consecutive operands, hence return False
    return False

# Check for incomplete expressions
def check_incomplete_expression(expression):    
    # Check if expression starts or ends with an operator
    # Check if expression has at least one operator
    # Check that it is an expression (e.g. x=a+2, c=apple+banana) and not an incomplete expession (e.g. a=b)
    if expression[0] in operators or expression[-1] in operators or not bool(operator_regex.search(expression)) or len(tokenize(expression)) == 1:
        return True


# =================================================
# Utils for AssignmentStatement.py and ParseTree.py
# =================================================

# Tokenize expression
def tokenize(expression):
    tokens = re.findall(r'(\b\w+\b|\S)', expression)
    return tokens