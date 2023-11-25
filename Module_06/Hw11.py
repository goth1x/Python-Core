"""
Реализуйте функцию get_credentials_users(path), которая возвращает 
список строк из бинарного файла, созданного в предыдущей задаче, где:

path - путь к файлу.
Формат файла:

andry:uyro18890D
steve:oppjM13LL9e
Откройте файл для чтения, используя with и режим rb. Сформируйте список
строк из файла и верните его из функции get_credentials_users в 
следующем формате:

['andry:uyro18890D', 'steve:oppjM13LL9e']
Требования:

Используйте менеджер контекста для чтения из файла

"""

path = 'D:\\Projects\Binary.txt'
users_info = {'andry': 'uyro18890D', 'steve': 'oppjM13LL9e'}


def get_credentials_users(path):
    line_list = []
    with open(path, 'rb') as file:
        while True:
            line = file.readline().decode().removesuffix('\n')
            if not line:
                break
            line_list.append(line)
    return line_list


get_credentials_users(path)
