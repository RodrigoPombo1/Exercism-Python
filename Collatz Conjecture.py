def steps(number):
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    counter = 0
    while number != 1:
        counter += 1
        if not number % 2:
            number = number // 2
            continue
        number = number * 3 + 1
    return counter
