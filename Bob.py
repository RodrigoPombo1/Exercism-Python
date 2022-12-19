def response(hey_bob):
    if hey_bob.strip() == "":
        return "Fine. Be that way!"
    if hey_bob[-1] == "?" and hey_bob[:-1].isupper():
        return "Calm down, I know what I'm doing!"
    if hey_bob.strip()[-1] == "?":
        return "Sure."
    if hey_bob.isupper():
        return "Whoa, chill out!"
    return "Whatever."
