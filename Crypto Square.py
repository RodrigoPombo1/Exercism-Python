from math import sqrt

def make_text_square(plaintext, r, c):
    lst_text_square = []
    for i in range(r):
        lst_text_square.append(plaintext[i*c:(i+1)*c])
    if len(lst_text_square[0]) != len(lst_text_square[-1]):
        for i in range(r):
            lst_text_square[i] += " " * (len(lst_text_square[0]) - len(lst_text_square[i]))
    return lst_text_square

def make_text_final(lst_text_square, r, c):
    text_final = ""
    for i in range(c):
        for j in range(r):
            text_final += lst_text_square[j][i]
        if i != c - 1:
            text_final += " "
    return text_final

def cipher_text(plain_text):
    plain_text = plain_text.lower()
    i = 0
    while i <= len(plain_text) - 1:
        if not plain_text[i].isalnum():
            plain_text = plain_text[:i] + plain_text[i+1:]
            if i == len(plain_text):
                break
            continue
        i += 1
    length = len(plain_text)
    if length == 0:
        return ""
    square_root = sqrt(length)
    r = int(square_root)
    if square_root == r:
        lst_text_square = make_text_square(plain_text, r, r)
        return make_text_final(lst_text_square, r, r)
    c = r + 1
    if r * c >= length:
        pass
    else:
        r = r+1
    lst_text_square = make_text_square(plain_text, r, c)
    return make_text_final(lst_text_square, r, c)
