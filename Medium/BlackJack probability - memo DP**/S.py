def getProbabilityOfBust(currentHand, target, memory):
    if currentHand in memory.keys():
        return memory[currentHand]
    if currentHand > target:
        return 1
    if currentHand + 4 >= target:
        return 0

    totalProbabilityOfBust = 0
    for drawnCard in range(1, 11): 
        totalProbabilityOfBust += 0.1*getProbabilityOfBust(currentHand + drawnCard, target, memory)
    
    memory[currentHand] = totalProbabilityOfBust
    return totalProbabilityOfBust


def blackjackProbability(target, startingHand):
    memory = {}
    return round(getProbabilityOfBust(startingHand, target, memory), 3)