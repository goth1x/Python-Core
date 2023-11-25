def prepare_data(data):
    data.sort()
    data.pop(-1)
    data.pop(0)
    return data


print(prepare_data([15, 20, 13, 2, 1, 22]))
