def prime(number):
    if number == 0:
        raise ValueError("there is no zeroth prime")
    counter = 1
    number_of_primes_found = 0
    while number_of_primes_found < number:
        counter += 1
        is_prime = True
        for i in range(2, counter // 2 + 1):
            if counter % i == 0:
                is_prime = False
                break
        if is_prime == True:
            number_of_primes_found += 1
    return counter
