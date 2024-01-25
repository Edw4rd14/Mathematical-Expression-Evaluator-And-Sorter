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
    validate_key_and_value, 
    handle_file, 
    get_key_and_value, 
    check_eq_sign, 
    file_operation, 
    merge_sort
)
# Import Classes
from Classes.History import History
# Import modules
from datetime import datetime

# AssignmentStatement Class
class AssignmentStatement:
    
    # Initialization
    def __init__(self):
        # Initialize HashTable Class
        self.hash_table = HashTable()
        # Initialize History Class
        self.history = History(hash_table=self.hash_table)
    
    # Option 1: Add/modify assignment statement
    def add_modify_statement(self):
        """
        The add_modify_statement function is for option 1 where users add or modify statements. 
        The user input goes through a series of validation before the assignment statements are 
        added to the HashTable, which was the data structure implemented here.
        
        :param self: Access the hashtable data structure
        :return: None
        """
        # While loop to prompt users until valid input is provided
        while True:
            # Get assignment statement from user
            statement = input("Enter the assignment statement you want to add/modify:\nFor example, a=(1+2)\n")
            # Check for equal sign
            if not check_eq_sign(statement):
                continue
            # Split the statement by '='
            key, value = get_key_and_value(statement)
            # Validate key and value
            loop, value = validate_key_and_value(key,value)
            if not loop:
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
        statements without printing any results. The function utilizes the ParseTree data structure 
        to evaluate the assignment statements. It utilizes the SortedList data structure to sort the 
        assignment statements by variablefor option 5. Furthermore, it also utilizes the Merge Sort 
        algorithm to sort keys for displaying.
        
        :param self: Access the hash_table and history attributes of the assignmentstatement class
        :param display: Determine whether or not the assignment statements should be printed
        :return: A sortedlist object
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
            for key in merge_sort(keys):
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
                        self.history.add_history(item=(statement, evaluated_value, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
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
        :return: The value of the variable that is being evaluated
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
                    print(f'\nVariable "{variable}" does not exist. Please try again or CTRL+C to return to the main menu.\n')
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
        :return: None
        """
        # While loop until valid input or user force exits
        while True:
            # Try and except to catch errors
            try:
                # Get, validate and read statements from file
                file_path = handle_file(question='Please enter input file: ', mode='r')
                # Read file
                statements = file_operation(file_path=file_path, mode='r')
                # Loop each statement
                for statement in statements:
                    # Check equal sign
                    if check_eq_sign(statement):
                        # Get key and value from statement
                        key, value = get_key_and_value(statement)
                        # Validate key and value
                        valid, value = validate_key_and_value(key,value)
                        if valid:
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
        
        
        :param self: Access the class attributes and methods
        :return: None
        """
        # While loop until valid user input or user force exits
        while True:
            try:
                # Get and validate file path
                output_file = handle_file(question='Please enter output file: ')
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
        
        :param self: Access the hash_table of the object
        :return: A sorted list of the assignment statements in ascending order of variable names
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
            for key in merge_sort(keys):
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
        if not self.history.is_empty:
            index = 1
            total = self.history.length
            while True:
                self.history.print_history(position=index)
                try:
                    # Get input for menu action
                    action = int(input(f"\n1. Next\n2. Previous\n3. Clear History \n4. Exit\nSelect your choice: "))
                    # If menu action is 1, go forward in history list (down the list)
                    if action == 1:
                        # Change current data to next node
                        self.history.go_forward()
                        # If index is not at total yet, means not at end of history list
                        if index != total:
                            # Increment index by 1
                            index += 1
                    # Else if action is 2, go back in history list (up the list)
                    elif action == 2:
                        # Change current data to previous node
                        self.history.go_back()
                        # If index is not 1, meaning the start of the list
                        if index != 1:
                            # Decrement index by 1
                            index -= 1
                    elif action == 4:
                        return
                except:
                    print("womp womp")
        else:
            print("\nAssignment statement history is empty. Assignment statements can be added through options 1 and 5.")