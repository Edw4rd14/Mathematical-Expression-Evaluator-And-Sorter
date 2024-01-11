# ST1507 DATA STRUCTURES AND ALGORITHM (AI) CA2 ASSIGNMENT: ASSIGNMENT STATEMENT EVALUATOR & SORTER
# NAME: EDWARD TAN YUAN CHONG; ASHWIN RAJ
# CLASS: DAAA/FT/2B/04
# ADM NO: 2214407; 2239716

# ParseTree.py

# Import modules
from DataStructures.Stack import Stack
from DataStructures.BinaryTree import BinaryTree

# ParseTree Class
class ParseTree:
    # Initialization
    def __init__(self, expression, hashTable):
        # Hashtable with variables stored
        self.hashTable = hashTable
        # Build parse tree of expression
        self.root = self.build_parse_tree(expression)
        # Regex expression
        self.regex = r'\s*(?:(\d+)|(\w+)|(.))'

    # Tokenize expression
    @staticmethod
    def tokenize(expression):
        return [*expression]
    
    # Build a parse tree
    def build_parse_tree(self,expression):
        tokens = self.tokenize(expression)
        stack = Stack()
        tree = BinaryTree(root_object=None)
        stack.push(tree)
        current_tree = tree
        for t in tokens:
            # RULE 1: If token is '(' add a new node as left child and descend into that node
            if t == '(':
                current_tree.insert_left(None)
                stack.push(current_tree)
                current_tree = current_tree.get_left_child()
            # RULE 2: If token is operator set key of current node to that operator and add a new node as right child and descend into that node
            elif t in ['+', '-', '*', '/']:
                current_tree.set_root_value(t)
                current_tree.insert_right(None)
                stack.push(current_tree)
                current_tree = current_tree.get_right_child()
            # RULE 3: If token is number, set key of the current node to that number and return to parent
            elif t not in ['+', '-', '*', '/', ')']:
                if t.isnumeric():
                    current_tree.set_root_value(int(t))
                else:
                    current_tree.set_root_value(self._evaluate_tree(self.build_parse_tree(self.hashTable[t])))
                parent = stack.pop()
                current_tree = parent
            # RULE 4: If token is ')' go to parent of current node
            elif t == ')':
                current_tree = stack.pop()
            else:
                raise ValueError
        return tree
    
    # Return evaluate tree result
    def evaluate(self):
        return self._evaluate_tree(tree=self.root)

    # Evaluate tree
    def _evaluate_tree(self,tree):
        left_tree = tree.get_left_child()
        right_tree = tree.get_right_child()
        op = tree.get_root_value()
        if left_tree != None and right_tree != None:
            if op == '+':
                return self._evaluate_tree(left_tree) + self._evaluate_tree(right_tree)
            elif op == '-':
                return self._evaluate_tree(left_tree) - self._evaluate_tree(right_tree)
            elif op == '*':
                return self._evaluate_tree(left_tree) * self._evaluate_tree(right_tree)
            elif op == '/':
                return self._evaluate_tree(left_tree) / self._evaluate_tree(right_tree)
        else:
            return tree.get_root_value()