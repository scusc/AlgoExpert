class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        queue = [self]
        while len(queue) > 0:
            curr = queue.pop(0)
            array.append(curr.name)
            for child in curr.children:
                queue.append(child)
        return array