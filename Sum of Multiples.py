def sum_of_multiples(limit, multiples):
    if multiples == [0]:
        return 0
    try:
        multiples.remove(0)
    except:
        pass
    return sum(set(i for i in range(limit) for multiple in multiples if i % multiple == 0))
