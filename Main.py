# ST1507 DATA STRUCTURES AND ALGORITHM (AI) CA2 ASSIGNMENT: ASSIGNMENT STATEMENT EVALUATOR & SORTER
# NAME: EDWARD TAN YUAN CHONG; ASHWIN RAJ
# CLASS: DAAA/FT/2B/04
# ADM NO: 2214407; 2239716

# MAIN.PY
'''
This is the Main file which handles the main application, inclusive of the printing of the banner, handling user choices for the menu of the application,
and running the Class methods to perform the menu option's functions.
'''

# IMPORT MODULES
from Classes.AssignmentStatement import AssignmentStatement

# Main class
class Main(AssignmentStatement):
    # Initialization
    def __init__(self):
        # Initialize AssignmentStatement Class
        super().__init__()
        # Banner 
        self._banner=['*'*59, "* ST1507 DSAA: Evaluating & Sorting Assignment Statements *", "*" + "-"*57 + "*", "*" + " "*57 + "*", "*  - Done by: Edward Tan (2214407) & Ashwin Raj (2239716) *", "*  - Class DAAA/2B/04" + " " * 37 + "*"]
        self.__banner_order = [0,1,2,3,4,5,3,0]
        # Menu options
        self.choice = None
        self._menu_options = ['Add/Modify assignment statement', 'Display current assignment statements', 'Evaluate a single variable', 'Read assignment statements from file', 'Sort assignment statements', 'Exit']
        self.__options = {
            1: super().add_modify_statement,
            2: super().display_statements
        }
        self._exit = "\nBye, thanks for using ST1507 DSAA: Assignment Statement Evaluator & Sorter"

    # Start banner
    def _start_banner(self):
        # Print banner
        for order in self.__banner_order:
            print(self._banner[order])
        print("\n")

    # Menu prompt
    def _menu(self):
        # Print menu
        print("Please select a choice ('1','2','3','4','5','6'):")
        for i in range(len(self._menu_options)):
            print(f"    {i+1}. {self._menu_options[i]}")
        # User input for menu option
        self.choice = int(input("Enter choice: "))

    # Run main application
    def run(self):
        # Start banner
        self._start_banner()
        # While loop for menu
        while True:
            try:
                # Prompt users for choice
                self._menu()
                # If user options are between 1 and 6
                if self.choice in range(1,6):
                    try:
                        # Get menu option function
                        option = self.__options.get(self.choice)
                        # Run menu option selected by user
                        option()
                    # Handle Keyboard Interrupt (CRTL + C)
                    except KeyboardInterrupt:
                        print("\nReturning back to main menu...")
                    input("\nPlease enter key to continue...\n")
                # Else if choice is 8 (exit application)
                elif self.choice == 6:
                    print(f"{self._exit}")
                    break
                # Else print error message (user option is not valid)
                else:
                    print("Only options between 1 and 6 are available. Please try again.")
            # Handle ValueError (user choice is not integer)
            except ValueError as ve:
                print(ve)
                print("\nInput must be an integer. Please try again.\n")
            # Handle Keyboard Interrupt (CRTL + C)
            except KeyboardInterrupt:
                print(f"\n{self._exit}")
                break
            # Handle errors
            except Exception as e:
                print(e)

# Instantiate Main class
main = Main()
# Run main application
main.run()
