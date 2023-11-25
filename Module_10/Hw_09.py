"""В четвертом модуле мы реализовали функцию lookup_key для поиска всех ключей по значению в словаре. 
Первым параметром в функцию мы передавали словарь, а вторым — значение, которое хотели найти. 
Результатом был список ключей или пустой список, если мы ничего не находили.

def lookup_key(data, value):
    keys = []
    for key in data:
        if data[key] == value:
            keys.append(key)
    return keys
Создайте класс LookUpKeyDict, родителем которого будет класс UserDict. Сделайте функцию lookup_key 
методом класса LookUpKeyDict."""


from collections import UserDict


class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        keys = filter(lambda key: self.data[key]==value in self.data.values(), self.data)

        return list(keys)
    

lookup = LookUpKeyDict({'key1': 1, 'key2': 2, 'key3': 3, 'key4': 2})

print(lookup.lookup_key(2))