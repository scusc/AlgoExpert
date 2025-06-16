def sweetAndSavory(dishes, target):
    dishes.sort()
    sweets = list(filter(lambda x: x<0, dishes))[::-1]
    savory = dishes[len(sweets): len(dishes)]
    res = [0, 0]
    bestDiff = 99999
    sweetIndex, savIndex = 0, 0
    while sweetIndex < len(sweets) and savIndex < len(savory):
        curSum = sweets[sweetIndex] + savory[savIndex]
        if curSum <= target:
            if target - curSum < bestDiff:
                bestDiff = target - curSum
                res = [sweets[sweetIndex], savory[savIndex]]
            savIndex += 1
        else:
            sweetIndex += 1
    return res