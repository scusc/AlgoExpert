class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    slow = fast = linkedList # because fast goes twice as fast, when it reaches the end, slow is at the middle.
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow    