# =================================================================================================
# ST1507 DATA STRUCTURES AND ALGORITHM (AI) CA2 ASSIGNMENT: ASSIGNMENT STATEMENT EVALUATOR & SORTER
# NAME: EDWARD TAN YUAN CHONG; ASHWIN RAJ
# CLASS: DAAA/FT/2B/04
# ADM NO: 2214407; 2239716
# =================================================================================================
# FILENAME: ParseTree.py
# =================================================================================================

# Import Data Structures
from DataStructures.Stack import Stack
from DataStructures.BinaryTree import BinaryTree
# Import Classes
from Classes.ExpressionHandler import ExpressionHandler

# ParseTree Class
class ParseTree:
    # Initialization
    def __init__(self, variable, expression, hash_table):
        """
        The __init__ function is called when the class is instantiated.
        It initializes all of the attributes that are required for this class.
        
        :param self: Refer to the instance of the class
        :param expression: Store the expression that is passed in as a string
        :param hash_table: Store the variables in a hash table
        :return: Nothing
        """
        # Hashtable with variables stored
        self.hash_table = hash_table
        # Variable of expression
        self.variable = variable
        # Expression Handler
        self.expression_handler = ExpressionHandler()
        # Build parse tree of expression
        self.expression = expression
        # Root tree
        self.root = self.build_parse_tree(self.expression)

    # Build a parse tree - Done by Edward
    def build_parse_tree(self, expression):     
        """
        The build_parse_tree function takes an expression as a string and returns a binary tree representation of that expression.
        The function uses the tokenize function to break the input into tokens, then it iterates through each token in order and
        evaluates the expression, returning None if the expression has unknown variables.

        :param self: Refer to the instance of the class
        :param expression: Build the parse tree
        :return: A tree with the root node set to none
        """
        stack = Stack()
        tree = BinaryTree(root_object=None)
        stack.push(tree)
        current_tree = tree
        try:
            tokens = self.expression_handler.tokenize(expression)
        except:
            raise
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
                raise
        return tree
    
    # Return evaluate tree result - Done by Edward
    def evaluate(self):
        """
        The evaluate function calls the protected function _evaluate_tree to evaluate the root binary tree expression. 
        The evaluate function is the public interface of the _evaluate_tree function.
        
        :param self: Refer to the instance of the class
        :return: The value of the root node
        """
        return self._evaluate_tree(tree=self.root)

    # Evaluate tree function - Done by Edward
    def _evaluate_tree(self,tree):
        """
        The _evaluate_tree function takes the root of a tree and returns the result of evaluating that tree.
        The _evaluate_tree function is recursive, so it calls itself on each node in the tree until it reaches a leaf node.
        When it reaches a leaf node, if that leaf is an operand (a number), then we return its value as an integer.
        If that leaf is an operator (+,-,*,/), then we call evaluate on its left and right children to get their values 
        (which are integers) and perform the operation between the two nodes.
        
        :param self: Refer to the instance of the class
        :param tree: Store the tree structure of the expression
        :return: The value of the expression
        """
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
        except Exception:
            # Handle exceptions or return None if there are any errors
            return None
        
    # Print the expression tree in in-order format with indentation - Done by Ashwin
    def print_in_order(self):
        """
        The print_in_order function prints the tree in order.
        
        :param self: Refer to the instance of the class
        :return: The in-order traversal of the tree
        """
        self._print_in_order(self.root)

    # Print in order function (This is a in-order traversal) - Done by Edward & Ashwin
    def _print_in_order(self, node, depth=0):
        """
        The _print_in_order function is a recursive function that prints the tree in order.
        The printout will be in an in order traversal format, in a RIGHT-CENTER-LEFT format.
        
        :param self: Refer to the instance of the class
        :param node: Represent the current node in the tree
        :param depth: Keep track of the depth of the current node in the tree
        :return: None
        """
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