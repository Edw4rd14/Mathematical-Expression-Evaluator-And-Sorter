# =================================================================================================
# ST1507 DATA STRUCTURES AND ALGORITHM (AI) CA2 ASSIGNMENT: ASSIGNMENT STATEMENT EVALUATOR & SORTER
# NAME: EDWARD TAN YUAN CHONG; ASHWIN RAJ
# CLASS: DAAA/FT/2B/04
# ADM NO: 2214407; 2239716
# =================================================================================================
# FILENAME: Utils.py
# =================================================================================================

# Import Modules
import os
# Import classes
from Classes.InputValidation import InputValidation

# ================================
# Utils for AssignmentStatement.py
# ================================

# Instantiate Input Validation class
input_validation = InputValidation()
# End of error message
err_msg = 'Please try again or CRTL + C to return back to main menu.\n'

# Get key and value from statement
def get_key_and_value(statement:str)->list:
    return [x.strip() for x in statement.split('=')]

# File operation (read/write)
def file_operation(file_path: str, mode: str, content: str = None):
    # Try and except to catch errors
    try:
        # Check if file exists and mode is 'write'
        if mode == 'w' and os.path.exists(file_path):
            # New line outside of loop
            print()
            overwrite = input_validation.prompt_polar_question(question=f'File "{file_path}" already exists. Overwrite? (Y/N): ')
            if not overwrite:
                print("\nWrite operation cancelled. Returning back to main menu...")
                return
        # Open file
        with open(file_path, mode, encoding='utf-8') as file:
            # If mode is write
            if mode == 'w':
                file.write(content)
            # Else mode is read
            else:
                return file.readlines()
    # Catch any errors
    except Exception:
        raise FileNotFoundError(f'\nError occurred with file "{file_path}".')