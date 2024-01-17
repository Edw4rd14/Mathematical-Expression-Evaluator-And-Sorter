# =================================================================================================
# ST1507 DATA STRUCTURES AND ALGORITHM (AI) CA2 ASSIGNMENT: ASSIGNMENT STATEMENT EVALUATOR & SORTER
# NAME: EDWARD TAN YUAN CHONG; ASHWIN RAJ
# CLASS: DAAA/FT/2B/04
# ADM NO: 2214407; 2239716
# =================================================================================================
# FILENAME: AssignmentStatement.py
# =================================================================================================
'''
Description:
This is the Main file which handles the main application, inclusive of the printing of the banner, handling user choices for the menu of the application,
and running the Class methods to perform the menu option's functions.
'''

# Import Data Structures
from DataStructures.HashTable import HashTable
from DataStructures.ParseTree import ParseTree
# Import Utils
from Utils import check_parenthesis
from Utils import format_error
from Utils import check_consecutive_operators
from Utils import tokenize
from Utils import check_incomplete_expression
# Import Modules
import re

# AssignmentStatement Class
class AssignmentStatement:
    # Initialization
    def __init__(self):
        # Initialize HashTable Class
        self.hash_table = HashTable()
        # Regex expression for variable
        self.regex = re.compile("^[A-Za-z]+$") # Check for only letters in variable
    
    # Option 1: Add/modify assignment statement
    def add_modify_statement(self):
        # While loop to prompt users until valid input is provided
        while True:
            # Get assignment statement
            statement = input("Enter the assignment statement you want to add/modify:\nFor example, a=(1+2)\n")

            # Get count of number of equal signs
            count_of_equal_signs = statement.count("=")

            # Check if there is an equal sign
            if count_of_equal_signs != 1:
                print(format_error("Please include at least/only one '=' in the statement"))
                continue
            
            # Split the statement by '='
            key, value = [x.strip() for x in statement.split('=')]

            # Check if key or value is empty, if it is empty, print error message
            if not key or not value:
                print(format_error("Both left-hand side and right-hand side of the statement should not be empty"))
                continue

            # Check if expression is incomplete
            if check_incomplete_expression(value):
                print(format_error("Expression is incomplete"))
                continue

            # Check for consecutive operators
            if check_consecutive_operators(value):
                print(format_error("There should not be consecutive operators"))
                continue

            # Check if variable is referencing itself
            if key in tokenize(value):
                print(format_error("Variable should not reference itself"))
                continue

            # Check if key matches regex to only contain letters
            if not self.regex.match(key):
                print(format_error("Variable names should only contain letters"))
                continue

            # Check for any unmatched parenthesis
            if check_parenthesis(value):
                print(format_error("Please resolve any unmatched parenthesis"))
                continue

            # Encapsulate value with parentheses if not already
            if not (value.startswith("(") and value.endswith(")")):
                value = f"({value})"

            # Expression satisfies all conditions, add to HashTable and break out of option 1
            self.hash_table[key] = value
            break
    
    # Option 2: Display current assignment statements
    def display_statements(self):
        # Print header
        print('\nCURRENT ASSIGNMENTS:\n' + "*"*20)
        # Check if there are any assignment statements (if there isnt all keys are None)
        if all(key is None for key in self.hash_table.keys):
            # Print error statement if there are no assignment statements
            print("There are no current assignment statements.")
        # Else if there are assignment statements
        else:
            # Loop each key in the sorted list
            for key in sorted(self.hash_table.keys,key=lambda x: (x is None, x)):
                # If key is not None and is an assignment statement
                if key is not None:
                    # Catch errors with try
                    try:
                        # Try grabbing the assignment statement value
                        value = self.hash_table[key]
                        # Evaluate value of expression with ParseTree
                        tree = ParseTree(expression=value, hash_table=self.hash_table)
                        # Print evaluation result
                        print(f'{key}={value}=> {tree.evaluate()}')
                    # If an error occurs, pass
                    except:
                        pass

    # Option 3: Evaluate and print parse tree for an individual variable
    def evaluate_single_variable(self):
    # Get variable from user input
        while True:
            variable = input("Please enter the variable you want to evaluate:\n")
            try:
                # Get the expression associated with the variable
                expression = self.hash_table[variable]
                # If expression exists
                if expression is not None:
                    # Build parse tree
                    tree = ParseTree(expression, hash_table=self.hash_table)
                    # Print expression tree in in-order format
                    print("\nExpression Tree:")
                    tree.print_in_order()
                    # Evaluate and print the value for the variable
                    value = tree.evaluate()
                    print(f"Value for variable \"{variable}\" is {value}")
                    # Break out of while loop after variable is evaluated
                    break
                # Else, variable does not exist
                else:
                    print(f'\nVariable "{variable}" does not exist. Please try again or CTRL+C to return to the main menu.\n')
            # Catch Any Errors
            except:
                pass
    