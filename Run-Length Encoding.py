def decode(string):
    store_num = ""
    result = ""
    for char in string:
        if char.isalpha():
            if store_num == "":
                result += char
                continue
            result += char * int(store_num)
            store_num = ""
            continue
        if char.isnumeric():
            store_num += char
            continue
        if store_num == "":
            result += char
            continue
        result += char * int(store_num)
        store_num = ""
    return result


def encode(string):
    if string == "":
        return string
    previous_char = string[0]
    number_of_appearances = 0
    result = ""
    for char in string:
        if char != previous_char:
            if number_of_appearances == 1:
                result += previous_char
                previous_char = char
                continue
            result += str(number_of_appearances) + previous_char
            number_of_appearances = 1
            previous_char = char
            continue
        number_of_appearances += 1
    if number_of_appearances == 1:
        return result + char
    return result + str(number_of_appearances) + char
