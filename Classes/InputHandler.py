# =================================================================================================
# ST1507 DATA STRUCTURES AND ALGORITHM (AI) CA2 ASSIGNMENT: ASSIGNMENT STATEMENT EVALUATOR & SORTER
# NAME: EDWARD TAN YUAN CHONG; ASHWIN RAJ
# CLASS: DAAA/FT/2B/04
# ADM NO: 2214407; 2239716
# =================================================================================================
# FILENAME: InputHandler.py
# =================================================================================================

# InputHandler class
class InputHandler:
    # Initialization
    def __init__(self):
        """
        The __init__ function is called when the class is instantiated.
        It initializes all of the attributes that are required for this class.
        
        :param self: Refer to the instance of the class
        :return: Nothing
        """
        # Error message
        self.err_msg = 'Please try again or CRTL + C to return back to main menu.\n'

    # Format error - Done by Edward
    def format_error(self, error, menu, var=""):
        """
        The format_error function is used to format error messages for the user.
        
        :param self: Refer to the instance of the class
        :param error: Error message to be displayed
        :param menu: Boolean on whether to include "Returning back to main menu..."
        :param var: Specify the variable name in the error message
        :return: Error message string formatted
        """
        # Return formatted error message
        return f"\nInvalid format{' for variable ' + var if var else ''}! {error}. {self.err_msg if menu else ''}"

    # Prompt polar question (yes/no) - Done by Edward
    def prompt_polar_question(self,question:str)->bool:
        """
        The prompt_polar_question function prompts the user with a question that requires a Yes or No answer.
        The function will loop until it receives either Y (Yes) or N (No). If the user inputs anything other than Y or N,
        the function will print an error message and prompt again. The function returns True if the input is Y, and False if 
        the input is N.
        
        :param self: Refer to the instance of the class
        :param question:str: Pass the question to be asked to the user
        :return: A boolean value
        """
        # While loop
        while True:
            # Get user input on overwriting
            user_input = input(question)
            # If user inputs No, return False
            if user_input.lower() == 'n':
                return False
            # Else if invalid input, not N or Y, print error and loop again
            elif user_input.lower() != 'y':
                print("\nInvalid input! Please enter only Y (Yes) or N (No).", self.err_msg)
            # Else input is Y, return True
            else:
                return True
