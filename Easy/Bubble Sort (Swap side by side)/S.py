def sort(array):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i+1], array[i] = array[i], array[i+1]
                sorted = False
    return array
