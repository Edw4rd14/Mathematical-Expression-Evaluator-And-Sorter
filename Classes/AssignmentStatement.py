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
from Utils import check_consecutive_operands
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
        self.regex = re.compile("^[A-Za-z]+$")
    
    # Option 1: Add/modify assignment statement
    def add_modify_statement(self):
        # While loop to prompt users until valid input is provided
        while True:

            # Get assignment statement
            statement = input("Enter the assignment statement you want to add/modify:\nFor example, a=(1+2)\n")

            # Check if '=' is in statement, which is the correct format we expect, else print error message
            if '=' not in statement:
                print(format_error("Please include '=' in the statement"))
                continue

            # Split the statement by '='
            key, value = statement.split('=')
            key, value = key.strip(), value.strip()

            # Check if key or value is empty, if it is empty, print error message
            if not key or not value:
                print(format_error("Both left-hand side and right-hand side of the statement should not be empty"))
                continue

            # Check if expression is incomplete
            if check_incomplete_expression(value):
                print(format_error("Expression is incomplete"))
                continue

            # Check if variable is referencing itself
            if key in tokenize(value):
                print(format_error("Variable should not reference itself"))
                continue

            # Check if key matches regex to only contain letters
            if not self.regex.match(key):
                print(format_error("Variable names should only contain letters"))
                continue

            # # Check for consecutive operands
            # if check_consecutive_operands(value):
            #     print(format_error("There should not be consecutive operands"))
            #     continue

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
                        # Feed it to the ParseTree to evaluate its value
                        tree = ParseTree(expression=value, hash_table=self.hash_table)
                        # Print evaluation result
                        print(f'{key}={value}=> {tree.evaluate()}')
                    # If an error occurs
                    except:
                        # Skip
                        pass