def binarySearch(array, target):
    start = 0
    end = len(array)-1
    while start <= end:
        mid = (start + end)//2
        if target < array[mid]:
            end = mid-1
        elif target > array[mid]:
            start = mid+1
        elif target ==array[mid]:
            return mid
    return -1