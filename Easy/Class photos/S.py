def classPhotos(redShirtHeights, blueShirtHeights):
    rowLen = len(redShirtHeights)
    redShirtHeights.sort()
    blueShirtHeights.sort()
    isBlueFirst = redShirtHeights[0] > blueShirtHeights[0]
    for i in range(rowLen):
        if (redShirtHeights[i] == blueShirtHeights[i]) or (isBlueFirst and redShirtHeights[i] < blueShirtHeights[i]) or (not isBlueFirst and redShirtHeights[i] > blueShirtHeights[i]):
            return False
    return True