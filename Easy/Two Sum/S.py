# So the good approach needs to be solved in O(n),
# Meaning, we will have to do it in a single iteration over the array
# Meaning, we will need to store the values in a hashSet

def twoSum(nums, target):
    seen = {}
    for i in nums:
        if(target - i in seen):
            return [seen[target - i], i]
        else:
            seen.add(i)
    return []
