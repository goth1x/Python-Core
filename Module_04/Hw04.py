def get_grade(key):
    key_ecst = {'F': 1, 'FX': 2, 'E': 3, 'D': 3, 'C': 4, 'B': 5, 'A': 5}
    return key_ecst.get(key)

def get_description(key):
    key_ecst = {'F': 'Unsatisfactorily', 'FX': 'Unsatisfactorily', 'E': 'Enough',
                'D': 'Satisfactorily', 'C': 'Good', 'B': 'Very good', 'A': 'Perfectly'}
    return key_ecst.get(key)

print(get_grade('A'))
print(get_description('D'))