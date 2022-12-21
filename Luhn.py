class Luhn:
    def __init__(self, card_num):
        card_num = list(card_num)
        while " " in card_num:
            card_num.remove(" ")
        self.card_num = "".join(card_num)
            
    def valid(self):
        if not self.card_num.isnumeric() or self.card_num == "0":
            return False
        card_num = list(self.card_num)
        for i in range(-2, -len(card_num) - 1, -2):
            aux = int(card_num[i])*2
            if aux > 9:
                card_num[i] = str(aux - 9)
                continue
            card_num[i] = aux
        if sum(map(lambda x: int(x), card_num)) % 10 != 0:
            return False
        return True
