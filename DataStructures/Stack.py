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
        """
        The __init__ function is called when the class is instantiated. 
        It sets up the initial state of the object, which in this case means creating an empty list to store stack items.
        
        :param self: Refer to the instance of the class
        :return: Nothing
        """
        # Use a list to store stack items
        self._items = []  

    def __len__(self):
        """
        The __len__ function is a special function that returns the length of an object.
        In this case, it returns the length of our stack.
        
        :param self: Refer to the instance of the class
        :return: The length of the stack
        """
        # Length of the stack is the length of the list
        return len(self._items)  

    def push(self, data):
        """
        The push function adds an item to the end of the stack.
        
        :param self: Refer to the instance of the class
        :param data: Add an item to the end of the stack
        :return: The length of the stack
        """
        # Add an item to the end of the list
        self._items.append(data)  

    def pop(self):
        """
        The pop function removes and returns the last item of the stack.
        If there are no items in the stack, it raises an exception.
        
        :param self: Refer to the instance of the class
        :return: The last item of the stack
        """
        # Remove and return the last item of the list
        if self.is_empty:
            raise Exception("Stack is empty")
        return self._items.pop() 
    
    @property
    def items(self):
        """
        The items function returns a list of all the items in the stack.
        
        :param self: Refer to the instance of the class
        :return: The items of the stack
        """
        return self._items

    @property
    def is_empty(self):
        """
        The is_empty function returns a boolean value on whether the stack is empty.
        It does this by checking if the length of items in the stack is equal to 0.
        
        :param self: Refer to the instance of the class
        :return: A boolean on whether the stack is empty

        """
        # Return boolean on whether list is empty
        return len(self._items) == 0