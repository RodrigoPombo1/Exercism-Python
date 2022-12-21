def transpose(lines):
    lines = lines.split("\n")
    max_len = len(lines[0])
    for line in lines:
        length = len(line)
        if max_len < length:
            max_len = length
    result = ["" for _ in range(max_len)]
    counter = len(lines)
    for line in lines:
        counter -= 1
        length = len(line)
        for i in range(max_len):
            if length <= i:
                if counter != 0:
                    result[i] += " "
                continue
            result[i] += line[i]
    for i in range(max_len - 1, -1, -1):
        if result[i][len(result[i]) - 1] != " ":
            break
        result[i] = result[i].strip() # I forgot rstip() existed
    return "\n".join(result)
