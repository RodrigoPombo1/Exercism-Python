def abbreviate(words):
    words = words.split()
    aux = []
    for word in words:
        aux2 = word.split("-")
        for i in range(len(aux2)):
            if aux2[i] != "":
                aux.append(aux2[i])
    result = ""
    for word in aux:
        result += word.strip("_")[0].upper()
    return result
