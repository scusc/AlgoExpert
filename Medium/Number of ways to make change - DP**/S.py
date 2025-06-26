def numberOfWaysToMakeChange(n, denoms):
    ways = [1] + [0 for _ in range(n)]
    for denom in denoms:
        for amount in range(1, n+1):
            if denom <=  amount:
                ways[amount] +=  ways[amount - denom]
    return ways[n]