# =================================================================================================
# ST1507 DATA STRUCTURES AND ALGORITHM (AI) CA2 ASSIGNMENT: ASSIGNMENT STATEMENT EVALUATOR & SORTER
# NAME: EDWARD TAN YUAN CHONG; ASHWIN RAJ
# CLASS: DAAA/FT/2B/04
# ADM NO: 2214407; 2239716
# =================================================================================================
# FILENAME: BinaryTree.py
# =================================================================================================
'''
Description:
This is the Main file which handles the main application, inclusive of the printing of the banner, handling user choices for the menu of the application,
and running the Class methods to perform the menu option's functions.
'''

# BinaryTree class
class BinaryTree:
    # Initialization
    def __init__(self, root_object):
        # Initialize key / root object
        self.key = root_object
        # Initialize left and right child
        self.left_child = None
        self.right_child = None

    # Insert left
    def insert_left(self, new_node):
        # If left child is empty
        if self.left_child is None:
            # Create new BinaryTree of new node in left child
            self.left_child = BinaryTree(new_node)
        # Else if left child exists
        else:
            # Create a new BinaryTree node for the new node
            t = BinaryTree(new_node)
            # Set the current left child as the left child of the new node
            t.left_child = self.left_child
            # Update the left child of the current node to be the new node
            self.left_child = t


    # Insert right
    def insert_right(self, new_node):
        # If right child is empty
        if self.right_child is None:
            # Create a new BinaryTree of new node in right child
            self.right_child = BinaryTree(new_node)
        # Else if right child exists
        else:
            # Create a new BinaryTree node for the new node
            t = BinaryTree(new_node)
            # Set the current right child as the right child of the new node
            t.right_child = self.right_child
            # Update the right child of the current node to be the new node
            self.right_child = t

    # Get the right child of the current node
    def get_right_child(self):
        return self.right_child

    # Get the left child of the current node
    def get_left_child(self):
        return self.left_child

    # Set the value of the root node
    def set_root_value(self, obj):
        self.key = obj

    # Get the value of the root node
    def get_root_value(self):
        return self.key
