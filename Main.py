# ST1507 DATA STRUCTURES AND ALGORITHM (AI) CA2 ASSIGNMENT: ASSIGNMENT STATEMENT EVALUATOR & SORTER
# NAME: EDWARD TAN YUAN CHONG; ASHWIN RAJ
# CLASS: DAAA/FT/2B/04
# ADM NO: 2214407; 2239716

# MAIN.PY

# IMPORT MODULES

# Main class
class Main:
    # Initialization
    def __init__(self):
        self._banner=['*'*59, "* ST1507 DSAA: Evaluating & Sorting Assignment Statements *", "*" + "-"*57 + "*", "*" + " "*57 + "*", "*  - Done by: Edward Tan (2214407) & Ashwin Raj (2239716) *", "*  - Class DAAA/2B/04" + " " * 37 + "*"]
        self.__banner_order = [0,1,2,3,4,5,3,0]
        self.choice = None
        self._menu_options = ['Add/Modify assignment statement', 'Display current assignment statements', 'Evaluate a single variable', 'Read assignment statements from file', 'Sort assignment statements', 'Exit']
        self.__options = {}
        self._exit = "Bye, thanks for using ST1507 DSAA: Assignment Statement Evaluator & Sorter"

    # Start banner
    def _start_banner(self):
        for order in self.__banner_order:
            print(self._banner[order])
        # Print banner
        # print(f'{self._banner[0]}\n{self._banner[1]}\n{self._banner[2]}\n{self._banner[3]}\n{self._banner[4]}\n{self._banner[5]}\n{self._banner[3]}\n{self._banner[0]}\n')

    # Menu prompt
    def _menu(self):
        print("\n\nPlease select a choice ('1','2','3','4','5','6'):")
        for i in range(len(self._menu_options)):
            print(f"    {i+1}. {self._menu_options[i]}")
        self.choice = input("Enter choice: ")

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
                    print(self._exit)
                    break
                # Else print error message (user option is not valid)
                else:
                    print("\nOnly options between 1 and 6 are available. Please try again.")
            # Handle errors
            except Exception as e:
                print(e)
            # Handle Keyboard Interrupt (CRTL + C)
            except KeyboardInterrupt:
                print(f"\n{self._exit}")
                break

# Instantiate Main class
main = Main()
# Run main application
main.run()
