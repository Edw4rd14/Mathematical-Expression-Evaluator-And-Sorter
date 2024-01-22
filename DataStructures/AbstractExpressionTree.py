# =================================================================================================
# ST1507 DATA STRUCTURES AND ALGORITHM (AI) CA2 ASSIGNMENT: ASSIGNMENT STATEMENT EVALUATOR & SORTER
# NAME: EDWARD TAN YUAN CHONG; ASHWIN RAJ
# CLASS: DAAA/FT/2B/04
# ADM NO: 2214407; 2239716
# =================================================================================================
# FILENAME: AbstractExpressionTree.py
# =================================================================================================

# Import modules
from abc import ABC, abstractmethod

# Abstract Expression Tree Class
class AbstractExpressionTree(ABC):
    @abstractmethod
    def __init__(self, expression):
        """
        Initializes the expression tree with a given expression.
        """
        self.expression = expression

    @abstractmethod
    def build_parse_tree(self, expression):
        """
        Builds the parse tree from the expression.
        """
        pass

    @abstractmethod
    def evaluate(self):
        """
        Evaluates the parse tree and returns the result.
        """
        pass

    @abstractmethod
    def print_in_order(self):
        """
        Prints the expression tree in in-order notation.
        """
        pass