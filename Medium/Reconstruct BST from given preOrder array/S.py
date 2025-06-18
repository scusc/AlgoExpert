class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
    root = BST(preOrderTraversalValues[0])
    leftNodes = []
    rightNodes = []
    for val in preOrderTraversalValues[1:]:
        if val < root.value:
            leftNodes.append(val)
        else:
            rightNodes.append(val)
    
    if leftNodes:
        root.left = reconstructBst(leftNodes)
    if rightNodes:
        root.right = reconstructBst(rightNodes)
    
    return root