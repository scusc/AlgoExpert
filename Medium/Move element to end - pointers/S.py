def moveElementToEnd(array, toMove):
    left = 0
    right = len(array)-1
    while left < right:
        if array[left] is toMove and array[right] is not toMove:
            array[left], array[right] = array[right], array[left]
        elif array[left] is not toMove:
            left += 1
        elif array[right] is toMove:
            right -= 1
    return array