def selectionSort(array):
    for i in range(len(array)-1):
        k = i
        for j in range(i+1, len(array)):
            if array[j] < array[k]:
                k = j 
        array[i], array[k] = array[k], array[i]
    return array