def is_armstrong_number(number):
    return sum((int(x)**len(str(number)) for x in str(number))) == number
