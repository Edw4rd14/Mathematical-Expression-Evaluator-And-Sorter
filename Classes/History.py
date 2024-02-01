# =================================================================================================
# ST1507 DATA STRUCTURES AND ALGORITHM (AI) CA2 ASSIGNMENT: ASSIGNMENT STATEMENT EVALUATOR & SORTER
# NAME: EDWARD TAN YUAN CHONG; ASHWIN RAJ
# CLASS: DAAA/FT/2B/04
# ADM NO: 2214407; 2239716
# =================================================================================================
# FILENAME: History.py
# =================================================================================================
'''
Description:
This is the History file of the application which handles option 7
'''

# Import Data Structure
from DataStructures.Deque import Deque
from DataStructures.ParseTree import ParseTree
# Import modules
import json
# Import Classes
from Classes.InputValidation import InputValidation

# History class
class History:
    # Initialization
    def __init__(self, hash_table, max_length=25):
        self.deque = Deque()
        self.hash_table = hash_table
        self.max_length = max_length
        self.__file_path = "./history.json"
        self.input_validation = InputValidation()

    def __len__(self):
        return len(self.deque)

    def update_file(self):
        # History array to store history to update file
        history = []
        # While deque is not empty
        while not self.deque.is_empty:
            history.append(self.deque.remove_tail())
        # Open file and store history
        with open(self.__file_path, 'w') as file:
            json.dump(history, file)
    
    def load_file(self):
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
        if not len(self.deque) >= self.max_length:
            self.deque.add_head(data=item)

    def remove_history(self):
        self.deque.remove_current()

    def print_history(self, position):
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
        load_relevant = self.input_validation.prompt_polar_question(question='Do you want to load all the variables in this expression as well? (Y/N): ')
        # Try and except to handle any errors
        try:
            # Current variable they want to import
            current_variable = self.deque.current.data[0]
            # If they decide to import relevant variables
            if load_relevant:
                # Get relevant variables
                relevant_variables = self.get_related_variables(current_variable)
                # For each relevant variable
                for variable in relevant_variables:
                    # Add relevant variable and its expression into the hash table
                    self.hash_table[variable] = self.deque.get_specific_object(variable)[1]
            # Add current varaible they wanted to import
            self.hash_table[current_variable] = self.deque.get_specific_object(current_variable)[1]
            # Print success message if not errors thus far
            print("\nVariable(s) have been successfully imported. Please use option 2 to verify them.")
        except:
            # Print random error message if error occurs
            print("\nAn error occurred while importing statements. Please restart the application or try again. Returning back to main menu...")

    @staticmethod        
    def extract_variables(item):
        variables = []
        for t in ParseTree.tokenize(item):
            if t.isalpha():
                variables.append(t)
        return variables

    def get_related_variables(self, variable):
        all_items = self.deque.get_all_objects()
        for item in all_items:
            if item[0] == variable:
                # Extract variables from the expression
                variables = self.extract_variables(item[1])
                # Recursively get related variables for each found variable
                related_variables = set(variables)
                for v in variables:
                    related_variables.update(self.get_related_variables(v))
                return related_variables
        return set()

    def forward(self):
        self.deque.go_forward()

    def backward(self):
        self.deque.go_back()

    def clear_history(self):
        self.deque.clear()

    def reset_to_head(self):
        self.deque.reset_to_head()


