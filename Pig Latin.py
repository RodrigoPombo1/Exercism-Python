def translate_single_word(text):
    vowels = ["a", "e", "i", "o", "u"]
    if text[0] in vowels or text[:2] in ["xr", "yt"]:
        return text + "ay"
    if text[0] not in vowels and text[1:3] == "qu":
            return text[3:] + text[0] + "quay"
    if text[:2] == "qu":
            return text[2:] + "quay"
    for i in range(len(text)):
        if text[i] in vowels or (text[i] == "y" and i > 0):
            return text[i:] + text[:i] + "ay"

def translate(text):
    result = ""
    lst_words = text.split()
    for word in lst_words[:-1]:
        result += translate_single_word(word) + " "
    return result + translate_single_word(lst_words[-1])
