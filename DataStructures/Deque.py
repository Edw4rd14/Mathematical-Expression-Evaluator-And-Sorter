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
        # Initialize head variable
        self.head = None 
        # Initialize tail variable
        self.tail = None
        # Initialize current variable
        self.current = None
        # Initialize length variable to 0 
        self.length = 0 

    def __len__(self):
        # Return length
        return self.length

    @property
    def is_empty(self):
        # Return boolean of length == 0
        return self.length == 0

    def add_head(self, data):
        # Create new node of data
        new_node = Node(data)

        # Check for duplicates and replace if found
        current_node = self.head
        while current_node:
            if current_node.data[0] == data[0]:
                # Replace the existing data
                current_node.data = data  
                return 
            current_node = current_node.nextNode

        # If head is None or no duplicates found, add a new node
        if not self.head:
            # Set head, tail, and current to new node
            self.head = self.tail = self.current = new_node
        # Else, Deque is not empty
        else:
            # Set new node's next node to current head
            new_node.nextNode = self.head
            # Set current head's previous node to new node
            self.head.prevNode = new_node
            # Set new head as new node
            self.head = new_node
            # Set current as new head
            self.current = self.head
        # Increment length by 1
        self.length += 1

    def add_tail(self, data):
        # Create new node of data
        new_node = Node(data)

        # Check for duplicates and replace if found
        current_node = self.head
        while current_node:
            if current_node.data[0] == data[0]: 
                current_node.data = data 
                return 
            current_node = current_node.nextNode

        # If head is None or no duplicates found, add a new node
        if not self.head:
            # Set head, tail, and current to new node
            self.head = self.tail = self.current = new_node
        # Else, Deque is not empty
        else:
            # Set new node's previous node to current tail
            new_node.prevNode = self.tail
            # Set current tail's next node to new node
            self.tail.nextNode = new_node
            # Set new tail as new node
            self.tail = new_node
            # Set current to new tail
            self.current = self.tail
        # Increment length by 1
        self.length += 1

    def remove_head(self):
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
                self.head = self.head.nextNode
                # Set new head's previous node to None as it is the new head
                self.head.prevNode = None
            # Decrement length by 1
            self.length -= 1
            # Return removed item
            return removed_item
        # Else raise error
        else:
            raise IndexError("Deque is empty")

    def remove_tail(self):
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
                self.tail = self.tail.prevNode
                # Set new tail's next node to None as it is the new tail
                self.tail.nextNode = None
            # Decrement length by 1
            self.length -= 1
            # Return removed item
            return removed_item
        # Else raise error
        else:
            raise IndexError("Deque is empty")
    
    def remove_current(self):
        if self.current is None:
            raise IndexError("No current item to remove")

        removed_data = self.current.data

        if self.current.prev:
            self.current.prev.nextNode = self.current.nextNode
        else:
            # Current is at head
            self.head = self.current.nextNode

        if self.current.nextNode:
            self.current.nextNode.prevNode = self.current.prev
        else:
            # Current is at tail
            self.tail = self.current.prev

        if self.current.nextNode:
            self.current = self.current.nextNode
        elif self.current.prev:
            self.current = self.current.prev
        else:
            self.current = None

        self.length -= 1
        return removed_data
        
    def go_back(self):
        # If current node and previous node exists
        if self.current and self.current.prevNode:
            # Set current node to previous node
            self.current = self.current.prevNode
            # Return current node (the previous node), effectively going backwards
            return self.current.data
        # Else return error message
        else:
            return "No previous item."

    def go_forward(self):
        # If current node and next node exists
        if self.current and self.current.nextNode:
            # Set current node to next node
            self.current = self.current.nextNode
            # Return current node (the next node), effectively going forward
            return self.current.data
        # Else return error message
        else:
            return "No next item."

    def clear(self):
        # Set head and tail to None
        self.head = self.tail = None
        # Set length to 0 (reset Deque)
        self.length = 0

    def contains(self, item):
        current_node = self.head
        while current_node:
            if current_node.data[0] == item[0]:
                return True
            current_node = current_node.nextNode
        return False