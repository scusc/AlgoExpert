def majorityElement(array):
    winner = 0 
    votes = 0
    for val in array:
        if votes == 0 or val == winner:
            votes += 1
            winner = val
        elif val != winner:
            votes -= 1
    return winner