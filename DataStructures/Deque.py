# =================================================================================================
# ST1507 DATA STRUCTURES AND ALGORITHM (AI) CA2 ASSIGNMENT: ASSIGNMENT STATEMENT EVALUATOR & SORTER
# NAME: EDWARD TAN YUAN CHONG; ASHWIN RAJ
# CLASS: DAAA/FT/2B/04
# ADM NO: 2214407; 2239716
# =================================================================================================
# FILENAME: Deque.py
# =================================================================================================

# Import Data Structure
from DataStructures.Node import Node

# Deque class
class Deque:
    # Initialization
    def __init__(self):
        """
        The __init__ function is called when the class is instantiated.
        It initializes all of the attributes that are required for this class.
        
        :param self: Refer to the instance of the class
        :return: Nothing
        """
        # Initialize head variable
        self.head = None 
        # Initialize tail variable
        self.tail = None
        # Initialize current variable
        self.current = None
        # Initialize length variable to 0 
        self.length = 0 

    # Override length len() function - Done by Edward
    def __len__(self):
        """
        This function returns the length of the Deque with Python's built-in len() function
        
        :param self: Refer to the instance of the class
        :return: The length of the Deque
        """
        # Return length
        return self.length
    
    # Get item function - Done by Edward
    def __getitem__(self, variable):
        """
        The __getitem__ function is a special function that overrides the get item built-in function, list[item].
        
        :param self: Refer to the instance of the class
        :param variable: Variable to be referred to
        :return: A tuple
        """
        # Get all items
        all_items = self.items
        # Iterate through each item and check if variables matches, return item
        for item in all_items:
            if item[0] == variable:
                return item
            
    # Contains function - Done by Edward
    def __contains__(self, item):
        """
        The __contains__ function takes in a tuple of the form (key, value) and returns True if the key is present in the Deque.
        If it is not present, then it returns False.
        
        :param self: Refer to the instance of the class
        :param item: Item to be checked on whether it is present in the Deque
        :return: True if the item is in the Deque, and false otherwise
        """
        # Set current node
        current_node = self.head
        # Loop through each current node that is not None
        while current_node:
            # If first item of current node data matches first item (variable)
            if current_node.data[0] == item[0]:
                # Return true
                return True
            # Point to next node
            current_node = current_node.next_node
        # If item has not been found, return false
        return False
        
    # Getter for current deque item - Done by Edward
    def get_current(self):
        return self.current.data

    # Is empty function - Done by Edward
    @property
    def is_empty(self):
        """
        The is_empty function returns a boolean value of True if the length of the Deque is 0, and False otherwise.
        
        :param self: Refer to the instance of the class
        :return: A boolean value of length == 0
        """
        # Return boolean of length == 0
        return self.length == 0

    # Add head function - Done by Edward
    def add_head(self, data):
        """
        The add_head function adds a new node to the head of the Deque.
        If there is already a node with that data, it replaces it.
            
        :param self: Refer to the instance of the class
        :param data: Data to be stored
        :return: Nothing
        """
        # Create new node of data
        new_node = Node(data)
        # Check for duplicates and replace if found
        current_node = self.head
        while current_node:
            if current_node.data[0] == data[0]:
                # Replace the existing data
                current_node.data = data  
                return 
            current_node = current_node.next_node
        # If head is None or no duplicates found, add a new node
        if not self.head:
            # Set head, tail, and current to new node
            self.head = self.tail = self.current = new_node
        # Else, Deque is not empty
        else:
            # Set new node's next node to current head
            new_node.next_node = self.head
            # Set current head's previous node to new node
            self.head.prev_node = new_node
            # Set new head as new node
            self.head = new_node
            # Set current as new head
            self.current = self.head
        # Increment length by 1
        self.length += 1

    # Add tail function - Done by Edward
    def add_tail(self, data):
        """
        The add_tail function adds a new node to the end of the Deque.
        If there is already a node with that key, replace it with the new data.
        
        :param self: Refer to the instance of the class
        :param data: Data to be stored
        :return: Nothing
        """
        # Create new node of data
        new_node = Node(data)
        # Check for duplicates and replace if found
        current_node = self.head
        while current_node:
            if current_node.data[0] == data[0]: 
                current_node.data = data 
                return 
            current_node = current_node.next_node
        # If head is None or no duplicates found, add a new node
        if not self.head:
            # Set head, tail, and current to new node
            self.head = self.tail = self.current = new_node
        # Else, Deque is not empty
        else:
            # Set new node's previous node to current tail
            new_node.prev_node = self.tail
            # Set current tail's next node to new node
            self.tail.next_node = new_node
            # Set new tail as new node
            self.tail = new_node
            # Set current to new tail
            self.current = self.tail
        # Increment length by 1
        self.length += 1

    # Remove head function - Done by Edward
    def remove_head(self):
        """
        The remove_head function removes the head of the Deque and returns it.
        If there is only one item in the Deque, then both head and tail are set to None.
        Else if there is more than one item in the Deque, then a new head is set to be 
        following node of current head, and its previous node pointer is set to None as it 
        will now be at front of list.
        
        :param self: Refer to the instance of the class
        :return: The data of the head node
        """
        # If Deque is not empty
        if not self.is_empty:
            # Store item to be removed, which is data at head
            removed_item = self.head.data
            # If Deque only has 1 item, and it is being removed
            if self.length == 1:
                # Set head and tail to None as Deque will be empty
                self.head = self.tail = None
            # Else Deque has more than 1 item
            else:
                # Set new head to the node following the current head
                self.head = self.head.next_node
                # Set new head's previous node to None as it is the new head
                self.head.prev_node = None
            # Decrement length by 1
            self.length -= 1
            # Return removed item
            return removed_item
        # Else raise error
        else:
            raise IndexError("Deque is empty")

    def remove_tail(self):
        """
        The remove_tail function removes the tail node from the Deque.
        It returns the data of that removed node.
        If there is only one item in the Deque, it will remove that item and set head and tail to None.
        
        :param self: Refer to the instance of the class
        :return: The removed item
        """
        # If Deque is not empty
        if not self.is_empty:
            # Store item to be removed, which is data at tail
            removed_item = self.tail.data
            # If Deque only has 1 item, and it is being removed
            if self.length == 1:
                # Set head and tail to None as Deque will be empty
                self.head = self.tail = None
            # Else Deque has more than 1 item
            else:
                # Set new tail to the node to the tail's previous node
                self.tail = self.tail.prev_node
                # Set new tail's next node to None as it is the new tail
                self.tail.next_node = None
            # Decrement length by 1
            self.length -= 1
            # Return removed item
            return removed_item
        # Else raise error
        else:
            raise IndexError("Deque is empty")

    # Go back function - Done by Edward
    def go_back(self):
        """
        The go_back function allows the user to go back one node in the Deque.
        If there is no previous node, it returns an error message.
        This allows for traversal backwards in the Deque.
        
        :param self: Refer to the instance of the class
        :return: The previous node
        """
        # If current node and previous node exists
        if self.current and self.current.prev_node:
            # Set current node to previous node
            self.current = self.current.prev_node
            # Return current node (the previous node), effectively going backwards
            return self.current.data
        # Else return error message
        else:
            return "No previous item."
        
    # Go forward function - Done by Edward
    def go_forward(self):
        """
        The go_forward function moves the current node to the next node in the Deque.
        If there is no next node, it returns an error message.
        This allows for forward traversal in the Deque.
        
        :param self: Refer to the instance of the class
        :return: The data of the next node
        """
        # If current node and next node exists
        if self.current and self.current.next_node:
            # Set current node to next node
            self.current = self.current.next_node
            # Return current node (the next node), effectively going forward
            return self.current.data
        # Else return error message
        else:
            return "No next item."

    # Clear function - Done by Edward
    def clear(self):
        """
        The __clear function sets the head, tail and current to None, and resets the length of the Deque to 0.
        
        :param self: Refer to the instance of the class
        :return: Nothing
        """
        # Set head and tail to None
        self.head = self.tail = self.current = None
        # Set length to 0 
        self.length = 0
    
    # Reset to head function - Done by Edward
    def reset_to_head(self):
        """
        The reset_to_head function resets the current pointer back to the head of the Deque.
        If the Deque is empty, it raises an IndexError.

        :param self: Refer to the instance of the class
        :return: Nothing
        """
        # If deque is empty
        if self.is_empty:
            raise IndexError("Deque is empty")
        # Set current to head
        self.current = self.head

    # Get all items function - Done by Edward
    @property
    def items(self):
        """
        The items function returns all objects in the Deque as an array.
        
        :param self: Refer to the instance of the class
        :return: An array containing all objects in the Deque
        """
        # Initialize list
        all_objects = []
        # Set current node to head node
        current_node = self.head
        # Iterate through all possible nodes
        while current_node:
            # Append current node data to list
            all_objects.append(current_node.data)
            # Point to next node
            current_node = current_node.next_node
        # Return list of all node data
        return all_objects
    
    # Get item function - Done by Edward
    def __getitem__(self, variable):
        """
        The __getitem__ function is a special function that overrides the get item built-in function, list[item].
        
        :param self: Refer to the instance of the class
        :param variable: Variable to be referred to
        :return: A tuple
        """
        # Get all items
        all_items = self.items
        # Iterate through each item and check if variables matches, return item
        for item in all_items:
            if item[0] == variable:
                return item
        