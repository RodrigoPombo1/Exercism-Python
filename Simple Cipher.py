from random import randint

class Cipher:
    def __init__(self, key=None):
        if key == None:
            self.key = "".join([chr(randint(0, 25) + ord("a")) for _ in range(26)])
        else:
            self.key = key
        

    def encode(self, text):
        if self.key == None:
            self.key = "a" * len(text)
        length_key = len(self.key)
        for i in range(len(text)):
            aux = ord(text[i]) + ord(self.key[i % (length_key)]) - 2*ord("a")
            text = text[:i] + chr(aux % 26 + ord("a")) + text[i + 1:]
        return text

    def decode(self, text):
        if self.key == None:
            self.key = "a" * len(text)
        length_key = len(self.key)
        for i in range(len(text)):
            aux = ord(text[i]) - ord(self.key[i % (length_key)])
            if aux >= 0:
                text = text[:i] + chr(aux + ord("a")) + text[i + 1:]
                continue
            text = text[:i] + chr(aux + ord("z") + 1) + text[i + 1:]
        return text
