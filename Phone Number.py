class PhoneNumber:
    def __init__(self, number):
        number_lst = list(number)
        for char in ["(", ")", ".", "-", " ", "+"]:
            while char in number_lst:
                number_lst.remove(char)
        length = len(number_lst)
        number = "".join(number_lst)
        if length < 10:
            raise ValueError("incorrect number of digits")
        if length > 11:
            raise ValueError("more than 11 digits")
        if length == 11:
            if number[0] != "1":
                raise ValueError("11 digits must start with 1")
            number = number[1:]
            number_lst = number_lst[1:]
        for char in number:
            if char.isnumeric():
                continue
            if char.isalpha():
                raise ValueError("letters not permitted")
            if not char.isalnum():
                raise ValueError("punctuations not permitted")
        if number[0] == "0":
            raise ValueError("area code cannot start with zero")
        if number[0] == "1":
            raise ValueError("area code cannot start with one")
        if number[3] == "0":
            raise ValueError("exchange code cannot start with zero")
        if number[3] == "1":
            raise ValueError("exchange code cannot start with one")
        self.number = number
        self.area_code = self.number[:3]
    def pretty(self):
        return f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:10]}"
