# =================================================================================================
# ST1507 DATA STRUCTURES AND ALGORITHM (AI) CA2 ASSIGNMENT: ASSIGNMENT STATEMENT EVALUATOR & SORTER
# NAME: EDWARD TAN YUAN CHONG; ASHWIN RAJ
# CLASS: DAAA/FT/2B/04
# ADM NO: 2214407; 2239716
# =================================================================================================
# FILENAME: InputValidation.py
# =================================================================================================

# Import Data Structures
from DataStructures.Stack import Stack
from DataStructures.ParseTree import ParseTree
# Import modules
import re
import os

# InputValidation class
class InputValidation:
    def __init__(self):
        """
        The __init__ function initializes the class with regular expressions for operators, parenthesis and variables.
        It also creates a lambda function that returns an error message if there is an invalid format.
        
        :param self: Refer to the instance of the class
        :return: Nothing
        """
        # Initialize regular expressions
        self.operator_regex = re.compile(r'\*\*|[\+\-\*/]')
        self.parenthesis_regex = re.compile(r'(\d\(|\)\d|\)\(|[a-zA-Z]\(|\)[a-zA-Z])')
        self.variable_regex = re.compile("^[A-Za-z]+$")
        # End of error message
        self.err_msg = 'Please try again or CRTL + C to return back to main menu.\n'
        # Formatting error
        self.format_error = lambda error, var="": f"\nInvalid format{' for variable ' + var if var else ''}! {error}. {self.err_msg}"

    def contain_operator(self, expression: str) -> bool:
        """
        The contain_operator function checks for the existence of operators in an expression.
            
        :param self: Refer to the instance of the class
        :param expression: str: Pass in the expression that is being evaluated
        :return: A boolean value of whether the expression contains operators
        """
        # Check for the existence of operators
        return bool(self.operator_regex.search(expression))

    def check_juxtaposition_parenthesis(self, expression: str) -> bool:
        """
        The check_juxtaposition_parenthesis function checks for juxtaposition of variables or number next to ( or after ), 
        or )(. It returns True if the expression contains any of these errors, and False otherwise.
        
        :param self: Refer to the instance of the class
        :param expression: str: Pass the expression to be evaluated
        :return: True if the expression contains juxtaposition of variables or number next to ( or after ), or )(
        """
        # Check for juxtaposition of variables or number next to ( or after ), or )(
        return bool(self.parenthesis_regex.search(expression))

    def check_consecutive_operators(self, expression: str) -> bool:
        """
        The check_consecutive_operators function checks for consecutive operators in the expression.
        If there are any, it returns True, else False.
        
        :param self: Refer to the instance of the class
        :param expression: str: Store the expression that is passed into the function
        :return: True if there is an operand without operands on both sides, and false otherwise
        """
        # Check for an operand without operands on both sides
        previous_char = ""
        # For each character in expression
        for char in expression:
            # If character is an operator
            if self.contain_operator(char):
                # And if previous character is empty, or is an operand, return True
                if previous_char == "" or previous_char in '+-':
                    return True
            # Set previous character of next character as current character
            previous_char = char
        # After looping through all characters, and no return True has occured, this means there are no consecutive operands, hence return False
        return False

    def check_eq_sign(self, statement: str) -> bool:
        """
        The check_eq_sign function checks if there is an equal sign in the statement.
        If there is not or more than 1, it returns False and prints a message to the user.
        If there is one, it returns True.
        
        :param self: Refer to the instance of the class
        :param statement: str: Get the string that is passed in
        :return: A boolean value of whether there is only 1 equal sign
        """
        # Get count of number of equal signs
        count_of_equal_signs = statement.count("=")
        # Check if there is an equal sign
        if count_of_equal_signs != 1:
            print(self.format_error("Please include at least/only one '=' in the statement"))
            return False
        return True

    def check_incomplete_expression(self, expression: str) -> bool:
        """
        The check_incomplete_expression function checks for incomplete expressions.
        It does this by checking if the expression starts or ends with an operator,
        and also checks that it is an expression (e.g. x=a+2, c=apple+banana) and not 
        an incomplete expession (e.g. a=b). If any of these conditions are met, then 
        the function returns True.
        
        :param self: Refer to the instance of the class
        :param expression: str: Check if the expression is incomplete
        :return: True if the expression is incomplete and false otherwise
        """
        # Check for incomplete expressions
        # Check if expression starts or ends with an operator
        # Check if expression has at least one operator
        # Check that it is an expression (e.g. x=a+2, c=apple+banana) and not an incomplete expession (e.g. a=b)
        if (self.contain_operator(expression[0]) or
                self.contain_operator(expression[-1]) or
                not self.contain_operator(expression) or
                len(ParseTree.tokenize(expression)) == 1):
            return True
        return False

    def handle_file(self, question: str, mode: str = None) -> str:
        """
        The handle_file function is used to validate user input for file paths.
        It takes two arguments: a question string and an optional mode string.
        The question argument is the prompt that will be displayed to the user, asking them for their input.
        The mode argument can either be 'r' or 'w', which stands for read or write respectively, and defaults to None if not specified by the caller.
        
        :param self: Refer to the instance of the class
        :param question: str: Prompt the user for a file path
        :param mode: str: Determine if the file is being read or written to
        :return: The file path
        """
        # Get user input on input file path
        file_path = input(question)
        # Validate file extension
        if not file_path.endswith(".txt"):
            raise ValueError(f'\n"{file_path}" is an invalid file type. Expected a .txt file. {self.err_msg}')
        # Validate file existence for reading
        if mode == 'r' and not os.path.exists(file_path):
            raise FileNotFoundError(f'\nFile path "{file_path}" does not exist. {self.err_msg}')
        # If no errors, return file path
        return file_path

    def check_parenthesis(self, expression: str) -> bool:
        """
        The check_parenthesis function checks if the expression is valid.
        It checks that each opening parenthesis has a closing one, and that there are no operators outside of parentheses.
        The function also checks for unbalanced parentheses and multiple operators inside a single set of parentheses, such as (a+b+c)
        
        :param self: Refer to the instance of the class
        :param expression: str: Pass in the expression to be evaluated
        :return: True if the expression is valid, and false otherwise
        """
        # Remove whitespace from the expression
        expression = expression.replace(' ', '')
        # Initialize a stack to keep track of parentheses and operators
        stack = Stack()
        # Get tokens
        tokens = ParseTree.tokenize(expression)
        # For each token in expression tokens
        for t in tokens:
            if t == '(':
                # Push a tuple to stack: (opening bracket, operator flag reset)
                stack.push(('(', False))
            elif self.operator_regex.search(t):
                if stack.is_empty:
                    # Operator found outside of any parentheses
                    return False
                else:
                    # Update the top element of the stack to set operator flag to True
                    top = stack.pop()
                    if top[1]:  # There's already an operator inside these parentheses
                        return False
                    stack.push((top[0], True))
            elif t == ')':
                if stack.is_empty or not stack.pop()[1]:  # Parentheses are unbalanced or no operator inside
                    return False
        # Check if there are any unclosed parentheses left in the stack
        return all(item[0] != '(' for item in stack.items)

    
    def validate_key_and_value(self, key: str, value: str) -> tuple:
        """
        The validate_key_and_value function takes in a key and value, and runs a series of
        validation to ensure that the key (variable) and value (expression) are valid, returning the

        
        :param self: Refer to the instance of the class
        :param key: str: Check if the key is empty
        :param value: str: Check if the expression is incomplete
        :return: A boolean value where True is valid and False is invalid key and value
        """
        # Check if key or value is empty
        if not key or not value:
            print(self.format_error("Both left-hand side and right-hand side of the statement should not be empty",key))
            return False

        # Check if expression is incomplete
        if self.check_incomplete_expression(value):
            print(self.format_error("Expression is incomplete",key))
            return False

        # Check for consecutive operators
        if self.check_consecutive_operators(value):
            print(self.format_error("There should not be consecutive operators",key))
            return False

        # Check if variable is referencing itself
        if key in ParseTree.tokenize(value):
            print(self.format_error("Variable should not reference itself",key))
            return False

        # Check if key matches regex to only contain letters
        if not self.variable_regex.match(key):
            print(self.format_error("Variable names should only contain letters",key))
            return False
        
        if self.check_juxtaposition_parenthesis(value):
            print(self.format_error("Please check juxtaposition of variables and numbers to parenthesis",key))
            return False

        # Check for any unmatched parenthesis
        if not self.check_parenthesis(value):
            print(self.format_error("Please check that the expression is fully parenthesized",key))
            return False

        return True

    def validate_file(self,question:str, mode:str=None)->str:
        # Get user input on input file path
        file_path = input(question)
        # Validate file extension
        if not file_path.endswith(".txt"):
            raise ValueError(f'\n"{file_path}" is an invalid file type. Expected a .txt file. {self.err_msg}')
        # Validate file existence for reading
        if mode == 'r' and not os.path.exists(file_path):
            raise FileNotFoundError(f'\nFile path "{file_path}" does not exist. {self.err_msg}')
        # If no errors, return file path
        return file_path
    
    def prompt_polar_question(self, question:str)->bool:
        while True:
            # Get user input on overwriting
            user_input = input(question)
            # If user inputs No, return False
            if user_input.lower() == 'n':
                return False
            # Else if invalid input, not N or Y, print error and loop again
            elif user_input.lower() != 'y':
                print("\nInvalid input! Please enter only Y (Yes) or N (No).",self.err_msg)
            # Else input is Y, return True
            else:
                return True
