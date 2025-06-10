def findNLargestNumbers(array):
    # for now lets consider 3 largest numbers
    n = 3
    result = [-99999]*n

    for val in array:
        for i in range(n-1, -1, -1): # Start from the end (smallest of top n)
            if val >  result[i]:
                for j in range(0, i): # Shift all smaller elements to left
                    result[j] = result[j+1]
                result[i] = val
                break
    return result