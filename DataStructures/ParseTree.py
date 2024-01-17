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
from Utils import tokenize

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

    # Build a parse tree
    def build_parse_tree(self,expression):        
        stack = Stack()
        tree = BinaryTree(root_object=None)
        stack.push(tree)
        current_tree = tree
        try:
            tokens = tokenize(expression)
        except:
            raise ValueError
        for t in tokens:
            # RULE 1: If token is '(' add a new node as left tree and descend into that node
            if t == '(':
                current_tree.insert_left(None)
                stack.push(current_tree)
                current_tree = current_tree.get_left_tree()
            # RULE 2: If token is operator set key of current node to that operator and add a new node as right tree and descend into that node
            elif t in ['+', '-', '*', '/']:
                current_tree.set_root_value((t,None))
                current_tree.insert_right(None)
                stack.push(current_tree)
                current_tree = current_tree.get_right_tree()
            # RULE 3: If token is number, set key of the current node to that number and return to parent
            elif t not in ['+', '-', '*', '/', ')']:
                if t.isnumeric():
                    current_tree.set_root_value((int(t),int(t)))
                elif t in self.hash_table.keys:
                    # If value is a string, build a subtree and store evaluated value
                    evaluated = self._evaluate_tree(self.build_parse_tree(self.hash_table[t]))
                    current_tree.set_root_value((t, evaluated))
                else:
                    current_tree.set_root_value((t,None))
                if not stack.is_empty():
                    current_tree = stack.pop()
            # RULE 4: If token is ')' go to parent of current node
            elif t == ')':
                if not stack.is_empty():
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
                original_token, evaluated_value = tree.get_root_value()
                # Get the left and right subtrees of the current node
                left_tree = tree.get_left_tree()
                right_tree = tree.get_right_tree()

                # If evaluated value is not None, return it directly
                if evaluated_value is not None:
                    return evaluated_value

                # If the node is an operator, recursively evaluate its operands
                if original_token in ['+', '-', '*', '/']:
                    left = self._evaluate_tree(left_tree)
                    right = self._evaluate_tree(right_tree)

                    if original_token == '+':
                        return left + right
                    elif original_token == '-':
                        return left - right
                    elif original_token == '*':
                        return left * right
                    elif original_token == '/':
                        if right != 0:
                            return left / right
                        else:
                            return None  # Handle division by zero
                else:
                    # If it's a variable, look up its value in the hash table
                    return tree.get_root_value()
        except Exception as e:
            # Handle exceptions or return None if there are any errors
            return None
        
    # Print the expression tree in in-order format with indentation
    def print_in_order(self):
        self._print_in_order(self.root)

    # Print in order function
    def _print_in_order(self, node, depth=0):
        if node is not None:
            self._print_in_order(node.get_right_tree(), depth + 1)
            
            # Get original token and evaluated value
            original_token, evaluated_value = node.get_root_value()
            # Check if original token is a variable and print it, else print evaluated value
            print_value = evaluated_value if original_token is None else original_token
            print(f"{'.' * depth}{print_value}")

            self._print_in_order(node.get_left_tree(), depth + 1)