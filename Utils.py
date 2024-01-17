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
    if expression[0] in operators or expression[-1] in operators or not bool(operator_regex.search(expression)) or len(tokenize(expression)) == 1:
        return True


# =================================================
# Utils for AssignmentStatement.py and ParseTree.py
# =================================================

# Tokenize expression
def tokenize(expression):
    tokens = re.findall(r'(\b\w+\b|\S)', expression)
    return tokens