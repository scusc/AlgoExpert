class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    ancestral_history = set()
    while descendantOne:
        ancestral_history.add(descendantOne.name)
        descendantOne = descendantOne.ancestor
    while descendantTwo:
        if descendantTwo.name in ancestral_history:
            return descendantTwo
        descendantTwo = descendantTwo.ancestor
    return None