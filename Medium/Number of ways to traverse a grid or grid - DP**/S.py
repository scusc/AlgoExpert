def numberOfWaysToTraverseGraph(width, height):
    result = [[0 for _ in range(width + 1) for _ in range(height + 1)]]

    for heightIdnex in range(1, height + 1):
        for widthIndex in range(1, width + 1):
            if heightIdnex == 1 or widthIndex == 1:
                result[heightIdnex][widthIndex] = 1
            else:
                result[heightIdnex][widthIndex] = result[heightIdnex][widthIndex - 1] + result[heightIdnex - 1][widthIndex]
    
    return result[height][width]
