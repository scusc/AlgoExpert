def generateDocument(characters, document):
    charMap = {}
    for i in characters:
        if i not in list(charMap.keys()):
            charMap[i] = 1
        else:
            charMap[i]+=1
    
    for i in document:
        if i in list(charMap.keys()) and charMap[i] > 0:
            charMap[i] -= 1
            continue
        else: return False
    return True