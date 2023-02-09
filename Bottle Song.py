def recite(start, take=1):
    number_upper = {
        10: "Ten",
        9: "Nine",
        8: "Eight",
        7: "Seven",
        6: "Six",
        5: "Five",
        4: "Four",
        3: "Three",
        2: "Two",
        1: "One"
    }
    number_lower = {
        10: "ten",
        9: "nine",
        8: "eight",
        7: "seven",
        6: "six",
        5: "five",
        4: "four",
        3: "three",
        2: "two",
        1: "one",
        0: "no"
    }
    res_lst = []
    for _ in range(take):
        if start == 2:
            res_lst += [f"{number_upper[start]} green bottles hanging on the wall,",
                f"{number_upper[start]} green bottles hanging on the wall,",
                "And if one green bottle should accidentally fall,",
                f"There'll be {number_lower[start - 1]} green bottle hanging on the wall.",""]
            start -= 1
            continue
        if start == 1:
            res_lst += [f"{number_upper[start]} green bottle hanging on the wall,",
                f"{number_upper[start]} green bottle hanging on the wall,",
                "And if one green bottle should accidentally fall,",
                f"There'll be {number_lower[start - 1]} green bottles hanging on the wall.",""]
            start -= 1
            continue
        res_lst += [f"{number_upper[start]} green bottles hanging on the wall,",
            f"{number_upper[start]} green bottles hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            f"There'll be {number_lower[start - 1]} green bottles hanging on the wall.",""]
        start -= 1
    res_lst.pop()
    return res_lst
