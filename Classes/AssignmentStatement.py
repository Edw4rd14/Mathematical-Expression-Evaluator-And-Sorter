# ST1507 DATA STRUCTURES AND ALGORITHM (AI) CA2 ASSIGNMENT: ASSIGNMENT STATEMENT EVALUATOR & SORTER
# NAME: EDWARD TAN YUAN CHONG; ASHWIN RAJ
# CLASS: DAAA/FT/2B/04
# ADM NO: 2214407; 2239716

# AssignmentStatement.py

# Import Module
from DataStructures.HashTable import HashTable

# AssignmentStatement Class
class AssignmentStatement(HashTable):
    # Initialization
    def __init__(self):
        # Initialize HashTable Class
        super().__init__()
    
    # Option 1: Add/modify assignment statement
    def add_modify_statement(self):
        # While loop to prompt users until valid input is provided
        while True:
            # Get assignment statement
            statement = input("Enter the assignment statement you want to add/modify:\nFor example, a=(1+2)\n")
            # If '=' is in statement, which is the correct format we expect
            if '=' in statement:
                # Split the statement by '='
                try:
                    key, value = statement.split('=')
                    # Check if key or value is empty, if it is not empty, add to HashTable and break out of option 1
                    if key.strip() and value.strip():
                        self[key.strip()] = value.strip()
                        break
                    # Else if it is empty, throw error message
                    else:
                        print("\nInvalid format! Left-hand side and right-hand side of statement should not be empty. Please try again or CRTL+C to return back to main menu.\n")
                except ValueError:
                    print("\nInvalid format! Please only include one variable assignment statement at one time. Please try again or CRTL+C to return back to main menu.\n")
            # Else if there is no '=' in the statement, throw error message
            else:
                print("\nInvalid format! Please enter statement in a format such as a=(1+2) OR CRTL+C to exit back to main menu.\n")
    
    def display_statements(self):
        print('a')
    
