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
        # Initialize head node
        self.head_node = None
        # Initialize current node
        self.current_node = None
        # Initialize length
        self._length = 0 
    
    def __len__(self): 
        # Return length
        return self._length

    def __iter__(self):
        # When object is iterated, set current_node to head_node to start looping from the head
        self.current_node = self.head_node
        # Return self as iterator object to be looped
        return self

    def __next__(self):
        # If current_node exists (which means it is not the end of the iteration),
        if self.current_node:
            # Set data to be returned to current node's tuple data
            data = self.current_node.data
            # Set current node variable to next node for next iteration
            self.current_node = self.current_node.nextNode
            # Return current node's tuple data to be accessed
            return data
        # Else if current_node is None (indicating the end of iteration), raise StopIteration exception
        else:
            raise StopIteration
        
    def print_sorted(self): 
        # Initialize a list to store the lines
        output_lines = [] 
        # Current value set to None
        current_value = None
        # For each assignment statement
        for node_data in self:
            # Extract statement and value from the node data
            statement, value = node_data
            # Check if still in the same group, if new group,
            if current_value != value:
                # And it is not the very first loop
                if current_value is not None:
                    # Add a new line to separate each value's groupings
                    output_lines.append("")  
                # Add the header
                output_lines.append(f"*** Statements with value=> {value}") 
                # Set current value to value
                current_value = value
            # Add the current statement
            output_lines.append(statement)
        # Join all the lines into a single string with newlines between them
        output_string = "\n".join(output_lines)
        # Return output string
        return output_string

    def __append_to_head(self, new_node): 
        # Store old head node
        oldHeadNode = self.head_node
        # Set new head node to new node
        self.head_node = new_node
        # Set the next node of the new head node to the old head node
        self.head_node.nextNode = oldHeadNode
        # Increment length by 1
        self._length += 1

    def insert(self, new_data): 
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
            while current.nextNode:
                current = current.nextNode
            current.nextNode = new_node
            return
        # Check if it is going to be new head
        if new_node.data[1] > self.head_node.data[1]:
            self.__append_to_head(new_node)
            return
        # Set left and right node for traversal
        left_node = self.head_node
        right_node = self.head_node.nextNode
        # Iterate through nodes while it has not reached the end
        while right_node is not None:
            # If correct position of node has been found, insert between left and right node
            if new_node.data[1] > right_node.data[1]:
                left_node.nextNode = new_node 
                new_node.nextNode = right_node
                return
            # Traverse to the next pair of nodes
            left_node = right_node
            right_node = right_node.nextNode
        # If end of the list is reached, new node is appended to the end
        left_node.nextNode = new_node
