"""
Есть список contacts, элементы которого — словари контактов следующего вида:

    {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}
Словарь содержит имя пользователя, его email, телефонный номер и свойство — 
избранный контакт или нет.

Создайте функцию get_favorites(contacts), которая будет возвращать список, 
содержащий только избранные контакты. Используйте при этом функцию filter, 
чтобы отфильтровать по полю favorite только избранные контакты.

"""

contacts =  [{'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk', 'phone': '(992) 914-3792', 'favorite': False}, {'name': 'Chaim Lewis', 'email': 'dui.in@egetlacus.ca', 'phone': '(294) 840-6685', 'favorite': False}, {'name': 'Kennedy Lane', 'email': 'mattis.Cras@nonenimMauris.net', 'phone': '(542) 451-7038', 'favorite': True}, {'name': 'Wylie Pope', 'email': 'est@utquamvel.net', 'phone': '(692) 802-2949', 'favorite': False}, {'name': 'Cyrus Jackson', 'email': 'nibh@semsempererat.com', 'phone': '(501) 472-5218', 'favorite': True}]


def get_favorites(contacts):
    f_contacts = filter(lambda x: x['favorite'], contacts)
    mailes = map(lambda x: x['email'], f_contacts)
    return list(mailes)


print(get_favorites(contacts))