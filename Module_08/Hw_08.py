"""
Есть список IP адресов:

IP = [
    "85.157.172.253",
    ...
]
Реализуйте две функции. Первая get_count_visits_from_ip 
с помощью Counter будет возвращать словарь, где ключ — это IP, 
а значение — количество вхождений в указанный список.

Пример:

{
    '85.157.172.253': 2,
    ...
}
Вторая функция get_frequent_visit_from_ip возвращает кортеж с 
наиболее часто встречаемым в списке IP и количеством его вхождений в список.

Пример:

('66.50.38.43', 4)

"""

from collections import Counter


def get_count_visits_from_ip(ips):
    return dict(Counter(ips))


def get_frequent_visit_from_ip(ips):
    return Counter(ips).most_common(1)[0]


ips = ['1.1.1.1', '192.168.0.1', '192.168.0.2', '192.168.0.1',
       '192.168.0.1', '192.168.0.5', '192.168.0.4']

print(get_count_visits_from_ip(ips))
print(get_frequent_visit_from_ip(ips))
