def missingNumbers(nums):
    res = []
    for i in range(1, len(nums)+3):
        if i not in nums:
            res.append(i)
    return res