# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def evaluateExpressionTree(tree):
    ops = {
        -1: lambda x,y: x+y,
        -2: lambda x,y: x-y,
        -3: lambda x,y: int(x/y),
        -4: lambda x,y: x*y
    }
    op = ops.get(tree.value)

    if op:
        return op(evaluateExpressionTree(tree.left), evaluateExpressionTree(tree.right))
    return tree.value