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
        self.deque = Deque()
        self.hash_table = hash_table
        self.max_length = max_length
        self.__file_path = "./history.json"
        self.input_handler = InputHandler()
        self.expression_handler = ExpressionHandler()

    # Override len()
    def __len__(self):
        """
        The __len__ function is a special function that returns the length of the history.        
        
        :param self: Refer to the instance of the class
        :return: The length of the deque
        """
        return len(self.deque)

    # Update file
    def update_file(self):
        """
        The update_file function is used to update the JSON file with the current history.
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
    
    # Load JSON file
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
                    if not self.deque.contains(history):
                        # Insert loaded data into head of deque
                        self.deque.add_head(data=tuple(history))
            # Set current node to head node
            self.deque.current = self.deque.head
        # If error print message
        except:
            print(f"\nError loading history. Please try again.")

    # Add History (No need for validation as all validation handled before adding)
    def add_history(self, item):
        """
        The add_history function adds a new item to the history.
        If the length of the deque is greater than or equal to max_length, then remove
        the last item from the deque and add this new item to the head of it. If not, 
        then just add this new item to the head.
        
        :param self: Refer to the instance of the class
        :param item: Item to be added to deque
        :return: None
        """
        if len(self.deque) >= self.max_length:
            # Remove the last item from the deque
            self.deque.remove_tail()
        # Add the new item to the head of the deque
        self.deque.add_head(data=item)

    # Remove history
    def remove_history(self):
        """
        The remove_history function is a public interface for removing the current item from the deque.   
        
        :param self: Refer to the instance of the class
        :return: None
        """
        self.deque.remove_current()

    # Print history
    def print_history(self, position):
        """
        The print_history function prints the current history item in a table format, including
        information such as variable, expression, evaluated value and timestamp
        
        :param self: Refer to the instance of the class
        :param position: Current position of history
        :return: None
        """
        print(f"\nCurrent History Position: {position}/{len(self.deque)}")
        # Labels for each row
        labels = ['Variable:', 'Expression:', 'Evaluated Value:', 'Timestamp:']
        # Data corresponding to each label
        data = self.deque.current.data 

        # Find the maximum length for the labels and data
        max_label_len = max(len(label) for label in labels)
        max_data_len = max(len(str(d)) for d in data)

        # Construct the horizontal border
        total_length = max_label_len + max_data_len + 5  # Additional spaces for padding and separator
        horizontal_border = '#' + '=' * total_length + '#'

        # Print the formatted table
        print(horizontal_border)
        for label, value in zip(labels, data):
            # Format each row with label and data in two columns
            row = f'{label.ljust(max_label_len)} | {str(value).ljust(max_data_len)}'
            print(f'| {row} |')
            print(horizontal_border)  # Add this line to create a row of '=' characters between each row

    # Import variable & relevant variables if necessary
    def import_variables(self): 
        """
        The import_variables function is used to import a statement from the deque into the hash table.
        The user can choose whether or not they want to load all of the variables in that expression as well.
        If so, then it will use the function get_related_variables to get all related variables recursively and
        add them to the hash table.
        
        :param self: Refer to the object that is calling the function
        :return: Nothing
        """
        # Prompt user on whether to import relevant variables
        load_relevant = self.input_handler.prompt_polar_question(question='Do you want to load all the variables in this expression as well? (Y/N): ')
        # Try and except to handle any errors
        try:
            # Count of items imported
            count = 0
            # Current variable they want to import
            current_variable = self.deque.current.data[0]
            # If they decide to import relevant variables
            if load_relevant:
                # Get relevant variables
                relevant_variables = self.expression_handler.get_related_variables(current_variable, self.deque.items)
                # For each relevant variable
                for variable in relevant_variables:
                    try:
                        # Add relevant variable and its expression into the hash table
                        self.hash_table[variable] = self.deque[variable][1]
                        # Increment count 
                        count += 1
                    except:
                        # Catch errors for missing variables in history
                        print(f'\nFailed to import variable "{variable}".')
            # Add current varaible they wanted to import
            self.hash_table[current_variable] = self.deque[current_variable][1]
            # Increment count
            count += 1
            # Print success message if not errors thus far
            print(f"\n{count} variable(s) have been successfully imported. Please use option 2 to verify them.")
        except:
            # Print random error message if error occurs
            print("\nAn error occurred while importing statements. Please restart the application or try again. Returning back to main menu...")

    # Public interface for forward in deque
    def forward(self):
        """
        The forward function moves the deque forward one position.
                
        :param self: Refer to the instance of the class
        :return: None
        """
        self.deque.go_forward()

    # Public interface for backwards in deque
    def backward(self):
        """
        The backward function moves the current node to the previous node in the deque.
                
        
        :param self: Refer to the instance of the class
        :return: None
        """
        self.deque.go_back()

    # Public interface clearing deque
    def clear_history(self):
        """
        The clear_history function clears the deque storing the history
        
        :param self: Refer to the instance of the class
        :return: Nothing
        """
        self.deque.clear()

    # Public interface for resetting deque to head
    def reset_to_head(self):
        """
        The reset_to_head function resets the current node to the head of the deque.
                
        :param self: Refer to the instance of the class
        :return: None
        """
        self.deque.reset_to_head()


