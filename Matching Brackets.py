def is_paired(input_string):
    open = ["(","{","["]
    close = [")","}","]"]
    result = True
    aux = []
    for char in input_string:
        if char not in open and char not in close:
            continue
        if char in open:
            aux.append(char)
            continue
        if len(aux) > 0:
            if close.index(char) != open.index(aux.pop()):
                result = False
                break
            continue
        result = False
        break    
    return result and len(aux) == 0
