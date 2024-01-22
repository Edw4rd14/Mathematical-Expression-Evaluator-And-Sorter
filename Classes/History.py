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
import json

# History class
class History(Deque):
    # Initialization
    def __init__(self, hash_table, max_length=25):
        super().__init__()
        self.hash_table = hash_table
        self.max_length = max_length
        self.__file_path = "./history.json"

    def update_file(self):
        # History array to store history to update file
        history = []
        # While deque is not empty
        while not self.is_empty:
            history.append(self.remove_tail())
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
                    if not self.contains(self,history):
                        # Insert loaded data into tail of deque
                        self.add_tail(data=tuple(history))
            # Set current node to head node
            self.current = self.head
        # If error print message
        except:
            print(f"\nError loading history. Please try again.")

    # Add History (No need for validation as all validation handled before adding)
    def add_history(self, item):
        if not len(self) >= self.max_length:
            self.add_tail(data=item)

    def remove_history(self):
        self.remove_current()

    def print_history(self, position):
        print(f"\nCurrent History Position: {position}/{self.length}")
        # Labels for each row
        labels = ['Assignment Statement:', 'Evaluated Value:', 'Timestamp:']
        # Data corresponding to each label
        data = self.current.data  # Assuming this is a tuple or list of length 3

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



