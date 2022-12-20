def slices(series, length):
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if length == 0:
        raise ValueError("slice length cannot be zero")
    len_series = len(series)
    if len_series == 0:
        raise ValueError("series cannot be empty")
    if len_series < length:
        raise ValueError("slice length cannot be greater than series length")
    result = []
    for i in range(len_series - length + 1):
        result.append(series[i:length + i])
    return result
