# =================================================================================================
# ST1507 DATA STRUCTURES AND ALGORITHM (AI) CA2 ASSIGNMENT: ASSIGNMENT STATEMENT EVALUATOR & SORTER
# NAME: EDWARD TAN YUAN CHONG; ASHWIN RAJ
# CLASS: DAAA/FT/2B/04
# ADM NO: 2214407; 2239716
# =================================================================================================
# FILENAME: Stack.py
# =================================================================================================
'''
Description:
This is the Main file which handles the main application, inclusive of the printing of the banner, handling user choices for the menu of the application,
and running the Class methods to perform the menu option's functions.
'''
# Stack Class
class Stack:
    def __init__(self):
        # Use a list to store stack items
        self.items = []  

    def __len__(self):
        # Length of the stack is the length of the list
        return len(self.items)  

    def push(self, data):
        # Add an item to the end of the list
        self.items.append(data)  

    def pop(self):
        # Remove and return the last item of the list
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items.pop() 

    def is_empty(self):
        # Return boolean on whether list is empty
        return len(self.items) == 0 

