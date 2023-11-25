import re

def total_salary(path):
    salary = 0
    file = open(path, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        find = re.search(r"\d+", line)
        salary += float(find.group())
    file.close()
    return salary