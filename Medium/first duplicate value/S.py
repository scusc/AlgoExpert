def firstDuplicateValue(array):
    seen = []
    for val in array:
        if val not in seen:
            seen.append(val)
        else:
            return val
    return -1