
def isValidSubsequence(array, sequence):
    seqIndex = 0
    for i in range(len(array)):
        if(seqIndex<len(sequence) and array[i]==sequence[seqIndex]):
            seqIndex+1
    return True if seqIndex == len(sequence) else False