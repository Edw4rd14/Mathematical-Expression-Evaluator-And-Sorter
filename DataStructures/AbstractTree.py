# =================================================================================================
# ST1507 DATA STRUCTURES AND ALGORITHM (AI) CA2 ASSIGNMENT: ASSIGNMENT STATEMENT EVALUATOR & SORTER
# NAME: EDWARD TAN YUAN CHONG; ASHWIN RAJ
# CLASS: DAAA/FT/2B/04
# ADM NO: 2214407; 2239716
# =================================================================================================
# FILENAME: AbstractTree.py
# =================================================================================================

# Import Modules
from abc import ABC, abstractmethod

# AbstractTree class
class AbstractTree(ABC):
    @abstractmethod
    def __init__(self, root_object):
        """
        The __init__ function is called when the class is instantiated.
        It initializes all of the attributes that are required for this class.
        
        :param self: Refer to the instance of the class
        :param root_object: Set the root object of the tree
        :return: Nothing
        """
        pass

    @property
    @abstractmethod
    def right_tree(self):
        """
        The right_tree function returns the right subtree of a node.
        This is an abstract method that needs to be implemented by subclasses.
        
        :param self: Refer to the instance of the class
        :return: The right subtree of the tree
        """
        pass

    @right_tree.setter
    @abstractmethod
    def right_tree(self, value):
        """
        This right_tree function sets the value of the right tree to the given value.
        This is an abstract method that needs to be implemented by subclasses.
        
        :param self: Refer to the instance of the class
        :param value: Value to be inserted into the right tree
        """
        pass

    @property
    @abstractmethod
    def left_tree(self):
        """
        The left_tree function returns the left subtree of a node.
        This is an abstract method that needs to be implemented by subclasses.
        
        :param self: Refer to the instance of the class
        :return: The left subtree of the tree
        """
        pass

    @left_tree.setter
    @abstractmethod
    def left_tree(self, value):
        """
        This left_tree function sets the value of the left tree to the given value.
        This is an abstract method that needs to be implemented by subclasses.
        
        :param self: Refer to the instance of the class
        :param value: Value to be inserted into the left tree
        """
        pass

    @abstractmethod
    def insert_left(self, new_node):
        """
        The insert_left function inserts a new sub-tree as the left child of the current root.
        If there is already a left child, it will be pushed down one level in the tree to become
        the left child of that node.
        This is an abstract method that needs to be implemented by subclasses.
        
        :param self: Refer to the instance of the class
        :param new_node: New_node to be inserted
        :return: Nothing
        """
        pass

    @abstractmethod
    def insert_right(self, new_node):
        """
        The insert_right function inserts a new sub-tree as the right child of the current root.
        If there is already a right child, it will be pushed down one level in the tree to become
        the right child of that node. This is similar to the insert_left function.
        This is an abstract method that needs to be implemented by subclasses.
        
        :param self: Refer to the instance of the class
        :param new_node: New node to be inserted
        :return: Nothing
        """
        pass

    @property
    @abstractmethod
    def root_value(self):
        """
        The root_value function returns the value of the root node.
        This is an abstract method that needs to be implemented by subclasses.
        
        :param self: Refer to the instance of the class
        :return: The root value
        """
        pass

    @root_value.setter
    @abstractmethod
    def root_value(self, value):
        """
        The root_value setter function is used to set the root value.
        This is an abstract method that needs to be implemented by subclasses.
        
        :param self: Refer to the instance of the class
        :param value: Value to be set as the root value
        """
        pass
