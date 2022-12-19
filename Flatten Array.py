def flatten(iterable):
    if iterable == None:
        return
    result = []
    for element in iterable:
        if element == []:
            return
        if type(element) == list:
            element = flatten(element)
            if element != None:
                result += element
            continue
        if element != None:
            result += [element]
    return result
