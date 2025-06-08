def minimumWaitingTime(queries):
    qlen = len(queries)
    if qlen ==1:
        return 0

    min =0 
    queries.sort()
    for i in range(qlen):
        min+sum(queries[:i])
    
    return min