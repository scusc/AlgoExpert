def threeNumberSum(array, targetSum):

    array.sort()
    res = []
    for i in range(len(array)):
        left = i+1
        right = len(array)-1
        while left < right:
            curSum = array[i] + array[left] + array[right]
            if curSum < targetSum:
                left += 1
            elif curSum > targetSum:
                right -= 1
            elif curSum ==targetSum:
                res.append(array[i], array[left], array[right])
                left += 1
                right -= 1
    return res