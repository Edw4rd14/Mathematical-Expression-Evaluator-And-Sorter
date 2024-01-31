# =================================================================================================
# ST1507 DATA STRUCTURES AND ALGORITHM (AI) CA2 ASSIGNMENT: ASSIGNMENT STATEMENT EVALUATOR & SORTER
# NAME: EDWARD TAN YUAN CHONG; ASHWIN RAJ
# CLASS: DAAA/FT/2B/04
# ADM NO: 2214407; 2239716
# =================================================================================================
# FILENAME: Node.py
# =================================================================================================

# Node class
class Node:
    def __init__(self, data):
        """
        The __init__ function is a special function in Python classes. It is run as soon as an object of a class is instantiated. 
        The method __init__() is called automatically every time the class is being used to create a new object.
        
        :param self: Refer to the instance of the class
        :param data: Store the data in the node
        :return: Nothing
        """
        # Store data
        self.data = data
        # Pointer for next node
        self.next_node = None
        # Pointer for previous node
        self.prev_node = None
    
    def __lt__(self, other):
        """
        The __lt__ function is a special function that allows us to compare two objects of the same class.
        The __lt__ function returns True if the first object (self) is less than the second object (other) 
        and we compare nodes based on their value part of their tuple data attribute.
        
        :param self: Refer to the instance of the class
        :param other: Compare the two values
        :return: A boolean value
        """
        # Comparison based on the value part of the tuple (self.data[1])
        return self.data[1] < other.data[1]