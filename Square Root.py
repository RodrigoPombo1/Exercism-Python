def square_root(number):
    for i in range(number + 1):
        if i * i == number:
            return i

    # return number ** 0.5
