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
        super().__init__()
        # Initialize regular expressions
        self.operator_regex = re.compile(r'\*\*|[\+\-\*/]')
        self.parenthesis_regex = re.compile(r'(\d\(|\)\d|\)\(|[a-zA-Z]\(|\)[a-zA-Z])')
        self.variable_regex = re.compile("^[A-Za-z]+$")

    # Tokenize expression
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
        # \b\w+\b matches whole words.
        # \*\* matches the ** operator.
        # // matches the // operator.
        # \S matches any non-whitespace character, covering other operators and single characters.
        # (\d+\.\d+) matches decimal numbers.
        tokens = re.findall(r'(\b\d+\.\d+\b|\b\w+\b|\*\*|//|\S)', expression)
        return tokens
    
    # Get key and value from statement
    @staticmethod
    def get_key_and_value(statement:str)->list:
        """
        The get_key_and_value function takes in an assignment statement by the = for the variable 
        and expression of the assignment statement.
        
        :param statement:str: Assignment statement to be split
        :return: A list of strings
        """
        return [x.strip() for x in statement.split('=')]


    # Check if expression contains operator
    def contain_operator(self, expression: str) -> bool:
        """
        The contain_operator function checks for the existence of operators in an expression.
            
        :param self: Refer to the instance of the class
        :param expression: str: Pass in the expression that is being evaluated
        :return: A boolean value of whether the expression contains operators
        """
        # Check for the existence of operators
        return bool(self.operator_regex.search(expression))

    # Check juxtaposition of parenthesis in expression
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

    # Check if there are consecutive operators in the expression
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

    # Check for equal sign
    def check_eq_sign(self, statement: str, menu: bool=True) -> bool:
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
            print(self.format_error("Please include at least/only one '=' in the statement", menu))
            return False
        return True

    # Check for incomplete expression
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
        if (
            self.contain_operator(expression[0]) or
            self.contain_operator(expression[-1]) or
            not self.contain_operator(expression) or
            len(self.tokenize(expression)) == 1
        ):
            return True
        return False

    # Check parenthesis in expression
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
        tokens = self.tokenize(expression)
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
    
    # Run key and value through all validation
    def validate_key_and_value(self, key: str, value: str, menu:bool=True) -> tuple:
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
            print(self.format_error("Both left-hand side and right-hand side of the statement should not be empty",menu,key))
            return False

        # Check if expression is incomplete
        if self.check_incomplete_expression(value):
            print(self.format_error("Expression is incomplete",menu,key))
            return False

        # Check for consecutive operators
        if self.check_consecutive_operators(value):
            print(self.format_error("There should not be consecutive operators",menu,key))
            return False

        # Check if variable is referencing itself
        if key in self.tokenize(value):
            print(self.format_error("Variable should not reference itself",menu,key))
            return False

        # Check if key matches regex to only contain letters
        if not self.variable_regex.match(key):
            print(self.format_error("Variable names should only contain letters",menu,key))
            return False
        
        if self.check_juxtaposition_parenthesis(value):
            print(self.format_error("Please check juxtaposition of variables and numbers to parenthesis",menu,key))
            return False

        # Check for any unmatched parenthesis
        if not self.check_parenthesis(value):
            print(self.format_error("Please check that the expression is fully parenthesized",menu,key))
            return False

        return True
    
    # Extract variable   
    def extract_variables(self, item):
        """
        The extract_variables returns the variables in an expression.
        
        :param item: Expression to be extracted
        :return: A list of all the variables from the expression
        """
        variables = []
        for t in self.tokenize(item):
            if t.isalpha():
                variables.append(t)
        return variables
    
    @staticmethod
    def format_dependency(variable, dependencies):
        dependency_list = list(dependencies)
        if len(dependency_list) > 1:
            result_string = ', '.join(dependency_list[:-1]) + f' and {dependency_list[-1]}.'
        elif len(dependency_list) == 1:
            result_string = dependency_list[0]
        return f"{variable} {'is dependent on ' + result_string if dependency_list else 'is independent.'}\n\n"
    
    # Get relevant variables recursively
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

    def has_circular_dependency(self, variable, hash_table, seen=None):
        if seen is None:
            seen = set()
        if variable in seen:
            return True  # Circular dependency detected
        if variable not in hash_table:
            return False  # Variable not defined, no circular dependency
        seen.add(variable)
        # Tokenize the expression associated with the variable to extract referenced variables
        tokens = self.tokenize(hash_table[variable])
        for token in tokens:
            if token in hash_table and self.has_circular_dependency(token, hash_table, seen.copy()):
                return True
        seen.remove(variable)
        return False
