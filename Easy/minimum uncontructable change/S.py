def nonConstructibleChange(coins):

    if 1 not in coins:
        return 1
    
    coins.sort()
    change=0
    for i in coins:
        if i > change+1:
            return change+1
        else:
            cahnge+=i
    return change+1