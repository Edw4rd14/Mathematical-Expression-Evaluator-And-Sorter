# =================================================================================================
# ST1507 DATA STRUCTURES AND ALGORITHM (AI) CA2 ASSIGNMENT: ASSIGNMENT STATEMENT EVALUATOR & SORTER
# NAME: EDWARD TAN YUAN CHONG; ASHWIN RAJ
# CLASS: DAAA/FT/2B/04
# ADM NO: 2214407; 2239716
# =================================================================================================
# FILENAME: SortedList.py
# =================================================================================================

# Import Data Structures
from DataStructures.Node import Node

# SortedList class
class SortedList:
    # Initialization
    def __init__(self):
        """
        The __init__ function is called when the class is instantiated.
        It initializes all of the attributes that are required for this class.
        
        :param self: Refer to the instance of the class
        :return: Nothing
        """
        # Initialize head node
        self.head_node = None
        # Initialize current node
        self.current_node = None
        # Initialize length
        self._length = 0 
    
    # Length of sorted list - Done by Ashwin
    def __len__(self): 
        """
        This function returns the length of the sorted list with Python's built-in len() function
        
        :param self: Refer to the instance of the class
        :return: The length of the queue
        """
        # Return length
        return self._length

    # Iterator for sorted list - Done by Ashwin
    def __iter__(self):
        """
        The __iter__ function is called when an iterator object is required for a container. 
        This function returns a new iterator object that can iterate over all the objects in the sorted list. 

        :param self: Refer to the instance of the class
        :return: The iterator object itself
        """
        # When object is iterated, set current_node to head_node to start looping from the head
        self.current_node = self.head_node
        # Return self as iterator object to be looped
        return self

    # Get next iterator for iteration for sorted list - Done by Ashwin
    def __next__(self):
        """
        The __next__ function is called by the Python interpreter to get each item from an iterator. 
        
        :param self: Refer to the instance of the class
        :return: The current node's tuple data
        """
        # If current_node exists (which means it is not the end of the iteration),
        if self.current_node:
            # Set data to be returned to current node's tuple data
            current_node = self.current_node
            # Set current node variable to next node for next iteration
            self.current_node = self.current_node.next_node
            # Return current node's tuple data to be accessed
            return current_node
        # Else if current_node is None (indicating the end of iteration), raise StopIteration exception
        else:
            raise StopIteration
        
    # Get all items function - Done by Edward
    @property
    def items(self):
        """
        The items function returns all objects in the Deque as an array.
        
        :param self: Refer to the instance of the class
        :return: An array containing all objects in the Deque
        """
        # Initialize list
        all_objects = {}
        # Iterate and add to list
        for node in self:
            data = node.data
            all_objects[data[0][0]] = (data[0][1],data[1])
        # Return list of all node data
        return all_objects
    
    @property
    def is_empty(self):
        """
        The is_empty function checks to see if the length of the sorted list is 0.

        :param self: Refer to the instance of the class
        :return: True if the sorted list is empty and false otherwise
        """
        return self._length == 0
        
    # Format and print sorted list items - Done by Ashwin
    def print_sorted(self): 
        """
        The print_sorted function will print the statements in sorted order.
        The output is a string with each value's groupings separated by new  lines.
        Each grouping starts with a header line containing the value, followed by 
        the statements that have that value.
        
        :param self: Refer to the instance of the class
        :return: A string that contains all the statements,
        """
        # Initialize a list to store the lines
        output_lines = [] 
        # Current value set to None
        current_value = None
        # Flag to indicate if current_value has been set
        is_current_value_set = False
        # For each assignment statement
        for node in self:
            # Extract statement and value from the node data
            statement, value = node.data
            # Check if still in the same group, if new group,
            if current_value != value or not is_current_value_set:
                # And it is not the very first loop
                if current_value is not None:
                    # Add a new line to separate each value's groupings
                    output_lines.append("")  
                # Add the header
                output_lines.append(f"*** Statements with value=> {value}") 
                # Set current value to value
                current_value = value
                # Set flag
                is_current_value_set = True
            # Add the current statement
            output_lines.append(f'{statement[0]}={statement[1]}')
        # Join all the lines into a single string with newlines between them
        output_string = "\n".join(output_lines)
        # Return output string
        return output_string
        
    # Insert into sorted list - Done by Ashwin
    def insert(self, new_data):
        """
        The insert function inserts the new data into the sorted list and keeps a sorted order
        within its list, sorted by the evaluated value of the expression.
        
        :param self: Refer to the instance of the class
        :param new_data: Create a new node with the data
        :return: None
        """
        key, value = new_data[0][0], new_data[1]
        # Make new data a node
        new_node = Node(new_data)
        # Increment length by 1
        self._length += 1
        # Check if the key already exists, and replace it if found
        current = self.head_node
        while current:
            # If current key matches new key, replace old key and value
            if current.data[0][0] == key:
                current.data = new_data
                return
            # Point to next node
            current = current.next_node
        # If there is no head node, set head node to new node
        if self.head_node is None:
            self.head_node = new_node
            return
        # If new data's evaluated value is None, append to the end of the list
        if value is None:
            # Point to head node
            current = self.head_node
            # While next node exists, keep goign down the list to the end
            while current.next_node:
                # Point to next node
                current = current.next_node
            # Set last node's next node to the new node
            current.next_node = new_node
            return
        # Check if it is going to be the new head
        if self.head_node.data[1] is None or value >= self.head_node.data[1]:
            # Set new head node to new node
            new_node.next_node = self.head_node
            self.head_node = new_node
            return
        # Set left and right node for traversal
        left_node = self.head_node
        right_node = self.head_node.next_node
        # Iterate through nodes while it has not reached the end
        while right_node is not None:
            # Check if right node's evaluated value is None
            if right_node.data[1] is None:
                # If it is, append the new node at the end of the list
                left_node.next_node = new_node
                new_node.next_node = right_node
                return
            # If correct position of node has been found, insert between left and right node
            if value >= right_node.data[1]:
                left_node.next_node = new_node
                new_node.next_node = right_node
                return
            # Traverse to the next pair of nodes
            left_node = right_node
            right_node = right_node.next_node
        # If end of the list is reached, new node is appended to the end
        left_node.next_node = new_node

    # Clear sorted list - Done by Ashwin
    def clear(self):
        """
        The clear function resets the sorted list to an empty state.
        
        :param self: Refer to the instance of the class
        :return: Nothing
        """
        # Reset head node
        self.head_node = None
        # Reset current node
        self.current_node = None
        # Reset length to 0
        self._length = 0