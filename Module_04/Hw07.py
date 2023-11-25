points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    length = 0
    if len(coordinates) > 1:
        for i in range(1, len(coordinates)):
            pair = tuple(sorted([coordinates[i], coordinates[i-1]]))
            length += points.get(pair)
    return length


print(calculate_distance([1, 3, 2, 0]))
