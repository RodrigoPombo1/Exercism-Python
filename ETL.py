def transform(legacy_data):
    result = {}
    for key, value_lst in legacy_data.items():
        for value in value_lst:
            result[value.lower()] = key
    return result
