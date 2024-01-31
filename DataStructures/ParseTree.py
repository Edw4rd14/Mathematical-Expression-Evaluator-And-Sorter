# =================================================================================================
# ST1507 DATA STRUCTURES AND ALGORITHM (AI) CA2 ASSIGNMENT: ASSIGNMENT STATEMENT EVALUATOR & SORTER
# NAME: EDWARD TAN YUAN CHONG; ASHWIN RAJ
# CLASS: DAAA/FT/2B/04
# ADM NO: 2214407; 2239716
# =================================================================================================
# FILENAME: ParseTree.py
# =================================================================================================
'''
Description:
This is the Main file which handles the main application, inclusive of the printing of the banner, handling user choices for the menu of the application,
and running the Class methods to perform the menu option's functions.
'''

# Import Data Structures
from DataStructures.Stack import Stack
from DataStructures.BinaryTree import BinaryTree
# Import Utils
# from Utils import tokenize
import re

# ParseTree Class
class ParseTree:
    # Initialization
    def __init__(self, expression, hash_table):
        # Hashtable with variables stored
        self.hash_table = hash_table
        # Build parse tree of expression
        self.expression = expression
        # Root tree
        self.root = self.build_parse_tree(self.expression)

    # Tokenize expression
    @staticmethod
    def tokenize(expression:str)->list:
        """
        The tokenize function takes a string and returns a list of tokens.
        The tokenize function uses the regular expression r'(\b\d+\.\d+\b|\b\w+\b|[^ \t]+)' to match:
            - decimal numbers, e.g., 3.15;
            - whole words, e.g., 'apple';
            - operators and single characters, e.g., '*', '/', '('.  
        
        :param expression:str: Expression to be tokenized
        :return: A list of tokens
        """
        # \b\w+\b matches whole words.
        # \*\* matches the ** operator.
        # // matches the // operator.
        # \S matches any non-whitespace character, covering other operators and single characters.
        # (\d+\.\d+) matches decimal numbers.
        tokens = re.findall(r'(\b\d+\.\d+\b|\b\w+\b|\*\*|//|\S)', expression)
        return tokens


    # Build a parse tree
    def build_parse_tree(self,expression):        
        stack = Stack()
        tree = BinaryTree(root_object=None)
        stack.push(tree)
        current_tree = tree
        try:
            tokens = self.tokenize(expression)
        except:
            raise ValueError
        for t in tokens:
            # RULE 1: If token is '(' add a new node as left tree and descend into that node
            if t == '(':
                current_tree.insert_left(None)
                stack.push(current_tree)
                current_tree = current_tree.left_tree
            # RULE 2: If token is operator set key of current node to that operator and add a new node as right tree and descend into that node
            elif t in ['+', '-', '*', '**', '/']:
                current_tree.root_value = (t,None)
                current_tree.insert_right(None)
                stack.push(current_tree)
                current_tree = current_tree.right_tree
            # RULE 3: If token is number, set key of the current node to that number and return to parent
            elif t not in ['+', '-', '*',  '**', '/', ')']:
                # Try converting t to float, then to integer (if it is an integer) before checking whether it is a variable or not 
                try:
                    num = float(t)
                    num = int(num) if num.is_integer() else num
                    current_tree.root_value = (num, num)
                except:
                    if t in self.hash_table.keys:
                        # If value is a string, build a subtree and store evaluated value
                        evaluated = self._evaluate_tree(self.build_parse_tree(self.hash_table[t]))
                        current_tree.root_value = (t, evaluated)
                    else:
                        current_tree.root_value = (t,None)
                if not stack.is_empty:
                    current_tree = stack.pop()
            # RULE 4: If token is ')' go to parent of current node
            elif t == ')':
                if not stack.is_empty:
                    current_tree = stack.pop()
            else:
                raise ValueError
        return tree
    
    # Return evaluate tree result
    def evaluate(self):
        return self._evaluate_tree(tree=self.root)

    # Evaluate tree function
    def _evaluate_tree(self,tree):
        try:
            if tree is not None:
                # Extract original token and evaluated value
                original_token, evaluated_value = tree.root_value
                # Get the left and right subtrees of the current node
                left_tree = tree.left_tree
                right_tree = tree.right_tree
                # If evaluated value is not None, return it directly
                if evaluated_value is not None:
                    return evaluated_value
                # Evaluation of operators
                operator_functions = {
                    '+': lambda l, r: l + r,
                    '-': lambda l, r: l - r,
                    '*': lambda l, r: l * r,
                    '**': lambda l,r: l ** r,
                    '/': lambda l, r: l / r if r != 0 else None
                }
                # If the node is an operator, recursively evaluate its operands
                if original_token in operator_functions:
                    left = self._evaluate_tree(left_tree)
                    right = self._evaluate_tree(right_tree)
                    return operator_functions[original_token](left,right)
                else:
                    # If it's a variable, return original value
                    return None
                
        except Exception as e:
            # Handle exceptions or return None if there are any errors
            return None
        
    # Print the expression tree in in-order format with indentation
    def print_in_order(self):
        self._print_in_order(self.root)

    # Print in order function (This is a in-order traversal)
    def _print_in_order(self, node, depth=0):
        # If node is not None
        if node is not None:
            # Recursively call the function on the right tree of the current tree [R]
            self._print_in_order(node.right_tree, depth + 1)
            # Get original token and evaluated value [C]
            original_token, evaluated_value = node.root_value
            # Check if original token is a variable and print it, else print evaluated value
            print_value = evaluated_value if original_token is None else original_token
            # Print the number of dots equal to the current depth and the evaluated/original value
            print(f"{'.' * depth}{print_value}")
            # Recursively call the function on the left tree of the current tree [L]
            self._print_in_order(node.left_tree, depth + 1)

    def variable_dependencies(self):
        dependencies = {}
        self._collect_variable_dependencies(self.root, dependencies)
        return dependencies

    # Helper method to collect variable dependencies recursively
    def _collect_variable_dependencies(self, node, dependencies, path=[]):
        if node is not None:
            original_token, _ = node.root_value
            if isinstance(original_token, str):
                path_context = path + [original_token]
                if original_token not in dependencies:
                    dependencies[original_token] = []
                dependencies[original_token].append(path_context)

            self._collect_variable_dependencies(node.left_tree, dependencies, path + ['L'])
            self._collect_variable_dependencies(node.right_tree, dependencies, path + ['R'])

    # Method to display variable dependencies in a tree-like structure
    def display_variable_dependencies(self):
        dependencies = self.variable_dependencies()

        for variable, paths in dependencies.items():
            print(variable)  # Print the variable name
            unique_paths = set()  # To store unique paths (avoid duplicates)
            
            for path in paths:
                formatted_path = ' -> '.join(path)
                unique_paths.add(formatted_path)

            for path in unique_paths:
                # Split the path into parts and print with indentation
                parts = path.split(' -> ')
                for i, part in enumerate(parts):
                    indent = '  ' * i + '+-' if i > 0 else ''
                    print(f"{indent}{part}")
