class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def splitBinaryTree(tree):
    sums = set()
    total = getLeftRightSums(tree, sums)
    return total/2 if total/2 in sums else 0

def getLeftRightSums(tree, sums):
    if tree is None:
        return 0
    
    total = tree.value + getLeftRightSums(tree.left, sums) + getLeftRightSums(tree.right, sums)
    sums.add(total)
    return total