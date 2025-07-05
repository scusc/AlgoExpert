def staircaseTraversal(height, maxSteps):
    curWays = 0
    waysToTop = [1]
    
    for curHeight in range(1, height + 1):
        start = curHeight - maxSteps - 1
        end = curHeight - 1
        
        if start >=0:
            curWays -= waysToTop[start]
        
        curWays += waysToTop[end]
        waysToTop.append(curWays)
    
    return waysToTop[-1]