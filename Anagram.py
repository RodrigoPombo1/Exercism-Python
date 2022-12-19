def find_anagrams(word, candidates):
    result = []
    word = word.lower()
    for candidate in candidates:
        if candidate.lower() == word.lower():
            continue
        if len(candidate) != len(word):
            continue
        is_anagram = True
        candidate2 = candidate.lower()
        word2 = word
        for char in candidate2:
            if char not in word2:
                is_anagram = False
                break
            for i in range(len(word2)):
                if char == word2[i]:
                    if i == len(word2) - 1:
                        word2 = word2[:i]
                        break
                    word2 = word2[:i] + word2[i + 1:]
                    break
        if is_anagram == True:
            result.append(candidate)
    return result
