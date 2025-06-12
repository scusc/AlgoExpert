def firstNonRepeatingCharacter(string):
    resmap = {}
    for inx, i in enumerate(string):
        if i not in list(resmap.keys()):
            resmap[i] = {'count': 1, 'index': inx}
        else:
            resmap[i]['count'] += 1
    
    fils = list(filter(lambda x: x[1]['count']==1, resmap.items()))

    return fils[0][1]['index'] if len(fils) else -1