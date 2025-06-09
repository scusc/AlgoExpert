def productSum(array, dep=1):
    return dep*(sum(productSum(i, dep+1) if type(i) is list else i for i in array))