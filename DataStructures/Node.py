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
        # Store data
        self.data = data
        # Pointer for next node
        self.nextNode = None
        # Pointer for previous node
        self.prevNode = None
    
    def __lt__(self, other):
        # Comparison based on the value part of the tuple (self.data[1])
        return self.data[1] < other.data[1]