def bestSeat(seats):
    longest = -999
    start = 1
    indices = []
    while start < len(seats):
        if seats[start] == 0:
            end = start
            while end < len(seats) and seats[end]==0:
                end += 1
            length = end - start
            if length > longest:
                indices = [start, end - 1]
                longest = length
        start += 1
    return sum(indices)//2
