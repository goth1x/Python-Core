def format_ingredients1(items):
    ingredients = ''
    if len(items) == 1:
        return f'{items[0]}'
    elif len(items) == 2:
        return f'{items[0]} and {items[1]}'
    elif len(items) > 2:
        for i in range(len(items) - 2):
            ingredients += f'{items[i]}, '
        ingredients += f'{items[-2]} and {items[-1]}'
    return ingredients


def format_ingredients2(items):
    list = ''
    if len(items) > 1:
        return ', '.join(items[0:-1]) + ' and ' + items[-1]
    elif len(items) == 1: 
        list = items[0]
    return list 

a = ["2", "1", "3", "4", "3", "4"]
b = ["2", "1"]
c = ["2"]
d = []
print(format_ingredients1(a))
print(format_ingredients2(a))
print(format_ingredients1(b))
print(format_ingredients2(b))
print(format_ingredients1(c))
print(format_ingredients2(c))
print(format_ingredients1(d))
print(format_ingredients2(d))