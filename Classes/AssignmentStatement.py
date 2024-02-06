# =================================================================================================
# ST1507 DATA STRUCTURES AND ALGORITHM (AI) CA2 ASSIGNMENT: ASSIGNMENT STATEMENT EVALUATOR & SORTER
# NAME: EDWARD TAN YUAN CHONG; ASHWIN RAJ
# CLASS: DAAA/FT/2B/04
# ADM NO: 2214407; 2239716
# =================================================================================================
# FILENAME: AssignmentStatement.py
# =================================================================================================

# Import Data Structures
from DataStructures.HashTable import HashTable
from DataStructures.ParseTree import ParseTree
from DataStructures.SortedList import SortedList
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
        # Initialize Sorted List
        self.sorted_list = SortedList()
    
    # Option 1: Add/modify assignment statement - Done by Edward
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
            if not self.expression_handler.validate_key_and_value(key, value, self.hash_table):
                continue
            # Add to hash table
            self.hash_table[key] = value
            # Evaluate and update history and sorted list
            self.evaluate_and_store_statement()
            break
    
    # Evaluate and store assignment statements in history and sorted list
    def evaluate_and_store_statement(self):
        """
        The evaluate_and_store_statement function evaluates every assignment statement in the hash table, 
        and stores the information in the sorted list and history.

        We chose to evaluate all the statements at once as we want to keep the evaluation most updated after adding
        every assignment statement, as if it is done when every assignment statement is added, it will need to be 
        re-evaluated to accommodate for newly added assignment statements to update previous added assignment statements.
        
        :param self: Refer to the instance of the class
        :return: Nothing
        """
        # Loop through each existing key
        for key in self.hash_table.filtered_keys:
            # Get value
            value = self.hash_table[key]
            # Evaluate statement
            tree = ParseTree(variable=key, expression=value, hash_table=self.hash_table)
            evaluated = tree.evaluate()
            # Store in sorted list and history
            self.sorted_list.insert(new_data=((key,value), evaluated))
            self.history.add_history(item=(key, value, evaluated, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

    # Option 2: Display current assignment statements - Done by Edward
    def display_statements(self):
        """
        The display_statements function takes the sorted assignment statements
        and displays them in the format variable=expression => evaluated value.
        
        :param self: Refer to the instance of the class
        :return: Nothing
        """
        # deque = self.sort_and_evaluate_statements()
        print('\nCURRENT ASSIGNMENTS:\n' + "*"*20)
        if self.sorted_list.is_empty:
            print("There are no current assignment statements.")
        else:
            # All statements
            all_statements = self.sorted_list.items
            # Sort variables
            sorted_variables = MergeSort.sort(list(all_statements.keys()))
            # Iterate through sorted variables and print statements
            for variable in sorted_variables:
                expression, evaluated = all_statements[variable]
                print(f'{variable}={expression}=> {evaluated}')

    # Option 3: Evaluate and print parse tree for an individual variable - Done by Edward & Ashwin
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

    # Option 4: Read statements from a file - Done by Edward & Ashwin
    def read_statements_from_file(self):
        """
        The read_statements_from_file function is for option 4 where users read assignment statements from a file.
        
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
                        if self.expression_handler.validate_key_and_value(key,value,self.hash_table,False):
                            # Expression satisfies all conditions, add to HashTable
                            self.hash_table[key] = value
                # Evaluate and update history and sorted list
                self.evaluate_and_store_statement()
                # Display the list of current assignments (same as Option 2)
                self.display_statements()
                # Break out of loop
                break
            # Catch any errors
            except Exception as e:
                print(e)

    # Option 5: Sort assignment statements - Done by Edward
    def sort_statements(self):
        """
        The sort_statements function is for option 5 where users sort their assignment statements and outputs them
        into a text file.
        
        :param self: Refer to the instance of the class
        :return: Nothing
        """
        # If there are no assignment statements
        if self.sorted_list.is_empty:
            # Print error
            print("\nThere are no assignment statements to sort. Returning back to main menu...")
        else:
            # While loop until valid user input or user force exits
            while True:
                # Try and except to catch errors
                try:
                    # Get and validate file path
                    output_file = self.file_handler.validate_file(question='Please enter output file: ')
                    # Process assignment statements and write to file
                    self.file_handler.file_operation(file_path=output_file, mode='w',content=self.sorted_list.print_sorted())
                    # Break out of loop
                    break
                # Print error received
                except Exception as e:
                    print(e)

    # Option 6: Batch process files - Done by Edward (Additional)
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
        border = "="*100
        # Read files from the folder and initialize processing
        file_deque, dir_name = self.file_handler.read_folder(folder_path=folder_path)
        # Initialize file counter
        count = 1  
        # Initialize logs
        logs = "Batch Processing Logs\n" + "="*25 + "\nInput file => Output file\n" + "=" * 25
        # Process each file in the deque
        if not file_deque.is_empty:
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
                    if self.expression_handler.validate_key_and_value(key, value, temp_hashtable, False):
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
                            sorted_list.insert(new_data=((key,value), evaluated))
                            # Get dependencies of the current variable
                            relevant_vars = self.expression_handler.get_related_variables(key, [(key, value) for key, value in zip(temp_hashtable.keys, temp_hashtable.buckets) if key is not None])
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
        else:
            print(f"\nThere were no text files detected in '{dir_name}'.")

    # Option 7: Manage assignment statement history - Done by Edward
    def manage_history(self):
        """
        The manage_history function calls the submenu of the history to allow users to view and manage their 
        assignment statement history.
    
        :param self: Refer to the current instance of the class
        :return: Nothing
        """
        # Call history submenu
        self.history.submenu()
        # Re-evaluate statements if there was any imported
        self.evaluate_and_store_statement()

    # Option 8: Remove all assignment statements - Done by Aswhin
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
                self.history.deque.clear()
                # Display a message indicating that all statements have been removed
                print("\nAll assignment statements have been removed.")
            except:
                print("\nThere are no assignment statements to be removed.")
        else:
            # Display a message indicating that no changes have been made
            print("\nNo changes have been made.")

    # Option 9: Display statistics - Done by Aswhin
    def display_statistics(self):
        """
        The display_statistics function calculates and displays basic statistics about the assignment statements.

        :param self: Refer to the instance of the class
        :return: Nothing
        """
        # Get total statement count
        total_statements = sum(1 for bucket in self.hash_table.buckets if bucket is not None)
        # Total length of expressions
        total_length = sum(len(bucket) for bucket in self.hash_table.buckets if bucket is not None)
        # Average length of expressions
        average_length = total_length / total_statements if total_statements > 0 else 0
        # Print results
        print(f"\nBasic Statistics:")
        print(f"Total Assignment Statements: {total_statements}")
        print(f"Average Length of Statements: {average_length:.2f} characters")




