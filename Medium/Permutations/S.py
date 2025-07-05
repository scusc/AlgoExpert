def getPermutations(array):
    res = []
    if len(array) == 1:
         return [array]
    for i in range(len(array)):
        for elem in getPermutations(array[:i] + array[i+1:]):
            res.append([array[i]] + elem)
    return res