def count_words(sentence):
    res_dict = {}
    sentence = sentence.lower()
    sentence = sentence.strip("'")
    sentence = sentence.split()
    counter = 0
    while counter < len(sentence):
        if sentence[counter].isalnum() and "," not in sentence[counter]:
            counter += 1
            continue
        if "\n" in sentence[counter]:
            sentence = sentence[:counter] + sentence[counter].split("\n") + sentence[counter + 1:]
        if "\t" in sentence[counter]:
            sentence = sentence[:counter] + sentence[counter].split("\t") + sentence[counter + 1:]
        if "," in sentence[counter]:
            sentence = sentence[:counter] + sentence[counter].split(",") + sentence[counter + 1:]
        if "." in sentence[counter]:
            sentence = sentence[:counter] + sentence[counter].split(".") + sentence[counter + 1:]
        if "_" in sentence[counter]:
            sentence = sentence[:counter] + sentence[counter].split("_") + sentence[counter + 1:]
        if "&" in sentence[counter]:
            sentence = sentence[:counter] + sentence[counter].split("&") + sentence[counter + 1:]
        if "!" in sentence[counter]:
            sentence = sentence[:counter] + sentence[counter].split("!") + sentence[counter + 1:]
        if "@" in sentence[counter]:
            sentence = sentence[:counter] + sentence[counter].split("@") + sentence[counter + 1:]
        if "%" in sentence[counter]:
            sentence = sentence[:counter] + sentence[counter].split("%") + sentence[counter + 1:]
        if "^" in sentence[counter]:
            sentence = sentence[:counter] + sentence[counter].split("^") + sentence[counter + 1:]
        if "$" in sentence[counter]:
            sentence = sentence[:counter] + sentence[counter].split("$") + sentence[counter + 1:]
        if ":" in sentence[counter]:
            sentence = sentence[:counter] + sentence[counter].split(":") + sentence[counter + 1:]
        sentence[counter] = sentence[counter].strip("'")
        counter += 1
        
    for word in sentence:
        if word != "":
            if word not in res_dict.keys():
                res_dict[word] = 1
                continue
            res_dict[word] += 1
    return res_dict
