def optimalFreelancing(jobs):
    profits = [0]*7
    jobs.sort(key = lambda job: job['payment'], reverse = True)
    for job in jobs:
        maxDeadline = min(job['deadline'], 7)
        for i in range(maxDeadline-1, -1, -1):
            if profits[i] == 0:
                profits[i] = job['payment']
                break
    return sum(profits)