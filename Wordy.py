def answer(question):
    
    operations = {
        "minus": lambda x, y: x - y ,
        "plus": lambda x, y: x + y,
        "multiplied": lambda x, y: x * y,
        "divided": lambda x, y: x / y,
    }
    
    question = question.split(" ")[2:-1] + [question.split(" ")[-1][:-1]]
    for _ in range(len(question)):
        if "by" in question:
            question.remove("by")
        else:
            break

    def compute(question):
        length = len(question)
        if length == 1 and question[0].isnumeric():
            return float(question[0])
        if length == 1 and not question[0].isnumeric():
            raise ValueError("syntax error")
        if length == 2:
            if question[1] in operations.keys() or question[1].isnumeric():
                raise ValueError("syntax error")
            raise ValueError("unknown operation")
        if length == 3:
            if question[1].isnumeric():
                raise ValueError("syntax error")
            if question[1] not in operations.keys():
                raise ValueError("unknown operation")
            try:
                return operations[question[1]](float(question[0]), float(question[2]))
            except:
                raise ValueError("syntax error")
        if length > 3:
            return compute([str(compute(question[:3]))] + question[3:])
    return int(compute(question))
