def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    aux = sum([x for x in range(1, number) if not number % x])
    if aux > number:
        return "abundant"
    if aux < number:
        return "deficient"
    return "perfect"
