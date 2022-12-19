def is_isogram(string):
    return len(list(filter(lambda x: True if x.isalpha() else False, string.lower()))) == len(set(filter(lambda x: True if x.isalpha() else False, string.lower())))
