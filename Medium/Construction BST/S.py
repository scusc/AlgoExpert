# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        cur = self
        while cur is not None:
            if value < cur.value:
                if cur.left is not None:
                    cur = cur.left
                else:
                    cur.left = BST(value)
                    break
            else:
                if cur.right is not None:
                    cur = cur.right
                else:
                    cur.right = BST(value)
                    break
        return self

    def contains(self, value):
        # Write your code here.
        cur = self
        while cur is not None:
            if value == cur.value:
                return True
            elif value < cur.value:
                cur = cur.left
            else:
                cur = cur.right
        return False
    
    def getMin(self):
        cur = self
        while cur.left is not None:
            cur = cur.left
        return cur.value

    def remove(self, value, parent = None):
        # Write your code here.
        # Do not edit the return statement of this method.
        cur = self
        while cur is not None:
            if value < cur.left:
                parent = cur
                cur = cur.left
            elif value > cur.right:
                parent = cur
                cur = cur.right
            else:
                if cur.left is not None and cur.right is not None:
                    cur.value = cur.right.getMin()
                    cur.right.remove(cur.value, cur)
                elif parent is None:
                    if cur.left is not None:
                        cur.value = cur.left
                        cur.right = cur.left.right
                        cur.left = cur.left.left
                    elif cur.right is not None:
                        cur.value = cur.right
                        cur.right = cur.right.right
                        cur.left = cur.right.left
                elif parent == cur.left:
                    parent.left = cur.left  if cur.left else cur.right
                elif parent == cur.right:
                    parent.right = cur.left if cur.left else cur.right
                break
        return self
