# ST1507 DATA STRUCTURES AND ALGORITHM (AI) CA2 ASSIGNMENT: ASSIGNMENT STATEMENT EVALUATOR & SORTER
# NAME: EDWARD TAN YUAN CHONG; ASHWIN RAJ
# CLASS: DAAA/FT/2B/04
# ADM NO: 2214407; 2239716

# AssignmentStatement.py

# Import Module
from DataStructures.HashTable import HashTable
from DataStructures.ParseTree import ParseTree
import re

# AssignmentStatement Class
class AssignmentStatement(HashTable):
    # Initialization
    def __init__(self):
        # Initialize HashTable Class
        super().__init__()
        # Regex expression for variable
        self.regex = r"^[a-zA-Z]+$"
    
    # Option 1: Add/modify assignment statement
    def add_modify_statement(self):
        # While loop to prompt users until valid input is provided
        while True:
            # Get assignment statement
            statement = input("Enter the assignment statement you want to add/modify:\nFor example, a=(1+2)\n")
            # If '=' is in statement, which is the correct format we expect
            if '=' in statement:
                try:
                    # Split the statement by '='
                    key, value = statement.split('=')
                    # Check if key or value is empty, if it is not empty, add to HashTable and break out of option 1
                    if key and value:
                        if re.match(self.regex, key):
                            self[key] = value
                            break
                        else:
                            print("\nInvalid format! Variable names should only contain letters. Please try again or CRTL+C to return back to main menu.\n")
                    # Else if it is empty, throw error message
                    else:
                        print("\nInvalid format! Left-hand side and right-hand side of statement should not be empty. Please try again or CRTL+C to return back to main menu.\n")
                except ValueError:
                    print("\nInvalid format! Please only include one variable assignment statement at one time. Please try again or CRTL+C to return back to main menu.\n")
            # Else if there is no '=' in the statement, throw error message
            else:
                print("\nInvalid format! Please enter statement in a format such as a=(1+2) OR CRTL+C to exit back to main menu.\n")
    
    # Option 2: Display current assignment statements
    def display_statements(self):
        print('\nCURRENT ASSIGNMENTS:\n' + "*"*20)
        if all(key is None for key in self.keys):
            print("There are no current assignment statements.")
        else:
            for key in sorted(self.keys,key=lambda x: (x is None, x)): 
                try:
                    value = self[key]
                    tree = ParseTree(expression=value, hashTable=self)
                    print(f'{key}={value}=> {tree.evaluate()}')
                except:
                    pass