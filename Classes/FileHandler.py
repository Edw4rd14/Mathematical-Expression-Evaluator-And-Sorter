# =================================================================================================
# ST1507 DATA STRUCTURES AND ALGORITHM (AI) CA2 ASSIGNMENT: ASSIGNMENT STATEMENT EVALUATOR & SORTER
# NAME: EDWARD TAN YUAN CHONG; ASHWIN RAJ
# CLASS: DAAA/FT/2B/04
# ADM NO: 2214407; 2239716
# =================================================================================================
# FILENAME: FileHandler.py
# =================================================================================================

# Import Data Structures
from DataStructures.Deque import Deque
# Import Classes
from Classes.InputHandler import InputHandler
# Import Modules
import os

# FileHandler class
class FileHandler(InputHandler):
    # Initialization
    def __init__(self):
        """
        The __init__ function is called when the class is instantiated.
        It initializes all of the attributes that are required for this class.
        
        :param self: Refer to the instance of the class
        :return: Nothing
        """
        super().__init__()

    def validate_file(self,question:str, mode:str=None)->str:
        """
        The validate_file function is used to validate user input for file paths.
        It takes two arguments: a question string and an optional mode string.
        The question argument is the prompt that will be displayed to the user, asking them for their input.
        The mode argument can either be 'r' or 'w', which stands for read or write respectively, and defaults to None if not specified by the caller.
        
        :param self: Refer to the instance of the class
        :param question: str: Prompt the user for a file path
        :param mode: str: Determine if the file is being read or written to
        :return: The file path
        """
        # Get user input on input file path
        file_path = input(question)
        # Validate file extension
        if not file_path.endswith(".txt"):
            raise ValueError(f"\n'{file_path}' is an invalid file type. Expected a .txt file. {self.err_msg}")
        # Validate file existence for reading
        if mode == 'r' and not os.path.exists(file_path):
            raise FileNotFoundError(f"\nFile path '{file_path}' does not exist. {self.err_msg}")
        # If no errors, return file path
        return file_path
    
    def validate_folder(self, question:str)->str:
        while True:
            folder_path = input(question)
            if os.path.isdir(folder_path):
                return folder_path
            print(f"\nFolder path '{folder_path}' does not exist. {self.err_msg}")
    
    def read_folder(self, folder_path:str):
        # File deque
        file_deque = Deque()
        # Loop folder content
        for dir_name, _, file_list in os.walk(folder_path):
            # Loop file
            for files in file_list:
                # Directory variable etc. "CASE01/file01.txt"
                file_directory = dir_name+"/"+files
                # Check if directory leads to an existing file, is a text file (ends with .txt)
                print(files)
                if os.path.isfile(file_directory) and files.endswith('.txt') and not "file-" in files and files != 'logs.txt':
                    # Open file
                    with open(file_directory, 'r') as file:
                        # Read file content
                        file_contents = file.readlines()
                        # Append to Queue
                        file_deque.add_head(data=(files,file_contents))
        # Return Queue object and directory name
        return file_deque, dir_name
    
    # File operation (read/write)
    def file_operation(self, file_path: str, mode: str, content: str = None, menu=True):
        # Try and except to catch errors
        try:
            # Check if file exists and mode is 'write'
            if mode == 'w' and os.path.exists(file_path):
                # New line outside of loop
                print()
                overwrite = self.prompt_polar_question(question=f"File '{file_path}' already exists. Overwrite? (Y/N): ")
                if not overwrite:
                    print("\nWrite operation cancelled." + (" Returning back to main menu..." if menu else ""))
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
            raise FileNotFoundError(f"\nError occurred with file '{file_path}'.")