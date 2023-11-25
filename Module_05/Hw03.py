"""
Ваша компания проводит маркетинговые кампании с помощью SMS рассылок. Автоматический сбор 
телефонных номеров с базы данных формирует определенный список. Но клиенты оставляют 
свои номера в произвольном виде:

    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",

Сервис рассылок прекрасно понимает и может отправить SMS-ку клиенту, только если телефонный 
номер содержит цифры. Необходимо реализовать функцию sanitize_phone_number, которая будет 
принимать строку с телефонным номером и нормализовать его, т.е. будет убирать 
символы (, -, ), + и пробелы.
"""
import time

t0 = time.time()
n = 10000

def sanitize_phone_number1(phone):
    return ''.join(''.join(''.join(''.join(''.join(phone.split('-')).split('+')).split(')')).split('(')).split(' '))


print(sanitize_phone_number1("  +38050 111-2 211   "))


def sanitize_phone_number2(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone

print(sanitize_phone_number2("  +38050 111-2 211   "))


def sanitize_phone_number3(phone):
    new_phone = phone.translate({ord('('): None, ord(')'): None, ord('+'): None, ord(' '): None, ord('-'): None})
    return new_phone

print(sanitize_phone_number3("  +38050 111-2 211   "))