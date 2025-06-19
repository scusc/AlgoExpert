class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def inOrder(tree, array =[]):
    if tree is None:
        return 
    inOrder(tree.left, array)
    array.append(tree)
    inOrder(tree.right, array)
    return array

def findSuccessor(tree, node):
    # Write your code here.
    values = inOrder(tree)
    for i in range(len(values)-1):
        if values[i] == node:
            return values[i+1]
    return None
