def runLengthEncoding(string):
    encodedString = []
    counter = 1
    for i in range(len(string)):
        if i ==len(string)-1 or string[i] != string[i+1] or counter==9:
            encodedString.append(str(counter) + string[i])
            counter = 0
        counter+=1
    return "".join(encodedString)