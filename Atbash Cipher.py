plain = "abcdefghijklmnopqrstuvwxyz1234567890"
cipher = "zyxwvutsrqponmlkjihgfedcba1234567890"

def encode(plain_text):
    while " " in plain_text:
        lst_plain_txt = list(plain_text)
        lst_plain_txt.remove(" ")
        plain_text = "".join(lst_plain_txt)
    while "," in plain_text:
        lst_plain_txt = list(plain_text)
        lst_plain_txt.remove(",")
        plain_text = "".join(lst_plain_txt)
    while "." in plain_text:
        lst_plain_txt = list(plain_text)
        lst_plain_txt.remove(".")
        plain_text = "".join(lst_plain_txt)
    return "".join(list(map(lambda x: cipher[plain.index(x[1].lower())] if x[0] % 5 != 0 or x[0] == 0 else " " + cipher[plain.index(x[1].lower())], enumerate(plain_text))))


def decode(ciphered_text):
    while " " in ciphered_text:
        lst_ciphered_txt = list(ciphered_text)
        lst_ciphered_txt.remove(" ")
        ciphered_text = "".join(lst_ciphered_txt)
    return "".join(list(map(lambda x: plain[cipher.index(x.lower())], ciphered_text)))
