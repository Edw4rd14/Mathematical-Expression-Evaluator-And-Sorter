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
from DataStructures.Deque import Deque
# Import Classes
from Classes.History import History
from Classes.ExpressionHandler import ExpressionHandler
from Classes.FileHandler import FileHandler
from Classes.InputHandler import InputHandler
from Classes.MergeSort import MergeSort
# Import Modules
from datetime import datetime

# AssignmentStatement class
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
        # Initialize handler classes
        self.expression_handler = ExpressionHandler()
        self.input_handler = InputHandler()
        self.file_handler = FileHandler()
    
    # Option 1: Add/modify assignment statement
    def add_modify_statement(self):
        """
        The add_modify_statement function is for option 1 where users add or modify statements. 
        The user input goes through a series of validation before the assignment statements are 
        added to the HashTable, which was the data structure implemented here.
        
        :param self: Refer to the instance of the class
        :return: Nothing
        """
        # While loop to prompt users until valid input is provided
        while True:
            # Get assignment statement from user
            statement = input("Enter the assignment statement you want to add/modify:\nFor example, a=(1+2)\n")
            # Check for equal sign
            if not self.expression_handler.check_eq_sign(statement):
                continue
            # Split the statement by '='
            key, value = self.expression_handler.get_key_and_value(statement)
            # Validate key and value
            if not self.expression_handler.validate_key_and_value(key,value):
                continue
            # Expression satisfies all conditions, add to HashTable and break out of the loop
            self.hash_table[key] = value
            # Update sorted statements in SortedList for option 5 and 7
            self.update_statements()
            break

    # Evaluate current assignment statements
    def sort_and_evaluate_statements(self):
        """
        The sort_and_evaluate_statements function will take the hash table keys (variables) that are not none, use the merge sort algorithm
        to sort them in an ascending alphabetical order, then evaluate each variable and store them in an deque that is returned
        
        :param self: Refer to the instance of the class
        :return: A deque with the expressions and evaluated values
        """
        deque = Deque()
        # Loop each sorted key from merge sort
        for key in MergeSort.sort(self.hash_table.filtered_keys):
            # If key is not None and is an assignment statement
            if key is not None:
                # Catch errors with try
                try:
                    # Try grabbing the assignment statement value
                    value = self.hash_table[key]
                    # Evaluate value of expression with ParseTree
                    tree = ParseTree(variable=key, expression=value, hash_table=self.hash_table)
                    # Get evaluated value of expression
                    evaluated_value = tree.evaluate()
                    # Add to stack
                    deque.add_head(data=(key,value,evaluated_value))
                # Catch value error
                except ValueError as e:
                    print(e)
                # If an error occurs, pass
                except Exception:
                    print("An occurred while trying to display and sort assignment statements. Please try again or restart the application.")
                    pass
        return deque

    # Option 2: Display current assignment statements
    def display_statements(self):
        """
        The display_statements function takes the sorted assignment statements
        and displays them in the format variable=expression => evaluated value.
        
        :param self: Refer to the instance of the class
        :return: Nothing
        """
        deque = self.sort_and_evaluate_statements()
        print('\nCURRENT ASSIGNMENTS:\n' + "*"*20)
        if deque.is_empty:
            print("There are no current assignment statements.")
        while not deque.is_empty:
            key, value, evaluated = deque.remove_head()
            print(f"{key}={value}=> {evaluated}")

    # Update history and sorted list
    def update_statements(self):
        """
        The update_statements function is responsible for updating the sorted_list and history.
        
        :param self: Refer to the instance of the class
        :return: Nothing
        """
        deque = self.sort_and_evaluate_statements()
        self.sorted_list = SortedList()
        while not deque.is_empty:
            key, value, evaluated = deque.remove_head()
            self.sorted_list.insert(new_data=(f"{key}={value}", evaluated))
            self.history.add_history(item=(key, value, evaluated, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

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
                    tree = ParseTree(variable=variable, expression=expression, hash_table=self.hash_table)
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
                    print(f'\nVariable "{variable}" does not exist. {self.input_handler.err_msg}')
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
                file_path = self.file_handler.validate_file(question='Please enter input file: ', mode='r')
                # Read file 
                statements = self.file_handler.file_operation(file_path=file_path, mode='r')  
                # Loop each statement
                for statement in statements:
                    # Check equal sign
                    if self.expression_handler.check_eq_sign(statement, False):
                        # Get key and value from statement
                        key, value = self.expression_handler.get_key_and_value(statement)
                        # Validate key and value
                        if self.expression_handler.validate_key_and_value(key,value,False):
                            # Expression satisfies all conditions, add to HashTable
                            self.hash_table[key] = value
                # Display the list of current assignments (same as Option 2) and store new statements
                self.display_statements()
                self.update_statements()
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
                output_file = self.file_handler.validate_file(question='Please enter output file: ')
                # Process assignment statements and write to file
                self.file_handler.file_operation(file_path=output_file, mode='w',content=self.sorted_list.print_sorted())
                break
            except AttributeError:
                print("\nPlease ensure that there are assignment statements added before sorting.")
                break
            except Exception as e:
                print(e)

    # Option 6:
    def batch_process(self):
        """
        The batch_process function is used to process multiple files at once.
        It takes in a folder path and processes each file in the folder, evaluating and sorting assignment statements,
        and produces a list of variable dependencies between variables then writes the results of each file to an output text file.
        
        :param self: Refer to the instance of the class
        :return: Nothing
        """
        # Validate and get the folder path for batch processing
        folder_path = self.file_handler.validate_folder(question='Please enter folder to batch process: ')
        # Border for formatting
        border = "="*60
        # Read files from the folder and initialize processing
        file_deque, dir_name = self.file_handler.read_folder(folder_path=folder_path)
        # Initialize file counter
        count = 1  
        # Initialize logs
        logs = "Batch Processing Logs\n" + "="*25 + "\nInput file => Output file\n" + "=" * 25
        # Process each file in the deque
        while not file_deque.is_empty:
            # Temporary storage for variables and their values
            temp_hashtable = HashTable()  
            # String to hold variable dependencies
            var_dependency = ""  
            # Get the next file's name and content
            file_name, file_content = file_deque.remove_head()  
            # Prepare a sorted list for evaluated expressions
            sorted_list = SortedList()  
            # String to accumulate errors found during processing
            errors = "" 
            # Statement error flag
            statement_error_flag = False
            # Print formatting
            print("\n"+border)
            print(f"File '{file_name}':")
            # Process each statement in the file content
            for statement in file_content:
                # Check if the statement contains an equal sign, skip if not
                if not self.expression_handler.check_eq_sign(statement, False):
                    statement_error_flag = True
                    continue
                # Extract key (variable) and value from the statement
                key, value = self.expression_handler.get_key_and_value(statement)
                # Validate the extracted key and value
                if self.expression_handler.validate_key_and_value(key, value, False):
                    # Store the valid key-value pair in the hashtable
                    temp_hashtable[key] = value
                else:
                    statement_error_flag = True
            # Evaluate expressions and dependencies for each key in the hashtable
            for key in MergeSort.sort(temp_hashtable.filtered_keys):
                if key is not None:
                    try:
                        # Evaluate the expression for the current key and add to sorted list
                        value = temp_hashtable[key]
                        evaluated = ParseTree(variable=key, expression=value, hash_table=temp_hashtable).evaluate()
                        sorted_list.insert(new_data=(f"{key}={value}", evaluated))
                        # Get dependencies of the current variable
                        key_value_pairs = [self.expression_handler.get_key_and_value(stmt) for stmt in file_content]
                        relevant_vars = self.expression_handler.get_related_variables(key, key_value_pairs)
                        var_dependency += self.expression_handler.format_dependency(variable=key, dependencies=relevant_vars)
                    except ValueError as ve:
                        # Accumulate errors encountered during evaluation
                        errors += str(ve)
            # Prepare evaluated statements for output
            evaluated_statements = sorted_list.print_sorted()
            # Handle cases where no errors, no evaluated statements, or no variable dependencies were found
            if evaluated_statements == "":
                evaluated_statements = "Please double check the original file and ensure that it is not empty or has unresolved errors." 
                errors = "\nThere are unresolved error(s) in the file."
            if var_dependency == "":
                var_dependency = "Please double check the original file and ensure that it is not empty or has unresolved errors." 
                errors = "\nThere are unresolved error(s) in the file."
            # Print errors from processing the file
            if errors:
                print(errors)
            if statement_error_flag:
                print("\nStatement error(s) occurred while processing file.")
            if not errors and not statement_error_flag:
                print("\nNo errors while processing file.")
            print(border)
            # Compile content for output file and write it to file
            content = (
                f"Original Filename: {file_name}\n\n"
                "====================\n"
                "Evaluated Statements\n"
                "====================\n\n"
                f"{evaluated_statements}\n\n"
                "========================\n"
                "Variable Dependency List\n"
                "========================\n\n"
                f"{var_dependency}"
            )
            # Output file name
            output_file_name = f"file-{count}.txt"
            # Write to output file
            self.file_handler.file_operation(file_path=f"{dir_name}/{output_file_name}", mode='w', content=content, menu=False)
            # Increment file counter
            count += 1  
            # Update logs
            logs += f"\n{file_name} => {output_file_name}"
        # Write logs to logs.txt
        self.file_handler.file_operation(file_path=f"{dir_name}/logs.txt", mode='w', content=logs, menu=False)
    # Option 7: Manage assignment statement history
    def manage_history(self):
        if not self.history.deque.is_empty:
            index = 1
            total = len(self.history)
            while True:
                try:
                    next_msg = "" if index < total else " (At the end of the list)"
                    prev_msg = "" if index > 1 else " (At the start of the list)"
                    self.history.print_history(position=index)
                    # Get input for menu action
                    action = int(input(f"\n1. Next{next_msg}\n2. Previous{prev_msg}\n3. Import this variable\n4. Clear History \n5. Exit\nSelect your choice: "))
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
                        # Import statements
                        self.history.import_variables()
                        # Reset history back to head
                        self.history.reset_to_head()
                        return
                    # Else if action is 4, clear history
                    elif action == 4:
                        # Clear history
                        self.history.clear_history()
                        # Print statement and return back to main menu
                        print("\nAssignment statement history cleared. Returning back to main menu...")
                        return
                    # Else if action is 5, return back to main menu
                    elif action == 5:
                        # Reset history back to head
                        self.history.reset_to_head()
                        return
                except ValueError:
                    print(f"\nInput must be an integer. {self.input_handler.err_msg}")
                except KeyboardInterrupt:
                    print("\nReturning back to main menu...")
                    # Reset history back to head
                    self.history.reset_to_head()
                    break
        else:
            print("\nAssignment statement history is empty. Assignment statements can be added through options 1 and 4.")

    # Update history function
    def update_history(self):
        """
        The update_history function is the public interface method for the
        history function to update the file
        
        :param self: Refer to the instance of the class
        :return: Nothing
        """
        self.history.update_file()

    # Option 8: Remove all assignment statements
    def remove_all_statements(self):
        """
        The remove_all_statements function removes all assignment statements from the hash table, sorted list and history.
        
        :param self: Refer to the instance of the class
        :return: Nothing
        """
        # Confirmation from the user
        confirmation = self.input_handler.prompt_polar_question(question="Are you sure you want to remove all assignment statements? (Y/N): ")
        # Check user's confirmation
        if confirmation:
            try:
                # Clear the hash_table
                self.hash_table.clear()
                # Clear the sorted list
                self.sorted_list.clear()
                # Clear the history
                self.history.clear_history()
                # Display a message indicating that all statements have been removed
                print("\nAll assignment statements have been removed.")
            except:
                print("\nThere are no assignment statements to be removed.")
        else:
            # Display a message indicating that no changes have been made
            print("\nNo changes have been made.")

    # Option 9:
    def calculate_total(self):
        total_value = 0

        # Iterate through each statement and accumulate the total value
        for statement in super().get_statements():
            try:
                key, value = self.expression_handler.get_key_and_value(statement)
                evaluated_value = super().evaluate_expression(value)
                total_value += evaluated_value
            except Exception as e:
                print(f"Error processing statement: {statement}. {str(e)}")

        # Output the total value
        print(f"\nTotal value of all statements: {total_value}\n")