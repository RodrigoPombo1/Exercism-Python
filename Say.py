def say(number):
    adict_10 = {
        1: "thousand",
        3: "million",
        5: "billion",
    }
    if number > 999999999999 or number < 0:
        raise ValueError("input out of range")
    if number == 0:
        return "zero"
    result = []
    while number > 0:
        result.append(number % 1000)
        number = number // 1000
    for key in adict_10.keys():
        if len(result) >= key + 1:
            result.insert(key, adict_10[key])
    result = result[::-1]
    to_remove = []
    for i in range(0,len(result) + 1, 2):
        aux = say_num_999(result[i])
        if aux == "":
            to_remove.append(i)
        result[i] = aux
    for i in range(1, len(to_remove)):
        result.remove(adict_10[to_remove[i] - 3])
    return " ".join(result).strip()

def say_num_999(number):
    adict1 = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }
    adict11 = {
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
    }
    adict10 = {
        10: "ten",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }
    result = []
    aux = number % 100
    if aux in adict11.keys():
        result.append(adict11[aux])
    else:
        if aux % 10 in adict1.keys():
            result.append(adict1[aux % 10])
            if aux - (aux % 10) in adict10.keys():
                result.append(adict10[aux - (aux % 10)] + "-")
                result[-2] = "".join(result[-1] + result[-2])
                result.pop()
        elif aux - (aux % 10) in adict10.keys():
            result.append(adict10[aux - (aux % 10)])
    if (number - aux) // 100 in adict1.keys():
        result.append(adict1[(number - aux) // 100] + " hundred")
    return " ".join(result[::-1])
