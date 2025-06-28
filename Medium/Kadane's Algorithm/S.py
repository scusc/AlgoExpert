def kadanesAlgorithm(array):
    temp = array[0]
    maxi = array[0]

    for val in array[1:]:
        temp = max(val, temp + val)
        maxi = max(maxi, temp)

    return maxi