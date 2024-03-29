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
    # Initialization
    def __init__(self, data):
        """
        The __init__ function is called when the class is instantiated.
        It initializes all of the attributes that are required for this class.
        
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
    
    # Less than operator overriding - Done by Ashwin
    def __lt__(self, other):
        """
        The __lt__ function is a special function that allows us to compare two objects of the same class.
        The __lt__ function returns True if the first object is less than the second object
        and we compare nodes based on their value part of their tuple data attribute.
        
        :param self: Refer to the instance of the class
        :param other: Compare the two values
        :return: A boolean value
        """
        # Comparison based on the value part of the tuple (self.data[1])
        return self.data[1] < other.data[1]