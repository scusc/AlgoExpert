def minNumberOfCoinsForChange(n, denoms):
    numOfCoins = [float('inf')]*(n+1)
    numOfCoins[0] = 0
    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                numOfCoins[amount] = min(numOfCoins[amount], numOfCoins[amount - denom]+1)
    return numOfCoins[n] if numOfCoins[n] != float('inf') else -1