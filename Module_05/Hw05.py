"""

Вернемся к нашей задаче с телефонными номерами. Компания расширяется и вышла на рынок Азии. 
Теперь в списке приходят телефоны разных стран. Каждая страна имеет свой телефонный код .

Компания работает со следующими странами

Страна	Код ISO	Префикс
Japan	JP	+81
Singapore	SG	+65
Taiwan	TW	+886
Ukraine	UA	+380
Чтобы мы могли корректно выполнить маркетинговую SMS кампанию, необходимо выдать для каждой страны свой список телефонных номеров.

Напишите функцию get_phone_numbers_for_сountries, которая будет:

Принимать список телефонных номеров.
Санитизировать (нормализовать) полученный список телефонов клиентов с помощью нашей функции sanitize_phone_number.
Сортировать телефонные номера по указанным в таблице странам.
Возвращать словарь со списками телефонных номеров для каждой страны в следующем виде:
{
    "UA": [<здесь список телефонов>],
    "JP": [<здесь список телефонов>],
    "TW": [<здесь список телефонов>],
    "SG": [<здесь список телефонов>]
}
Если не удалось сопоставить код телефона с известными, этот телефон должен быть добавлен в список словаря с ключом "UA".

"""

def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    dict_phones = {'UA':[],'JP':[],'TW':[],'SG':[]}
    for number in list_phones:
        if sanitize_phone_number(number).startswith('81'):
            dict_phones['JP'].append(sanitize_phone_number(number))
        elif sanitize_phone_number(number).startswith('65'):
            dict_phones['SG'].append(sanitize_phone_number(number))
        elif sanitize_phone_number(number).startswith('886'):
            dict_phones['TW'].append(sanitize_phone_number(number))
        else:
            dict_phones['UA'].append(sanitize_phone_number(number))
    return dict_phones


print(get_phone_numbers_for_countries(['+380505745','6111518','88615874','+818874864','815444477']))