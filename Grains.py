def square(number):
    if not(0 < number <= 64):
        raise ValueError("square must be between 1 and 64")
    return 2**(number-1)


def total():
    return sum([square(x) for x in range(1, 65)])
