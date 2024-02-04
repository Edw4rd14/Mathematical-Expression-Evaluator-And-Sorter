# =================================================================================================
# ST1507 DATA STRUCTURES AND ALGORITHM (AI) CA2 ASSIGNMENT: ASSIGNMENT STATEMENT EVALUATOR & SORTER
# NAME: EDWARD TAN YUAN CHONG; ASHWIN RAJ
# CLASS: DAAA/FT/2B/04
# ADM NO: 2214407; 2239716
# =================================================================================================
# FILENAME: SortedList.py
# =================================================================================================

# Import data structures
from DataStructures.Node import Node

# SortedList class
class SortedList:
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
    
    def __len__(self): 
        """
        The __len__ function is a special function that returns the length of an object.
        It is called by Python's built-in len() function.
        This function returns the length of the sorted list
        
        :param self: Refer to the instance of the class
        :return: The length of the queue
        """
        # Return length
        return self._length

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

    def __next__(self):
        """
        The __next__ function is called by the Python interpreter to get each item from an iterator. 
        
        :param self: Refer to the instance of the class
        :return: The current node's tuple data
        """
        # If current_node exists (which means it is not the end of the iteration),
        if self.current_node:
            # Set data to be returned to current node's tuple data
            data = self.current_node.data
            # Set current node variable to next node for next iteration
            self.current_node = self.current_node.next_node
            # Return current node's tuple data to be accessed
            return data
        # Else if current_node is None (indicating the end of iteration), raise StopIteration exception
        else:
            raise StopIteration
        
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
        for node_data in self:
            # Extract statement and value from the node data
            statement, value = node_data
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
            output_lines.append(statement)
        # Join all the lines into a single string with newlines between them
        output_string = "\n".join(output_lines)
        # Return output string
        return output_string

    def __append_to_head(self, new_node): 
        """
        The __append_to_head function is a private function that appends a new node to the head of the sorted list.
        It does this by storing the old head node, setting the new head node to be the new_node parameter, 
        setting next_node of our newly set head_node (new_node) to the oldHeadNode and finally incrementing length by 1.
        
        :param self: Refer to the instance of the class
        :param new_node: Set the new head node
        :return: Nothing
        """
        # Store old head node
        oldHeadNode = self.head_node
        # Set new head node to new node
        self.head_node = new_node
        # Set the next node of the new head node to the old head node
        self.head_node.next_node = oldHeadNode
        # Increment length by 1
        self._length += 1

    def insert(self, new_data): 
        """
        The insert function takes in a new_data parameter, which is a tuple of the form (key, value).
        The function then creates a new node with this data. It then checks if the list is empty and inserts it as head node if so.
        If not, it checks whether or not the key of the new data is None; if so, it appends to end of list. If not, 
        it compares its key to that of head node's and inserts before or after accordingly.
        
        :param self: Refer to the instance of the class
        :param new_data: Insert a new node into the sortedlist
        :return: None
        """
        # Make new data a node
        new_node = Node(new_data)
        # Increment length by 1
        self._length += 1
        # If there is no head node (empty SortedList), set head node to new node
        if self.head_node is None: 
            self.head_node = new_node
            return
        # If new data's value is None, append to the end of the list
        if new_node.data[1] is None:
            current = self.head_node
            while current.next_node:
                current = current.next_node
            current.next_node = new_node
            return
        # Check if it is going to be new head
        if self.head_node.data[1] is None or new_node.data[1] > self.head_node.data[1]:
            self.__append_to_head(new_node)
            return
        # Set left and right node for traversal
        left_node = self.head_node
        right_node = self.head_node.next_node
        # Iterate through nodes while it has not reached the end
        while right_node is not None:
            # Check if right node's data is None
            if right_node.data[1] is None:
                # If it is, append the new node at the end of the list
                left_node.next_node = new_node
                new_node.next_node = right_node
                return
            # If correct position of node has been found, insert between left and right node
            if new_node.data[1] > right_node.data[1]:
                left_node.next_node = new_node 
                new_node.next_node = right_node
                return
            # Traverse to the next pair of nodes
            left_node = right_node
            right_node = right_node.next_node
        # If end of the list is reached, new node is appended to the end
        left_node.next_node = new_node

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