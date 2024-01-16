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
        # Initialize left and right tree
        self.left_tree = None
        self.right_tree = None

    # Insert left
    def insert_left(self, new_node):
        # If left tree is empty
        if self.left_tree is None:
            # Create new BinaryTree of new node in left tree
            self.left_tree = BinaryTree(new_node)
        # Else if left tree exists
        else:
            # Create a new BinaryTree node for the new node
            t = BinaryTree(new_node)
            # Set the current left tree as the left tree of the new node
            t.left_tree = self.left_tree
            # Update the left tree of the current node to be the new node
            self.left_tree = t

    # Insert right
    def insert_right(self, new_node):
        # If right tree is empty
        if self.right_tree is None:
            # Create a new BinaryTree of new node in right tree
            self.right_tree = BinaryTree(new_node)
        # Else if right tree exists
        else:
            # Create a new BinaryTree node for the new node
            t = BinaryTree(new_node)
            # Set the current right tree as the right tree of the new node
            t.right_tree = self.right_tree
            # Update the right tree of the current node to be the new node
            self.right_tree = t

    # Get the right tree of the current node
    def get_right_tree(self):
        return self.right_tree

    # Get the left tree of the current node
    def get_left_tree(self):
        return self.left_tree

    # Set the value of the root node
    def set_root_value(self, obj):
        self.key = obj

    # Get the value of the root node
    def get_root_value(self):
        return self.key
