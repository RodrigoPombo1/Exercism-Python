def rows(letter):
    length = ord(letter) - ord("A")
    result = []
    for i in range(length + 1):
        if i == 0:
            result.append(" " * (length - i) + chr(i+ord("A")) + " " * (length - i))
            continue
        result.append(" " * (length - i) + chr(i+ord("A")) + (2*i-1) * " " + chr(i+ord("A")) + " " * (length - i))
    return result + result[-2::-1]
