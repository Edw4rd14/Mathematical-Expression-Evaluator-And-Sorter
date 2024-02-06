# =================================================================================================
# ST1507 DATA STRUCTURES AND ALGORITHM (AI) CA2 ASSIGNMENT: ASSIGNMENT STATEMENT EVALUATOR & SORTER
# NAME: EDWARD TAN YUAN CHONG; ASHWIN RAJ
# CLASS: DAAA/FT/2B/04
# ADM NO: 2214407; 2239716
# =================================================================================================
# FILENAME: ExpressionHandler.py
# =================================================================================================

# Import Data Structures
from DataStructures.Stack import Stack
# Import Classes
from Classes.InputHandler import InputHandler
# Import Modules
import re

# ExpressionHandler class
class ExpressionHandler(InputHandler):
    # Initialization
    def __init__(self):
        """
        The __init__ function is called when the class is instantiated.
        It initializes all of the attributes that are required for this class.
        
        :param self: Refer to the instance of the class
        :return: Nothing
        """
        # Initialize super handler class
        super().__init__()
        # Initialize regular expression
        self.parenthesis_regex = re.compile(r'(\d\(|\)\d|\)\(|[a-zA-Z]\(|\)[a-zA-Z])')
        self.operator_regex = re.compile(r'\*\*|[\+\-\*/]')
        # Operators list
        self.operators = ["+","-","**","*","/"]

    # Tokenize expression - Done by Edward
    @staticmethod
    def tokenize(expression:str)->list:
        """
        The tokenize function takes a string and returns a list of tokens.
        The tokenize function uses the regular expression r'(\b\d+\.\d+\b|\b\w+\b|[^ \t]+)' to match:
        - decimal numbers, e.g., 3.15;
        - whole words, e.g., 'apple';
        - operators and single characters, e.g., '*', '/', '('.  
        
        :param expression:str: Expression to be tokenized
        :return: A list of tokens
        """
        tokens = []
        current = ''
        last_char_was_operator = False  # Track if the last character processed was part of an operator

        i = 0
        while i < len(expression):
            char = expression[i]

            # Check for floating point numbers and alphanumeric tokens
            if char.isdigit() or char.isalpha():
                if last_char_was_operator:
                    if current:  # If there's something in current (it could be an operator), add it to tokens
                        tokens.append(current)
                        current = ''
                    last_char_was_operator = False  # Reset flag since we're now processing a digit/alpha
                current += char
            elif char == '.' and current.isdigit():
                current += char  # Continue building a floating point number
            elif char == '*' and i + 1 < len(expression) and expression[i + 1] == '*':
                # For '**' operator, append current if it's not empty and reset current
                if current:
                    tokens.append(current)
                tokens.append('**')
                current = ''
                i += 1  # Skip the next '*' as it's already processed
                last_char_was_operator = True
            else:
                if char.strip():  # This checks if char is not whitespace
                    if current:  # Add the current token if it exists
                        tokens.append(current)
                        current = ''
                    if char != '*' or not last_char_was_operator:  # Avoid adding '*' if it's part of '**'
                        tokens.append(char)
                    last_char_was_operator = (char in ['*', '+', '-', '/', '='])  # Update flag based on current char
                else:
                    last_char_was_operator = False  # Reset if we encounter whitespace

            i += 1  # Move to the next character

        if current:  # Add any remaining token
            tokens.append(current)

        return tokens

    
    # Get key and value from statement - Done by Edward
    @staticmethod
    def get_key_and_value(statement:str)->list:
        """
        The get_key_and_value function takes in an assignment statement by the = for the variable 
        and expression of the assignment statement.
        
        :param statement:str: Assignment statement to be split
        :return: A list of strings
        """
        return [x.strip() for x in statement.split('=')]

    # Check if expression contains operator - Done by Edward
    def contain_operator(self, expression: str) -> bool:
        """
        The contain_operator function checks for the existence of operators in an expression.
            
        :param self: Refer to the instance of the class
        :param expression: str: Pass in the expression that is being evaluated
        :return: A boolean value of whether the expression contains operators
        """
        return bool(self.operator_regex.search(expression))

    # Check juxtaposition of parenthesis in expression - Done by Edward
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

    # Check if there are consecutive operators in the expression - Done by Edward
    def check_consecutive_operators(self, expression: str) -> bool:
        """
        The check_consecutive_operators function checks for consecutive operators in the expression.
        If there are any, it returns True, else False.
        
        :param self: Refer to the instance of the class
        :param expression: str: Store the expression that is passed into the function
        :return: True if there is an operand without operands on both sides, and false otherwise
        """
        # Check for an operator without operator on both sides
        previous_char = ""
        # For each character in expression
        for char in expression:
            # If character is an operator
            if self.contain_operator(char):
                # And if previous character is empty, or is an operator, return True
                if previous_char == "" or previous_char in '+-/':
                    return True
            # Set previous character of next character as current character
            previous_char = char
        # After looping through all characters, check for consecutive asterisks "***"
        if '***' in expression:
            return True
        # After looping through all characters, and no return True has occured, this means there are no consecutive operands, hence return False
        return False

    # Check for equal sign - Done by Edward
    def check_eq_sign(self, statement: str, menu: bool=True) -> bool:
        """
        The check_eq_sign function checks if there is an equal sign in the statement.
        If there is not or more than 1, it returns False and prints a message to the user.
        If there is one, it returns True.
        
        :param self: Refer to the instance of the class
        :param statement: str: Statement to check
        :return: A boolean value of whether there is only 1 equal sign
        """
        # Get count of number of equal signs
        count_of_equal_signs = statement.count("=")
        # Check if there is an equal sign
        if count_of_equal_signs != 1:
            print(self.format_error("Please include at least/only one '=' in the statement", menu))
            return False
        return True

    # Check for incomplete expression - Done by Edward
    def check_incomplete_expression(self, expression: str) -> bool:
        """
        The check_incomplete_expression function checks for incomplete expressions.
        The function returns True for an incomplete expression, otherwise False.
        
        :param self: Refer to the instance of the class
        :param expression: str: Expression to be validated
        :return: True if the expression is incomplete and false otherwise
        """
        # Check if the expression starts or ends with an operator
        if self.contain_operator(expression[0]) or self.contain_operator(expression[-1]):
            return True
        # Check for absence of operators in the expression
        if not self.contain_operator(expression):
            return True
        # Check if expression is a single token
        if len(self.tokenize(expression)) == 1:
            return True
        # Additional check for operator next to parenthesis
        for i in range(len(expression) - 1):
            if (expression[i] in self.operators and expression[i+1] == ')') or (expression[i] == '(' and expression[i+1] in self.operators):
                return True
        # Return False otherwise
        return False
    
    def check_float(self, expression:str)->bool:
        """
        The check_float function checks if every '.' is both preceded and followed by a digit.
        
        :param self: Refer to the instance of the class
        :param expression: Expression to be validated
        :return: False if the expression is properly formatted and True otherwise
        """
        # Check if every '.' is both preceded and followed by a digit
        for i, char in enumerate(expression):
            # If character is '.'
            if char == '.':
                # Check if '.' is at the start, the end, or the preceding/following character is not a digit
                if i == 0 or not expression[i-1].isdigit():
                    return True 
                if i == len(expression) - 1 or not expression[i+1].isdigit():
                    return True 
        # Return True if all '.' are properly formatted
        return False 

    # Check parenthesis in expression - Done by Edward
    def check_parenthesis(self, expression: str) -> bool:
        """
        The check_parenthesis function checks if the expression is valid.
        It checks that each opening parenthesis has a closing one, and that there are no operators outside of parenthesis.
        The function also checks for unbalanced parenthesis and multiple operators inside a single set of parenthesis, such as (a+b+c)
        
        :param self: Refer to the instance of the class
        :param expression: str: Expression to be validated
        :return: True if the expression is valid, and false otherwise
        """
        # Remove whitespace from the expression
        expression = expression.replace(' ', '')
        # Initialize a stack to keep track of parentheses and operators
        stack = Stack()
        # Get tokens
        tokens = self.tokenize(expression)
        # For each token in expression tokens
        for t in tokens:
            # If token is (
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
                    if top[1]:
                        return False
                    stack.push((top[0], True))
            # Else if token is )
            elif t == ')':
                if stack.is_empty or not stack.pop()[1]: 
                    return False
        # Check if there are any unclosed parentheses left in the stack
        return all(item[0] != '(' for item in stack.items)
    
    # Check circular dependency - Done by Edward
    def has_circular_dependency(self, variable, hash_table, seen=None):
        """
        The has_circular_dependency function takes a variable and hash_table as input.
        It returns True if the variable has a circular dependency, False otherwise.
        A circular dependency example is where A depends on B, B depends on A
        
        :param self: Refer to the instance of the class
        :param variable: Variable to be checked
        :param hash_table: Hash table of all statements to be checked against
        :param seen: Keep track of the variables that have been seen so far
        :return: True if a circular dependency is detected, False if there is no circular dependency
        """
        # Initialize seen if it has not been initialized
        if seen is None:
            seen = set()
        # Check if the current variable has already been seen, indicating circular dependency
        if variable in seen:
            return True 
        # Check if the variable is not in the hash_table, meaning it is undefined and has no circular dependency
        if variable not in hash_table:
            return False 
        # Add the current variable to the seen set
        seen.add(variable)
        # Tokenize the expression to get tokens
        tokens = self.tokenize(hash_table[variable])
        # Iterate over each token to check for circular dependencies
        for token in tokens:
            # If token is a variable in hash_table, recursively check for circular dependencies
            if token in hash_table and self.has_circular_dependency(token, hash_table, seen.copy()):
                return True 
        # Remove the current variable from the 'seen' set after checking all referenced variables
        seen.remove(variable)
        # Return False if no circular dependencies are detected after checking all referenced variables
        return False
    
    # Check for float - Done by Edward
    @staticmethod
    def is_float(token:str)->bool:
        """
        The is_float function checks if the token is a float
        
        :param token:str: Token to be checked
        :return: True if the token is a float, and false otherwise
        """
        try:
            # Try to convert to float, if no error, return True
            float(token)
            return True
        # If error, return False
        except ValueError:
            return False
    
    # Check for invalid characters - Done by Edward
    def check_invalid_characters(self, expression:str)->bool:
        """
        The check_invalid_characters function checks for invalid characters in the expression, such as @ or _
        It returns True if there are any invalid characters, and False otherwise.
        
        :param self: Refer to the instance of the class
        :param expression:str: Expression to be checked
        :return: True if there are invalid characters in the expression
        """
        # For each token
        for t in self.tokenize(expression):
            # Check that it is a valid character
            if not self.operator_regex.search(t) and not t.isalpha() and not t.isdigit() and not self.is_float(t) and t not in "()":
                return True 
        # Return False if all characters are valid
        return False
    
    # Run key and value through all validation - Done by Edward
    def validate_key_and_value(self, key: str, value: str, hash_table, menu:bool=True) -> tuple:
        """
        The validate_key_and_value function takes in a key and value, and runs a series of
        validation to ensure that the key (variable) and value (expression) are valid, returning True for valid and False for invalid.

        The function also checks for circular dependency, by firstly adding the key and value into the hashtable, evaluating whether
        there is circular dependency from that key and value, and removing it before throwing an error or returning True so that the
        adding can be done outside the function (as this function should ONLY validate).
        
        :param self: Refer to the instance of the class
        :param key: str: Check if the key is empty
        :param value: str: Check if the expression is incomplete
        :param hashtable: Hash table to be used to validate circular dependency
        :return: A boolean value where True is valid and False is invalid key and value
        """
        # Check if key or value is empty
        if not key or not value:
            print(self.format_error("Both left-hand side and right-hand side of the statement should not be empty",menu,key))
            return False

        # Check if expression is incomplete
        if self.check_incomplete_expression(value):
            print(self.format_error("Expression is incomplete",menu,key))
            return False
        
        # Check if there are invalid characters in expression
        if self.check_invalid_characters(value):
            print(self.format_error("Expression has invalid characters",menu,key))
            return False

        # Check if key only contain letters
        if not key.isalpha():
            print(self.format_error("Variable names should only contain letters",menu,key))
            return False

        # Check for consecutive operators
        if self.check_consecutive_operators(value):
            print(self.format_error("There should not be consecutive operators",menu,key))
            return False

        # Check if variable is referencing itself
        if key in self.tokenize(value):
            print(self.format_error("Variable should not reference itself",menu,key))
            return False
        
        # Check for any unmatched parenthesis
        if not self.check_parenthesis(value):
            print(self.format_error("Please check that the expression is fully parenthesized",menu,key))
            return False
        
        # Check juxtaposition of parenthesis
        if self.check_juxtaposition_parenthesis(value):
            print(self.format_error("Please check juxtaposition of variables and numbers to parenthesis",menu,key))
            return False
        
        # Check float formatting
        if self.check_float(value):
            print(self.format_error("Please check formatting of float",menu,key))
            return False
        
        # Checks for circular dependency
        # Add to hash table first
        hash_table[key] = value
        # Check for circular dependency after adding to hash
        if self.has_circular_dependency(key, hash_table):
            print(self.format_error("Circular dependency detected. The assignment is not added", menu, var=key))
            del hash_table[key]
            return False
        del hash_table[key]

        # Return True for no errors
        return True
    
    # Extract variable - Done by Edward
    def extract_variables(self, item):
        """
        The extract_variables returns the variables in an expression.
        
        :param self: Refer to the instance of the class
        :param item: Expression to be extracted
        :return: A list of all the variables from the expression
        """
        # Variables list
        variables = []
        # For each item in expression
        for t in self.tokenize(item):
            # If it is a variable
            if t.isalpha():
                # Append to list
                variables.append(t)
        return variables
    
    # Format variable dependency - Done by Edward
    @staticmethod
    def format_dependency(variable, dependencies):
        """
        The format_dependency function takes a variable and its dependencies and formats it as a string
        for outputting to a file for batch processing.
        If a variable is independent, it will return "{variable} is independent."
        If the variable is dependent, it will return "{variable} is dependent on ..."
        
        :param variable: Variable that was checked for dependencies
        :param dependencies: Dependencies of that variable
        :return: A formatted string that describes the dependencies of a variable
        """
        # List of dependencies
        dependency_list = list(dependencies)
        # If list is more than 1, format with an "and"
        if len(dependency_list) > 1:
            result_string = ', '.join(dependency_list[:-1]) + f' and {dependency_list[-1]}.'
        # Else just format with the dependency
        elif len(dependency_list) == 1:
            result_string = dependency_list[0]
        # Return formatted string, with "is independent" if there is no dependency for that variable
        return f"{variable} {'is dependent on ' + result_string if dependency_list else 'is independent.'}\n\n"
    
    # Get relevant variables recursively - Done by Edward
    def get_related_variables(self, variable, statements, explored=None):
        """
        The get_related_variables function takes a variable as input and returns all variables that are related to it.
        
        :param self: Refer to the instance of the class
        :param variable: Variable to refer to for finding relevant variables
        :param statements: List of statements containing variables and their expressions
        :param explored: Set of variables that have already been explored to avoid infinite recursion
        :return: A set of variables that are related to the variable
        """
        if explored is None:
            # Initialize explored as an empty set if it is None
            explored = set()
        # Initialize related_variables as an empty set
        related_variables = set()
        # Avoid re-exploring variables
        if variable in explored:
            # If the variable has been explored before, return the current set of related variables
            return related_variables
        # Add the current variable to the set of explored variables
        explored.add(variable)
        for item in statements:
            if item[0] == variable:
                # Extract variables from the expression
                variables = self.extract_variables(item[1])
                # Add directly related variables
                related_variables.update(variables)
                # Recursively get related variables for each found variable
                for v in variables:
                    # Check to prevent re-exploration
                    if v not in explored:  
                        related_variables.update(self.get_related_variables(v, statements, explored))
        # Return the set of related variables
        return related_variables