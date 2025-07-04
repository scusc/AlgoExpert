class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(l1, l2):
    dummy = tail = LinkedList(None)
    carry = 0
    while l1 or l2 or carry:
        val1 = l1.value if l1 else 0
        val2 = l2.value if l2 else 0
        carry, val = divmod(val1 + val2 + carry, 10)
        tail.next = LinkedList(val)
        tail = tail.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next