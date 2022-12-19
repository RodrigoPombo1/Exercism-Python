def distance(strand_a, strand_b):
    length_a = len(strand_a)
    if length_a != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    result = 0
    for i in range(length_a):
        if strand_a[i] != strand_b[i]:
            result += 1
    return result
