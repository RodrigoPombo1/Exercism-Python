def is_pangram(sentence):
    return 26 == len(set(filter(lambda x: True if x.isalpha() else False, sentence.lower())))
