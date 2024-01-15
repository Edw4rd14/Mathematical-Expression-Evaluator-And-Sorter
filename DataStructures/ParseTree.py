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
        self.root = self.build_parse_tree(self.expression)

    # Build a parse tree
    def build_parse_tree(self,expression):        
        stack = Stack()
        tree = BinaryTree(root_object=None)
        stack.push(tree)
        current_tree = tree
        tokens = tokenize(expression)
        for t in tokens:
            # RULE 1: If token is '(' add a new node as left tree and descend into that node
            if t == '(':
                current_tree.insert_left(None)
                stack.push(current_tree)
                current_tree = current_tree.get_left_tree()
            # RULE 2: If token is operator set key of current node to that operator and add a new node as right tree and descend into that node
            elif t in ['+', '-', '*', '/']:
                current_tree.set_root_value(t)
                current_tree.insert_right(None)
                stack.push(current_tree)
                current_tree = current_tree.get_right_tree()
            # RULE 3: If token is number, set key of the current node to that number and return to parent
            elif t not in ['+', '-', '*', '/', ')']:
                if t.isnumeric():
                    current_tree.set_root_value(int(t))
                elif t in self.hash_table.keys:
                    # If value is a string, build a subtree
                    current_tree.set_root_value(int(t) if t.isnumeric() else self._evaluate_tree(self.build_parse_tree(self.hash_table[t])))
                else:
                    current_tree.set_root_value(None)
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

    # Evaluate tree
    def _evaluate_tree(self,tree):
        try:
            # Get the left and right subtrees of the current node
            left_tree = tree.get_left_tree()
            right_tree = tree.get_right_tree()
            # Get the operator stored in the current node
            op = tree.get_root_value()
            # Check if both left and right subtrees exist
            if left_tree is not None and right_tree is not None:
                # Recursively evaluate the left and right subtrees
                left, right = self._evaluate_tree(left_tree), self._evaluate_tree(right_tree)
                # Perform the arithmetic operation based on the operand
                if op == '+':
                    return left + right
                elif op == '-':
                    return left - right
                elif op == '*':
                    return left * right
                elif op == '/':
                    # Check for division by zero before performing the division.
                    if right != 0:
                        return left / right
                    else:
                        # Handle division by zero by returning None.
                        return None
            else:
                # If either left or right subtree is missing, return the value stored in the current node
                return tree.get_root_value()
        except:
            # Return None if there are any errors
            return None