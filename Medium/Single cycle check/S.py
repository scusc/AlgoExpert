def hasSingleCycle(array):
    counter = 0
    index = array[0]%len(array)
    while counter < len(array) - 1 and index != 0:
        counter += 1
        index = (index + array[index]) % len(array)
    return counter == len(array) - 1 and index == 0
