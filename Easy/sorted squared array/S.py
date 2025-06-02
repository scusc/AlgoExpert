def sortedSquaredArray(array):
    return sorted(list(map(lambda val: abs(val)**2, array)))