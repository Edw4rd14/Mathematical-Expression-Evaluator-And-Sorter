# =================================================================================================
# ST1507 DATA STRUCTURES AND ALGORITHM (AI) CA2 ASSIGNMENT: ASSIGNMENT STATEMENT EVALUATOR & SORTER
# NAME: EDWARD TAN YUAN CHONG; ASHWIN RAJ
# CLASS: DAAA/FT/2B/04
# ADM NO: 2214407; 2239716
# =================================================================================================
# FILENAME: BinaryTree.py
# =================================================================================================
# Import Data Structures
from DataStructures.AbstractTree import AbstractTree

# BinaryTree class
class BinaryTree(AbstractTree):
    # Initialization
    def __init__(self, root_object):
        """
        The __init__ function is called when the class is instantiated.
        It initializes all of the attributes that are required for this class.
        
        :param self: Refer to the instance of the class
        :param root_object: Root of the current binary tree
        :return: Nothing
        """
        # Initialize key / root object
        self._key = root_object
        # Initialize left and right tree
        self._left_tree = None
        self._right_tree = None

    # Get the right tree of the current node - Done by Edward
    @property
    def right_tree(self):
        """
        The right_tree function returns the right subtree of the current root.
        
        :param self: Refer to the instance of the class
        :return: The right tree of the node
        """
        return self._right_tree
    
    # Set the right tree of the current node - Done by Edward
    @right_tree.setter
    def right_tree(self, value):
        """
        The right_tree function is a setter function that sets the right_tree attribute of an instance of the BinaryTree class.
        The right_tree function takes in one parameter, value, which is assigned to self._right_tree.
        
        :param self: Refer to the instance of the class
        :param value: Value to be set to the right tree
        """
        self._right_tree = value

    # Get the left tree of the current node - Done by Edward
    @property
    def left_tree(self):
        """
        The left_tree function returns the left tree of the current root.
        
        :param self: Refer to the instance of the class
        :return: The left subtree of a tree
        """
        return self._left_tree    
    
    # Set the left tree of the current node - Done by Edward
    @left_tree.setter
    def left_tree(self, value):
        """
        The left_tree function is also a setter function that sets the left_tree attribute of an instance of the BinaryTree class, similar
        to the right_tree setter function.
        The left_tree function takes in one parameter, value, which is assigned to self._left_tree.
            
        :param self: Refer to the instance of the class
        :param value: Value to be set to the left tree
        """
        self._left_tree = value

    # Insert left - Done by Edward
    def insert_left(self, new_node):
        """
        The insert_left function inserts a new sub-tree as the left child of the current root.
        If there is already a left child, it will be pushed down one level in the tree to become
        the left child of that node.
        
        :param self: Refer to the instance of the class
        :param new_node: New_node to be inserted
        :return: Nothing
        """
        # If left tree is empty
        if self._left_tree is None:
            # Create new BinaryTree of new node in left tree
            self.left_tree = BinaryTree(new_node)
        # Else if left tree exists
        else:
            # Create a new BinaryTree node for the new node
            t = BinaryTree(new_node)
            # Set the current left tree as the left tree of the new node
            t.left_tree = self._left_tree
            # Update the left tree of the current node to be the new node
            self.left_tree = t

    # Insert right - Done by Edward
    def insert_right(self, new_node):
        """
        The insert_right function inserts a new sub-tree as the right child of the current root.
        If there is already a right child, it will be pushed down one level in the tree to become
        the right child of that node. This is similar to the insert_left function.
        
        :param self: Refer to the instance of the class
        :param new_node: New node to be inserted
        :return: Nothing
        """
        # If right tree is empty
        if self._right_tree is None:
            # Create a new BinaryTree of new node in right tree
            self.right_tree = BinaryTree(new_node)
        # Else if right tree exists
        else:
            # Create a new BinaryTree node for the new node
            t = BinaryTree(new_node)
            # Set the current right tree as the right tree of the new node
            t.right_tree = self._right_tree
            # Update the right tree of the current node to be the new node
            self.right_tree = t
    
    # Get the value of the root node - Done by Edward
    @property
    def root_value(self):
        """
        The root_value function returns the value of the root node.
        
        :param self: Refer to the instance of the class
        :return: The root value
        """
        return self._key

    # Set the value of the root node - Done by Edward
    @root_value.setter
    def root_value(self, value):
        """
        The root_value setter function is used to set the root value.
        
        :param self: Refer to the instance of the class
        :param value: Value to be set as the root value
        """
        self._key = value

