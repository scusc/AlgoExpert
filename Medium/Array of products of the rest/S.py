def arrayOfProducts(array):
    res = []
    for i in range(len(array)):
        curProd = 1
        leftIndex = i-1
        rightIndex = i+1
        while leftIndex >= 0:
            curProd *= array[leftIndex]
            leftIndex -= 1
        while rightIndex < len(array):
            curProd *= array[rightIndex]
            rightIndex += 1
        res.append(curProd)
    return res