class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def nodeDepths(root, dep=0):
    if root is None: return 0
    return dep + nodeDepths(root.left, dep+1) + nodeDepths(root.right, dep+1)