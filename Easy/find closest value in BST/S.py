# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def findClosestValueInBst(tree, target):
    res = tree.value
    while tree is not None:
        if(abs(tree.value - target) < abs(res-target)):
            res = tree.value
        if target == tree.value:
            break
        if target < tree.value:
            tree = tree.left
        else:
            tree = tree.right
    return res