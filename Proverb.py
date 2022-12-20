def proverb(*lst, qualifier):
    result = []
    if len(lst) > 1:
        for counter, element in enumerate(lst[:-1]):
            result.append(f"For want of a {element} the {lst[counter + 1]} was lost.")
    if len(lst) != 0 and qualifier != None:
        result.append(f"And all for the want of a {qualifier} {lst[0]}.")
    elif len(lst) != 0:
        result.append(f"And all for the want of a {lst[0]}.")
    return result
