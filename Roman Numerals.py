def roman(number):
    adict = {
        1: "I",
        5: "V",
        10: "X",
        50: "L",
        100: "C",
        500: "D",
        1000: "M",
    }
    power_10 = 1
    result = ""
    while number > 0:
        current_digit = number % 10
        number = number // 10
        if current_digit == 0:
            pass
        elif current_digit <= 3:
            result = current_digit * adict[power_10] + result
        elif current_digit == 9:
            result = adict.get(power_10) + adict[power_10 * 10] + result
        elif current_digit <= 5:
            result = adict.get(power_10, "I") * abs(current_digit - 5) + adict[5 * power_10] + result
        else:
            result = adict[5 * power_10] + adict.get(power_10, "I") * (current_digit - 5)+ result
        power_10 = power_10 * 10
    return result
