# =================================================================================================
# ST1507 DATA STRUCTURES AND ALGORITHM (AI) CA2 ASSIGNMENT: ASSIGNMENT STATEMENT EVALUATOR & SORTER
# NAME: EDWARD TAN YUAN CHONG; ASHWIN RAJ
# CLASS: DAAA/FT/2B/04
# ADM NO: 2214407; 2239716
# =================================================================================================
# FILENAME: Sorter.py
# =================================================================================================

# Import modules
from abc import ABC, abstractmethod

# Sorter class
class Sorter(ABC):
    @staticmethod
    @abstractmethod
    def sort(arr, reverse=False):
        """
        Sort the array and return the sorted array.
        This is an abstract method that needs to be implemented by subclasses.
        
        :param arr: The list to be sorted.
        :param reverse: If True, sort the list in descending order.
        :return: The sorted list.
        """
        pass