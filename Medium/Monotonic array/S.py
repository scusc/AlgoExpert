def isMonotonic(array):
    FLAT = 'flat'
    UP = 'up'
    DOWN = 'down'

    if len(array) <=1:
        return True
    
    direction  = FLAT
    for i in range(len(array)-1):
        left = array[i]
        right = array[i+1]

        if direction is FLAT and left == right:
            continue
        elif direction is FLAT and left < right:
            direction  = UP
        elif direction is FLAT and left > right:
            direction  = DOWN
        elif direction is not FLAT and ((left < right and direction is DOWN) or (left > right and direction is UP)):
            return False
    return True
