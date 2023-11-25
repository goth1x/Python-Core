def game(terra, power):
    for list in terra:
        for element in list:
            if power >= element:
                power += element
            else:
                break
    return power
    

terra = [[1, 1, 5, 10], [10, 2], [1, 1, 1]]
power = 1
print(game(terra, power))