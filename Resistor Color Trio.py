def label(colors):
    adict = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9,
    }
    result = ""
    for color in colors:
        result += str(adict[color])
    result = int(result[:-1]) * 10 ** int(result[-1])
    if result >= 1000:
        return f"{result // 1000} kiloohms"
    return f"{result} ohms"
