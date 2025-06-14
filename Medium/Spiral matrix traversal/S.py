def spiralTraverse(array):
    res = []
    while array:
        res +=array.pop(0)
        array = list(zip(*array))[::-1]
    return res