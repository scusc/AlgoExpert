def mergeOverlappingIntervals(intervals):
    intervals.sort(key = lambda interval: interval[0])
    res = [intervals[0]]
    for i in range(1, len(intervals)):
        if res[-1][1] < intervals[i][0]:
            res.append([intervals[i][0], intervals[i][1]])
        else:
            res[-1][1] = max(res[-1][1], intervals[i][1])
    return res