def zeroSumSubarray(nums):
    if len(nums)==1 and 0 not in nums:
        return False
    
    for i in range(len(nums)):
        start = i
        while start < len(nums):
            if sum(nums[i: start+1]) == 0:
                return True
            start += 1
    return False