# =================================================================================================
# ST1507 DATA STRUCTURES AND ALGORITHM (AI) CA2 ASSIGNMENT: ASSIGNMENT STATEMENT EVALUATOR & SORTER
# NAME: EDWARD TAN YUAN CHONG; ASHWIN RAJ
# CLASS: DAAA/FT/2B/04
# ADM NO: 2214407; 2239716
# =================================================================================================
# FILENAME: Stack.py
# =================================================================================================

# Stack Class
class Stack:
    # Initialization
    def __init__(self):
        """
        The __init__ function is called when the class is instantiated.
        It initializes all of the attributes that are required for this class.
        
        :param self: Refer to the instance of the class
        :return: Nothing
        """
        # Use a list to store stack items
        self._items = []  

    # Length of stack - Done by Ashwin
    def __len__(self):
        """
        This function returns the length of the stack with Python's built-in len() function
        
        :param self: Refer to the instance of the class
        :return: The length of the stack
        """
        # Length of the stack is the length of the list
        return len(self._items)  

    # Push to stack - Done by Ashwin
    def push(self, data):
        """
        The push function adds an item to the end of the stack.
        
        :param self: Refer to the instance of the class
        :param data: Add an item to the end of the stack
        :return: The length of the stack
        """
        # Add an item to the end of the list
        self._items.append(data)  

    # Pop from stack - Done by Ashwin
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
    
    # Get all items in stack - Done by Ashwin
    @property
    def items(self):
        """
        The items function returns a list of all the items in the stack.
        
        :param self: Refer to the instance of the class
        :return: The items of the stack
        """
        return self._items

    # Check if stack is empty - Done by Ashwin
    @property
    def is_empty(self):
        """
        The is_empty function returns a boolean value on whether the stack is empty by checking if the length of items in the stack is equal to 0.
        
        :param self: Refer to the instance of the class
        :return: A boolean on whether the stack is empty
        """
        # Return boolean on whether list is empty
        return len(self._items) == 0