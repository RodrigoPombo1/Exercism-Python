def score(word):
    adict = {
        "".join(["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]): 1,
        "".join(["D", "G"]) :2,
        "".join(["B", "C", "M", "P"  " "]) :3,
        "".join(["F", "H", "V", "W", "Y"]) :4,
        "".join(["K"  " "]) :5,
        "".join(["J", "X"]) :8,
        "".join(["Q", "Z"]) :10,
    }
    result = 0
    for letter in word:
        for lst_keys in adict:
            if letter.lower() in lst_keys.lower():
                result += adict[lst_keys]
                break
    return result
