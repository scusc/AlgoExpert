class UnionFind:
    def __init__(self):
        self.parents = {}
    
    def createSet(self, value):
        self.parents[value] = value
    
    def find(self, value):
        if value not in self.parents.keys():
            return None
        
        if self.parents[value] != value:
            self.parents[value] = self.find(self.parents[value])
        return self.parents[value]
    
    def union(self, valueOne, valueTwo):
        if valueOne not in self.parents.keys() or valueTwo not in self.parents.keys():
            return
        rootOne = self.find(valueOne)
        rootTwo = self.find(valueTwo)
        self.parents[rootOne] = rootTwo

