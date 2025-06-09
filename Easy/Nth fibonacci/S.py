def getNthFib(n):
    fib= [0,1,1]
    steps = abs(len(fib) - n)
    if steps > 0:
        for _ in range(steps):
            fib.append(fib[-1] + fib[-2])
    return fib[n-1]