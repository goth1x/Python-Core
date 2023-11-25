def split_list(grade):
    lowgrade = []
    highgrade = []
    if len(grade) > 0:
        mediana = sum(grade) / len(grade)
        for element in grade:
            if element <= mediana:
                lowgrade.append(element)
            else:
                highgrade.append(element)
    return lowgrade, highgrade


print(split_list([1, 2, 5, 8, 12, 4, 2, 4]))
