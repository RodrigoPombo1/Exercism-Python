def append(list1, list2):
    return list1 + list2


def concat(lists):
    result = []
    for list in lists:
        result += list
    return result


def filter(function, list):
    return [x for x in list if function(x)]


def length(list):
    return len(list)


def map(function, list):
    result = []
    for element in list:
        result.append(function(element))
    return result


def foldl(function, list, initial):
    result = initial
    for i in range(len(list)):
        result = function(result, list[i])
    return result


def foldr(function, list, initial):
    if len(list) == 0:
        return initial    
    result = list[0]
    for i in range(1, len(list)):
        result = function(result, list[i])
    return result + initial
    
def reverse(list):
    return list[::-1]
