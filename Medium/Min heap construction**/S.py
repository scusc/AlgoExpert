# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        firstParentIndex = (len(array)-2) // 2
        for currentIndex in reversed(range(firstParentIndex + 1)):
            self.siftDown(array, currentIndex)
        return array

    def siftDown(self, heap, currentIndex = 0):
        endIndex = len(heap) - 1
        childOneIndex = (currentIndex * 2) + 1
        while childOneIndex <= endIndex:
            childTwoIndex = childOneIndex + 1 if childOneIndex + 1 <= endIndex else -1
            if childTwoIndex != -1 and heap[childTwoIndex] < heap[childOneIndex]:
                indexToSwap = childTwoIndex
            else:
                indexToSwap = childOneIndex

            if heap[indexToSwap] < heap[currentIndex]:
                self.swap(indexToSwap, currentIndex, heap)
                currentIndex = indexToSwap
                childOneIndex = (currentIndex * 2) + 1
            else:
                return

    def siftUp(self, heap):
        currentIndex = len(heap) - 1
        parentIndex = (currentIndex - 1) // 2
        while currentIndex > 0 and heap[currentIndex] < heap[parentIndex]:
            self.swap(currentIndex, parentIndex, heap)
            currentIndex = parentIndex
            parentIndex = (currentIndex - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap)-1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(self.heap)
        return valueToRemove

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
