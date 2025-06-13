def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    inx1, inx2 = 0,0
    res = 999999
    val1, val2 = 0,0
    while inx1 < len(arrayOne) and inx2  < len(arrayTwo):
        diff = abs(arrayOne[inx1] - arrayTwo[inx2])
        if diff < res:
            res = diff
            val1, val2 = arrayOne[inx1], arrayTwo[inx2]
        if arrayOne[inx1] < arrayTwo[inx2]:
            inx1 += 1
        else:
            inx2 += 1
    return [val1, val2]