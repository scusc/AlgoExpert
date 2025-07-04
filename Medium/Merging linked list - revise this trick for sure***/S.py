class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergingLinkedLists(linkedListOne, linkedListTwo):
    l1 = linkedListOne
    l2 = linkedListTwo
    while l1 != l2:
        l1 = l1.next if l1 else linkedListTwo
        l2 = l2.next if l2 else linkedListOne
    return l1