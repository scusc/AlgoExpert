def longestPeak(array):
    longestPeakLength = 0
    for i in range(1, len(array)-1):
        if array[i-1] < array[i] > array[i+1]:
            leftIndex = i-2
            while leftIndex >= 0 and array[leftIndex] < array[leftIndex+1]:
                leftIndex -= 1
            rightIndex = i+2
            while rightIndex < len(array) and array[rightIndex] < array[rightIndex-1]:
                rightIndex -= 1
            currentPeakLength = rightIndex - leftIndex - 1
            longestPeakLength = max(longestPeakLength, currentPeakLength)
    return longestPeakLength