def is_valid(isbn):
    isbn = str(isbn)
    result = 0
    counter = 0
    for digit in isbn:
        if digit.isnumeric():
            result += (10 - counter) * int(digit)
            counter += 1
            continue
        if digit == "X" and counter == 9:
            result += (10 - counter) * 10
            counter += 1
            continue
        if digit != "-" and counter != 9:
            return False
    if counter != 10:
        return False
    return result % 11 == 0
