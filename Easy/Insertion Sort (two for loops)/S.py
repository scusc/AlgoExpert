def insertionSort(array):
    for i in range(len(array)-1):
        for j in range(i+1, 0, -1):
            if array[j]<array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break
    return array