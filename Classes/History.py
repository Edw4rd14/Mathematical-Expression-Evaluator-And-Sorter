# =================================================================================================
# ST1507 DATA STRUCTURES AND ALGORITHM (AI) CA2 ASSIGNMENT: ASSIGNMENT STATEMENT EVALUATOR & SORTER
# NAME: EDWARD TAN YUAN CHONG; ASHWIN RAJ
# CLASS: DAAA/FT/2B/04
# ADM NO: 2214407; 2239716
# =================================================================================================
# FILENAME: History.py
# =================================================================================================

# Import Data Structure
from DataStructures.Deque import Deque
# Import Classes
from Classes.InputHandler import InputHandler
from Classes.ExpressionHandler import ExpressionHandler
# Import Modules
import json

# History class
class History:
    # Initialization
    def __init__(self, hash_table, max_length=25):
        """
        The __init__ function is called when the class is instantiated.
        It initializes all of the attributes that are required for this class.
        
        :param self: Refer to the instance of the class
        :param hash_table: Hash table of variables and expressions
        :param max_length: Set the max length of the history deque
        :return: Nothing
        """
        # Deque
        self.deque = Deque()
        # Hash table
        self.hash_table = hash_table
        # Max length of history
        self.max_length = max_length
        # JOSN file Path to store history
        self.__file_path = "./history.json"
        # Input handlers
        self.input_handler = InputHandler()
        self.expression_handler = ExpressionHandler()

    # Override len() - Done by Edward
    def __len__(self):
        """
        The __len__ function is a special function that returns the length of the history.        
        
        :param self: Refer to the instance of the class
        :return: The length of the deque
        """
        return len(self.deque)
    
    # History submenu - Done by Edward
    def submenu(self):
        """
        The submenu function is a menu that allows the user to navigate through their history of assignment statements.
        The history shows information of assignment statements such as variable, expression, evaluated value and timestamp at which the statement was created.
        The user can then choose whether they want to go forward or backward through this list using option 1 or 2 respectively.
        If they wish to import one of these variables into their current session, they can use option 3 which will return them back 
        to the main menu with that variable imported into their current session.
        Option 4 allows users to clear their history, and lastly option 5 returns the users back to the main menu
        
        :param self: Represent the instance of the class
        :return: Nothing
        """
        # If history is not empty
        if not self.deque.is_empty:
            # Initialize index
            index = 1
            # Total length of history
            total = len(self.deque)
            # While loop
            while True:
                # Try
                try:
                    # Next message if at first index
                    next_msg = "" if index < total else " (At the end of the list)"
                    # Previous message if at last index
                    prev_msg = "" if index > 1 else " (At the start of the list)"
                    # Print history with current index position
                    self.print_history(position=index)
                    # Get input for menu action
                    action = int(input(f"\n1. Next{next_msg}\n2. Previous{prev_msg}\n3. Import this variable\n4. Clear History \n5. Exit\nSelect your choice: "))
                    # If menu action is 1, go forward in history list
                    if action == 1:
                        # Change current data to next node
                        self.deque.go_forward()
                        # If index is not at total yet, means not at end of history list
                        if index != total:
                            # Increment index by 1
                            index += 1
                    # Else if action is 2, go back in history list 
                    elif action == 2:
                        # Change current data to previous node
                        self.deque.go_back()
                        # If index is not 1, meaning the start of the list
                        if index != 1:
                            # Decrement index by 1
                            index -= 1
                    # Else if action is 3, import variable
                    elif action == 3:
                        # Import statements
                        self.import_variables()
                        # Reset history back to head
                        self.deque.reset_to_head()
                        return
                    # Else if action is 4, clear history
                    elif action == 4:
                        # Clear history
                        self.deque.clear()
                        # Print statement and return back to main menu
                        print("\nAssignment statement history cleared. Returning back to main menu...")
                        return
                    # Else if action is 5, return back to main menu
                    elif action == 5:
                        # Reset history back to head
                        self.deque.reset_to_head()
                        return
                    # Else if action is not between 1 and 5, print error message
                    else:
                        print(f"\nOnly options between 1 and 5 are available. {self.input_handler.err_msg}\n")
                # If user input is not integer
                except ValueError:
                    print(f"\nInput must be an integer. {self.input_handler.err_msg}")
                # If keyboard interrupt
                except KeyboardInterrupt:
                    print("\nReturning back to main menu...")
                    # Reset history back to head
                    self.deque.reset_to_head()
                    break
        # Print error message if history is empty
        else:
            print("\nAssignment statement history is empty. Assignment statements can be added through options 1 and 4.")

    # Update history - Done by Edward
    def update_history(self):
        """
        The update_history function is used to update the JSON file with the current history.
        It does this by first emptying out the deque and storing it in a list, then
        writing that list to a json file.
        
        :param self: Refer to the instance of the class
        :return: Nothing
        """
        # History array to store history to update file
        history = []
        # While deque is not empty
        while not self.deque.is_empty:
            history.append(self.deque.remove_tail())
        # Open file and store history
        with open(self.__file_path, 'w') as file:
            json.dump(history, file)
    
    # Load JSON file - Done by Edward
    def load_file(self):
        """
        The load_file function is used to load the history from the JSON file.
        The function will first try to open the file and then load it into memory.
        If there are any errors, an error message will be printed.
        
        :param self: Refer to the instance of the class
        :return: Nothing
        """
        # Load from file
        try:
            # Open file and load history
            with open(self.__file_path, 'r') as file:
                total_history = json.load(file)
                # Loop loaded data
                for history in total_history:
                    if history not in self.deque:
                        # Insert loaded data into head of deque
                        self.deque.add_head(data=tuple(history))
            # Set current node to head node
            self.deque.current = self.deque.head
        # If error print message
        except:
            print(f"\nError loading history. Please try again.")

    # Add History (No need for validation as all validation handled before adding) - Done by Edward
    def add_history(self, item):
        """
        The add_history function adds a new item to the history.
        If the length of the deque is greater than or equal to max_length, then remove
        the last item from the deque and add this new item to the head of it. If not, 
        then just add this new item to the head.
        
        :param self: Refer to the instance of the class
        :param item: Item to be added to deque
        :return: Nothing
        """
        # If length of deque exceed max history length
        if len(self.deque) >= self.max_length:
            # Remove the last item from the deque
            self.deque.remove_tail()
        # Add the new item to the head of the deque
        self.deque.add_head(data=item)

    # Print history - Done by Edward
    def print_history(self, position):
        """
        The print_history function prints the current history item in a table format, including
        information such as variable, expression, evaluated value and timestamp
        
        :param self: Refer to the instance of the class
        :param position: Current position of history
        :return: Nothing
        """
        # Header
        print(f"\nCurrent History Position: {position}/{len(self.deque)}")
        # Labels for each row
        labels = ['Variable:', 'Expression:', 'Evaluated Value:', 'Timestamp:']
        # Data corresponding to each label
        data = self.deque.get_current()
        # Find the maximum length for the labels and data
        max_label_len = max(len(label) for label in labels)
        max_data_len = max(len(str(d)) for d in data)
        # Construct the horizontal border
        total_length = max_label_len + max_data_len + 5
        horizontal_border = '#' + '=' * total_length + '#'
        # Print the formatted table
        print(horizontal_border)
        for label, value in zip(labels, data):
            # Format each row with label and data in two columns
            row = f'{label.ljust(max_label_len)} | {str(value).ljust(max_data_len)}'
            print(f'| {row} |')
            print(horizontal_border)

    # Import variable & relevant variables if necessary - Done by Edward
    def import_variables(self): 
        """
        The import_variables function is used to import a statement from the deque into the hash table.
        The user can choose whether or not they want to load all of the variables in that expression as well.
        If so, then it will use the function get_related_variables to get all related variables recursively and
        add them to the hash table.
        
        :param self: Refer to the instance of the class
        :return: Nothing
        """
        # Prompt user on whether to import relevant variables
        load_relevant = self.input_handler.prompt_polar_question(question='Do you want to load all the variables in this expression as well? (Y/N): ')
        # Try and except to handle any errors
        try:
            # Count of items imported
            count = 0
            # Current variable they want to import
            current_variable = self.deque.get_current()[0]
            # If they decide to import relevant variables
            if load_relevant:
                # Get relevant variables
                relevant_variables = self.expression_handler.get_related_variables(current_variable, self.deque.items)
                # For each relevant variable
                for variable in relevant_variables:
                    try:
                        # Get expression of relevant variable
                        expression = self.deque[variable][1]
                        if self.expression_handler.validate_key_and_value(variable, expression, self.hash_table):
                            # Add relevant variable and its expression into the hash table
                            self.hash_table[variable] = expression
                            # Increment count 
                            count += 1
                    except:
                        # Catch errors for missing variables in history
                        print(f'\nFailed to import variable "{variable}".')
            # Get expression of current variable
            expression = self.deque[current_variable][1]
            # Validate the current variable and its expression
            if self.expression_handler.validate_key_and_value(current_variable, expression,self.hash_table):
                # Add current variable they wanted to import
                self.hash_table[current_variable] = expression
                # Increment count
                count += 1
            # Print success message if not errors thus far
            print(f"\n{count} variable(s) have been imported. Please use option 2 to verify them.")
        except:
            # Print random error message if error occurs
            print("\nAn error occurred while importing statements. Please restart the application or try again. Returning back to main menu...")