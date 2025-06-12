def commonCharacters(strings):
    strings.sort(key = lambda x: len(x))
    tester = strings[0]
    result = []
    for test in tester:
        isThere = True
        if test not in result:
            for i in range(1, len(strings)):
                if test not in strings[i]:
                    isThere = False
                    break
            if isThere:
                result.append(test)

    return result