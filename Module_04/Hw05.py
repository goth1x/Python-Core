def lookup_key(data, value):
    key_list = []
    for key, item in data.items():
        if value == item:
            key_list.append(key)
    return key_list

print(lookup_key({'key1': 1, 'key2': 2, 'key3': 3, 'key4': 2}, 2))