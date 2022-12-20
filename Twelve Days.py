def recite(start_verse, end_verse):
    result = []
    numbers = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]
    gifts = ["a Partridge in a Pear Tree.", "two Turtle Doves, ", "three French Hens, ", "four Calling Birds, ", "five Gold Rings, ", "six Geese-a-Laying, ", "seven Swans-a-Swimming, ", "eight Maids-a-Milking, ", "nine Ladies Dancing, ", "ten Lords-a-Leaping, ", "eleven Pipers Piping, ", "twelve Drummers Drumming, "]
    str_gift = gifts[0]
    for i in range(end_verse):
        str_num = f"On the {numbers[i]} day of Christmas my true love gave to me: "
        if i > 1:
            str_gift = gifts[i] + str_gift
        if i == 1:
            str_gift = gifts[i] + "and " + str_gift
        result.append(str_num + str_gift)
    return result[start_verse - 1:]
