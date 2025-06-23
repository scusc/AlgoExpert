class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def heightBalancedBinaryTree(tree):
    global balanced
    balanced = [True]
    checkBalance(tree)
    return balanced[-1]

def checkBalance(tree):
    if tree is None:
        return 0
    global balanced
    leftDepth = checkBalance(tree.left)
    rightDepth = checkBalance(tree.right)
    if abs(leftDepth - rightDepth) > 1:
        balanced.append(False)
    return max(leftDepth, rightDepth) + 1