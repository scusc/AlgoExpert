def phoneNumberMnemonics(phoneNumber):
    phoneDict = {
        "0": ["0"],
        "1": ["1"],
        "2": ["a", "b", "c"],
        "3": ["d","e","f"],
        "4": ["g","h","i"],
        "5": ["j","k","l"],
        "6": ["m","n","o"],
        "7": ["p","q","r", "s"],
        "8": ["t","u","v"],
        "9": ["w","x","y", "z"],
    }
    
    res = [""]
    for num in phoneNumber:
        updatedRes = [existing + char for existing in res for char in phoneDict[num]]
        res = updatedRes
    return res