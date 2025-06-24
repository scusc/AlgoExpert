class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def symmetricalTree(tree):
    return checkSymmetry(tree.left, tree.right)

def checkSymmetry(left, right):
    if left and right and left.value == right.value:
        return checkSymmetry(left.left, right.right) and checkSymmetry(left.right, right.left)
    return left == right