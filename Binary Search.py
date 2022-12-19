def find(search_list, value):
    length = len(search_list)
    if length == 0:
        raise ValueError("value not in array")        
    search_pos = length // 2
    search_res = search_list[search_pos]
    if search_res == value:
        return search_pos
    if length == 1:
        raise ValueError("value not in array")
    if search_res < value:
        return search_pos + 1 + find(search_list[length // 2 + 1:], value)
    if search_res > value:
        return find(search_list[:length // 2], value)
