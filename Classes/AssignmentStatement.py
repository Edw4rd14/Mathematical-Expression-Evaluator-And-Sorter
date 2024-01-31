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
from DataStructures.SortedList import SortedList
# Import Utils
from Utils import (
    get_key_and_value, 
    file_operation
)
# Import Classes
from Classes.History import History
from Classes.InputValidation import InputValidation
from Classes.Sorter import Sorter
# Import modules
from datetime import datetime

# AssignmentStatement Class
class AssignmentStatement:
    
    # Initialization
    def __init__(self):
        """
        The __init__ function is called when the class is instantiated.
        It initializes all of the attributes that are required for this class.
        
        :param self: Refer to the instance of the class
        :return: Nothing
        """
        # Initialize HashTable Class
        self.hash_table = HashTable()
        # Initialize History Class
        self.history = History(hash_table=self.hash_table)
        # Load history file statements into history
        self.history.load_file()
        # Initialize InputValidation class 
        self.input_validation = InputValidation()
    
    # Option 1: Add/modify assignment statement
    def add_modify_statement(self):
        """
        The add_modify_statement function is for option 1 where users add or modify statements. 
        The user input goes through a series of validation before the assignment statements are 
        added to the HashTable, which was the data structure implemented here.
        
        :param self: Access the hashtable data structure
        :return: Nothing
        """
        # While loop to prompt users until valid input is provided
        while True:
            # Get assignment statement from user
            statement = input("Enter the assignment statement you want to add/modify:\nFor example, a=(1+2)\n")
            # Check for equal sign
            if not self.input_validation.check_eq_sign(statement):
                continue
            # Split the statement by '='
            key, value = get_key_and_value(statement)
            # Validate key and value
            if not self.input_validation.validate_key_and_value(key,value):
                continue
            # Expression satisfies all conditions, add to HashTable and break out of the loop
            self.hash_table[key] = value
            # Update sorted statements in SortedList for option 5
            self.display_and_sort_statements(display=False)
            break
    
    # Option 2: Display current assignment statements
    def display_and_sort_statements(self, display=True):
        """
        The display_and_sort_statements function is for option 2 where users display the assignment statements created/imported 
        from text files. The function is also utilized in option 5 in order to sort the assignment
        statements without printing any results. This function is also utilized for option 7 for the
        assignment statement historyas this function loops through each assignment statement and stores it. 
        The function utilizes the ParseTree data structure to evaluate the assignment statements. It 
        utilizes the SortedList data structure to sort the assignment statements by variablefor option 5. 
        Furthermore, it also utilizes the Merge Sort algorithm to sort keys for displaying.
        
        :param self: Access the hash_table and history attributes of the assignmentstatement class
        :param display: Determine whether or not the assignment statements should be printed
        :return: Nothing
        """
        # Sorted List to store results sorted
        self.sorted_list = SortedList()
        # If display boolean is True (default is True)
        if display:
            # Print header
            print('\nCURRENT ASSIGNMENTS:\n' + "*"*20)
        # Check if there are any assignment statements (if there isnt all keys are None)
        if all(key is None for key in self.hash_table.keys):
            # Print error statement if there are no assignment statements
            print("There are no current assignment statements.")
        # Else if there are assignment statements
        else:
            # Get all keys that are not None
            keys = [key for key in self.hash_table.keys if key is not None]
            # Loop each sorted key from merge sort
            for key in Sorter.sort(keys):
                # If key is not None and is an assignment statement
                if key is not None:
                    # Catch errors with try
                    try:
                        # Try grabbing the assignment statement value
                        value = self.hash_table[key]
                        # Formulate statement string
                        statement = f'{key}={value}'
                        # Evaluate value of expression with ParseTree
                        tree = ParseTree(expression=value, hash_table=self.hash_table)
                        # Get evaluated value of expression
                        evaluated_value = tree.evaluate()
                        # If display boolean is True (default is True)
                        if display:
                            # Print evaluation result
                            print(f'{statement}=> {evaluated_value}')
                        # Add evaluation result to SortedList
                        self.sorted_list.insert(new_data=(statement, evaluated_value))
                        # Add evaluation result to History
                        self.history.add_history(item=(key, value, evaluated_value, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
                    # If an error occurs, pass
                    except Exception:
                        print("An occurred while trying to display and sort assignment statements. Please try again or restart the application.")
                        pass

    # Option 3: Evaluate and print parse tree for an individual variable
    def evaluate_single_variable(self):
        """
        The evaluate_single_variable function is for option 3 where users evaluate one variable and view 
        the evaluation of it in a in-order traversal format. The function mainly utilizes the HashTable and ParseTree data structures.
        
        :param self: Refer to the current instance of a class
        :return: Nothing
        """
        # Get variable from user input
        while True:
            variable = input("Please enter the variable you want to evaluate:\n")
            try:
                # Get the expression associated with the variable
                expression = self.hash_table[variable]
                # If expression exists
                if expression is not None:
                    # Build parse tree
                    tree = ParseTree(expression=expression, hash_table=self.hash_table)
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
                    print(f'\nVariable "{variable}" does not exist. {self.input_validation.err_msg}')
            # Catch Any Errors
            except:
                pass

    # Option 4: Read statements from a file
    def read_statements_from_file(self):
        """
        The read_statements_from_file function is for option 4 where users read assignment statements from a file. This option
                includes file operations handled by the Utilities file (Utils.py), and reads the file and validates 
                and adds each assignment statement into the HashTable, then displays the statements (Option 2)
        
        :param self: Refer to the instance of the class
        :return: Nothing
        """
        # While loop until valid input or user force exits
        while True:
            # Try and except to catch errors
            try:
                # Get, validate and read statements from file
                file_path = self.input_validation.validate_file(question='Please enter input file: ', mode='r')
                # Read file
                statements = file_operation(file_path=file_path, mode='r')
                # Loop each statement
                for statement in statements:
                    # Check equal sign
                    if self.input_validation.check_eq_sign(statement):
                        # Get key and value from statement
                        key, value = get_key_and_value(statement)
                        # Validate key and value
                        if self.input_validation.validate_key_and_value(key,value):
                            # Expression satisfies all conditions, add to HashTable
                            self.hash_table[key] = value
                # Display the list of current assignments (same as Option 2) and break out of loop
                self.display_and_sort_statements()
                break
            # Catch any errors
            except Exception as e:
                print(e)

    # Option 5: Sort assignment statements
    def sort_statements(self):
        """
        The sort_statements function is for option 5 where users sort their assignment statements and outputs them
        into a text file, and utilizes file operations handled by the Utilities file as well.
        
        :param self: Refer to the instance of the class
        :return: Nothing
        """
        # While loop until valid user input or user force exits
        while True:
            try:
                # Get and validate file path
                output_file = self.input_validation.validate_file(question='Please enter output file: ')
                # Process assignment statements and write to file
                file_operation(file_path=output_file, mode='w',content=self.sorted_list.print_sorted())
                break
            except AttributeError:
                print("\nPlease check menu option 2 for the assignment statements before sorting.")
                break
            except Exception as e:
                print(e)

    # Option 6:
    def view_dependency(self):
        """
        The view_dependency function is used to display the dependency of each variable.
        It will print out all variables and their dependencies in a sorted order.
        If there are no assignment statements, it will print an error statement.
        
        :param self: Refer to the instance of the class
        :return: Nothing
        """
        # Sorted List to store results sorted
        self.sorted_list = SortedList()
        # If display boolean is True (default is True)
        # Check if there are any assignment statements (if there isnt all keys are None)
        if all(key is None for key in self.hash_table.keys):
            # Print error statement if there are no assignment statements
            print("There are no current assignment statements.")
        # Else if there are assignment statements
        else:
            # Get all keys that are not None
            keys = [key for key in self.hash_table.keys if key is not None]
            # Loop each sorted key from merge sort
            for key in Sorter.merge_sort(keys):
                # If key is not None and is an assignment statement
                if key is not None:
                    # Catch errors with try
                    try:
                        # Try grabbing the assignment statement value
                        value = self.hash_table[key]
                        # Evaluate value of expression with ParseTree
                        tree = ParseTree(expression=value, hash_table=self.hash_table)
                        # Get evaluated value of expression
                        tree.display_variable_dependencies()
                    # # If an error occurs, pass
                    except Exception as e:
                        print(e)
                        pass
        
    def manage_history(self):
        print(len(self.history))
        if not self.history.deque.is_empty:
            index = 1
            total = len(self.history)
            while True:
                try:
                    self.history.print_history(position=index)
                    # Get input for menu action
                    action = int(input(f"\n1. Next\n2. Previous\n3. Import this variable\n4. Clear History \n5. Exit\nSelect your choice: "))
                    # If menu action is 1, go forward in history list (down the list)
                    if action == 1:
                        # Change current data to next node
                        self.history.forward()
                        # If index is not at total yet, means not at end of history list
                        if index != total:
                            # Increment index by 1
                            index += 1
                    # Else if action is 2, go back in history list (up the list)
                    elif action == 2:
                        # Change current data to previous node
                        self.history.backward()
                        # If index is not 1, meaning the start of the list
                        if index != 1:
                            # Decrement index by 1
                            index -= 1
                    # Else if action is 3, import variable
                    elif action == 3:
                        print(self.history.deque.current.data)
                        self.history.import_statement()
                        return
                    # Else if action is 4, clear history
                    elif action == 4:
                        # Clear history
                        self.history.clear_history()
                        # Print statement and return back to main menu
                        print("Assignment statement history cleared. Returning back to main menu...")
                        return
                    # Else if action is 5, return back to main menu
                    elif action == 5:
                        # Reset history back to head
                        self.history.reset_to_head()
                        return
                except ValueError:
                    print(f"\nInput must be an integer. {self.input_validation.err_msg}")
                except KeyboardInterrupt:
                    print("\nReturning back to main menu...")
                    break
        else:
            print("\nAssignment statement history is empty. Assignment statements can be added through options 1 and 4.")

    def update_history(self):
        self.history.update_file()

    # Option 8:
    def remove_all_statements(self):
        # Confirmation from the user
        confirmation = input("Are you sure you want to remove all assignment statements? (y/n): ").lower()
        
        # Check user's confirmation
        if confirmation == 'y':
            # Clear the hash_table
            self.hash_table.clear()
            
            # Display a message indicating that all statements have been removed
            print("All assignment statements have been removed.")
            
            # Clear the sorted list and history
            self.sorted_list.clear()
            self.history.clear()
        else:
            # Display a message indicating that no changes have been made
            print("No changes have been made.")

    # Option 9:
    # Inside the AssignmentStatement class
    def display_information(self):
        """
        The display_information function is for option 9 where users can display some general information or a message.
        
        :param self: Access the AssignmentStatement class
        :return: None
        """
        print("\nQ: Some question")
        print("A: Some answer")

