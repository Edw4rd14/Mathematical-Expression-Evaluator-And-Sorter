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
from Utils import validate_and_process_statement, handle_file, get_key_and_value, check_eq_sign, write_file, read_file
# Import Modules
import re

# AssignmentStatement Class
class AssignmentStatement:
    # Initialization
    def __init__(self):
        # Initialize HashTable Class
        self.hash_table = HashTable()
    
    # Option 1: Add/modify assignment statement
    def add_modify_statement(self, key=None, value=None, loop=True):
        # While loop to prompt users until valid input is provided
        while True:
            # Get assignment statement from user
            statement = input("Enter the assignment statement you want to add/modify:\nFor example, a=(1+2)\n")
            # Check for equal sign
            if not check_eq_sign(statement):
                continue
            # Split the statement by '='
            key, value = get_key_and_value(statement)
            # Validate and process key and value
            loop, value = validate_and_process_statement(key,value)
            if not loop:
                continue
            # Expression satisfies all conditions, add to HashTable and break out of the loop
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

    # Option 4: Read statements from a file and sort statements
    def read_statements_from_file(self):
        # While loop until valid input or user force exits
        while True:
            # Try and except to catch errors
            try:
                # Get, validate and read statements from file
                file_path = handle_file(question='Please enter input file: ', mode='r')
                # Read file
                statements = read_file(file_path)
                # Loop each statement
                for statement in statements:
                    # Check equal sign
                    if check_eq_sign(statement):
                        # Get key and value from statement
                        key, value = get_key_and_value(statement)
                        # Validate and process key and value
                        if validate_and_process_statement(key,value)[0]:
                            # Expression satisfies all conditions, add to HashTable
                            self.hash_table[key] = value
                # Display the list of current assignments (same as Option 2) and break out of loop
                self.display_statements()
                break
            # Catch any errors
            except Exception as e:
                print(e)

    # Option 5: Sort assignment statements
    def sort_statements(self):
        # While loop until valid user input or user force exits
        while True:
            try:
                # Get user input on output file path
                output_file=input("Please enter output file: ")
                
            except Exception as e:
                print(e)