def commands(binary_str):
    rvs = binary_str[::-1]
    result = []
    adict = {
        0: "wink",
        1: "double blink",
        2: "close your eyes",
        3: "jump",

    }
    for i in range(len(rvs) - 1):
        if rvs[i] == "1":
            result.append(adict[i])
    if binary_str[0] == "1":
        result = result[::-1]
    return result
