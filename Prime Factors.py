def factors(value):
    result:list = []
    num:int = 2
    while value > num-1: 
        while not value % num:
            result.append(num)
            value //= num
        num += 1
    return result
