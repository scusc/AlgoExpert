class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

def minHeightTree(array):
    left = 0 
    right = len(array)-1
    if left > right:
        return 
    mid = (left+right)//2
    node = BST(array[mid])
    node.left = minHeightTree(array[:mid])
    node.right = minHeightTree(array[mid+1:])
    
    return node