"""Продолжаем расширять функциональность класса Contacts. На этом этапе мы добавим 
в класс метод get_contact_by_id. Метод должен искать контакт по уникальному id в 
списке contacts и возвращать словарь из него с указанным ключом id . Если словаря 
с указанным id в списке contacts не найдено, метод возвращает None.

Примечание: для правильного прохождения теста не создавайте экземпляр класса в коде."""

class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        for contact in self.contacts:
            if id in contact.values():
                return contact
        else:
            return
        
new = Contacts()
new.add_contacts("Wylie Pope","(692) 802-2949", "est@utquamvel.net",True)
new.add_contacts("Pope Wylie ","(692) 2949 802", "est@utquamvel.net",False)
print(new.list_contacts())
print(new.get_contact_by_id(3))
