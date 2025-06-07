class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    if root is None:
        return []
    branches = branchSums(root.left) + branchSums(root.right)
    return [curSum + root.value for curSum in branches] if branches else [root.value]