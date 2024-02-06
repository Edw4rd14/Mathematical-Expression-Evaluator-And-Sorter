# =================================================================================================
# ST1507 DATA STRUCTURES AND ALGORITHM (AI) CA2 ASSIGNMENT: ASSIGNMENT STATEMENT EVALUATOR & SORTER
# NAME: EDWARD TAN YUAN CHONG; ASHWIN RAJ
# CLASS: DAAA/FT/2B/04
# ADM NO: 2214407; 2239716
# =================================================================================================
# FILENAME: Main.py
# =================================================================================================

# Import Classes
from Classes.AssignmentStatement import AssignmentStatement

# Main class
class Main:
    # Initialization
    def __init__(self):
        """
        The __init__ function initializes the Main class.
        
        :param self: Refer to the current instance of a class
        :return: Nothing
        """
        # Initialize AssignmentStatement Class
        self.assignment_statement = AssignmentStatement()
        # Banner 
        self._banner=['*'*59, "* ST1507 DSAA: Evaluating & Sorting Assignment Statements *", "*" + "-"*57 + "*", "*" + " "*57 + "*", "*  - Done by: Edward Tan (2214407) & Ashwin Raj (2239716) *", "*  - Class DAAA/2B/04" + " " * 37 + "*"]
        self.__banner_order = [0,1,2,3,4,5,3,0]
        # Menu options
        self.choice = None
        self._menu_options = ['Add/Modify assignment statement', 'Display current assignment statements', 'Evaluate a single variable', 'Read assignment statements from file', 'Sort assignment statements', 'Batch process assignment statement from files', 'Manage assignment statement history', 'Remove all statements', 'Display statistics','Exit']
        self.__options = {
            1: self.assignment_statement.add_modify_statement,
            2: self.assignment_statement.display_statements,
            3: self.assignment_statement.evaluate_single_variable,
            4: self.assignment_statement.read_statements_from_file,
            5: self.assignment_statement.sort_statements,
            6: self.assignment_statement.batch_process,
            7: self.assignment_statement.manage_history,
            8: self.assignment_statement.remove_all_statements,
            9: self.assignment_statement.display_statistics
        }
        # Exit message
        self._exit = "\nBye, thanks for using ST1507 DSAA: Assignment Statement Evaluator & Sorter"

    # Start banner - Done by Edward
    def _start_banner(self):
        """
        The _start_banner function prints the banner of the application in the specified order.
            
        :param self: Refer to the instance of the class
        :return: Nothing
        """
        # Print banner
        for order in self.__banner_order:
            print(self._banner[order])
        print("\n")

    # Menu prompt - Done by Edward
    def _menu(self):
        """
        The _menu function prints the menu options and prompts the user for a choice.
        The choice is then stored in self.choice to handle user's menu option.
        
        :param self: Refer to the instance of the class
        :return: Nothing
        """
        # Print menu
        print("Please select a choice ('1','2','3','4','5','6','7','8','9','10'):")
        for i in range(len(self._menu_options)):
            print(f"    {i+1}. {self._menu_options[i]}")
        # User input for menu option
        self.choice = int(input("Enter choice: "))

    # Run main application - Done by Edward
    def start(self):
        """
        The start function is the main function that runs the application.
        It starts by printing a banner, then prompts users for their choice of menu option.
        If user options are between 1 and 10, it will run the menu option selected by user.
        Else if choice is 10 (exit application), it will exit out of program with an exit message.
        Else print error message (user option is not valid).  
        
        :param self: Refer to the instance of the class
        :return: Nothing
        """
        # Start banner
        self._start_banner()
        # While loop for menu
        while True:
            try:
                # Prompt users for choice
                self._menu()
                # If user options are between 1 and 10
                if self.choice in range(1,10):
                    try:
                        # Get menu option function
                        option = self.__options.get(self.choice)
                        # Run menu option selected by user
                        option()
                    # Handle Keyboard Interrupt (CRTL + C)
                    except KeyboardInterrupt:
                        print("\nReturning back to main menu...")
                    input("\nPlease enter key to continue...\n")
                # Else if choice is 10 (exit application)
                elif self.choice == 10:
                    print(f"{self._exit}")
                    break
                # Else print error message (user option is not valid)
                else:
                    print("\nOnly options between 1 and 10 are available. Please try again.\n")
            # Handle ValueError (user choice is not integer)
            except ValueError:
                print("\nInput must be an integer. Please try again.\n")
            # Handle Keyboard Interrupt (CRTL + C)
            except KeyboardInterrupt:
                print(f"\n{self._exit}")
                break
            # # Handle any other errors (as a precaution, and not leak error messages)
            # except Exception:
            #     print("\nAn error has occurred with the application. Try restarting the application.\n")
        # Update history
        self.assignment_statement.history.update_history()

# Instantiate Main class
main = Main()

# Check that script is being run directly and not being imported
if __name__ == '__main__':
    # Run main application
    main.start()