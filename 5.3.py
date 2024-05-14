from faker import Faker

class BaseContact:
    def __init__(self, name, surname, phone, mail):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.mail = mail
        self.__label_length = len(self.name) + len(self.surname)

    def __str__(self):
        return f'{self.name} {self.surname}'
    
    def contact(self):
        return f'Wybieram numer {self.phone} i dzwonię do {self.name}'
    
    @property
    def label_length(self):
        return self.__label_length


class BusinessContact(BaseContact):
    def __init__(self, position, company, company_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        self.company_phone = company_phone

    def contact(self):
        return f'Wybieram numer {self.company_phone} i dzwonię do {self.name}'

def create_contact(id_type, amount):
    ids_list = []
    fake_data = Faker()
    if id_type == 1:
        for i in range(amount):
            fake_data_list = [fake_data.name().split(' ')[0], fake_data.name().split(' ')[1], fake_data.phone_number(), fake_data.email()]
            fake_inf = BaseContact(*fake_data_list)
            ids_list.append(fake_inf)

            
    elif id_type == 2:
        for i in range(amount):
            fake_data_list = [fake_data.job(), fake_data.company(), fake_data.phone_number(), fake_data.name().split(' ')[0], fake_data.name().split(' ')[1], fake_data.phone_number(), fake_data.email()]
            fake_inf = BusinessContact(*fake_data_list)
            ids_list.append(fake_inf)
    return ids_list



if __name__ == "__main__":
    cards_type = int(input('Podaj rodzaj wizytówki: \n 1: base \n 2: business \n'))
    cards_amount = int(input('Podaj liczbę wizytówek: '))
    contacts = create_contact(cards_type, cards_amount)
    for contact in contacts:
        print(contact)
        print(contact.contact())
        print(contact.label_length)
