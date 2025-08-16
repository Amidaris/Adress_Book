from faker import Faker
import random

fake = Faker("pl_PL")


class BaseContact:
    def __init__(self, name, surname, phone_number, mail):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.mail = mail

    def contact(self):
        print(f"Wybieram numer +48 {self.phone_number} i dzwonię do {self.name} {self.surname}.")

    @property
    def label_length(self):
        return len(self.name) + len(self.surname) + 1 # uwzględnienie spacji między imieniem, a nazwiskiem


class BusinessContact(BaseContact):
    def __init__(self, name, surname, phone_number, mail, company, job_position, work_phone):
        super().__init__(name, surname, phone_number, mail)
        self.company = company
        self.job_position = job_position
        self.work_phone = work_phone

    def contact(self):
        print(f"Wybieram numer +48 {self.work_phone} i dzwonię do {self.name} {self.surname}.")

contacts_list = []

def create_contacts(contact_type, quantity):

    for _ in range(quantity):
        name = fake.first_name()
        surname = fake.last_name()
        phone_number = fake.phone_number()
        mail = fake.email()

        if contact_type == BaseContact:
            contact = BaseContact(name, surname, phone_number, mail)
        elif contact_type == BusinessContact:
            company = fake.company()
            job_position = fake.job()
            work_phone = fake.phone_number()
            contact = BusinessContact(name, surname, phone_number, mail, company, job_position, work_phone)
        else:
            raise ValueError("Unknown business card type.")

        contacts_list.append(contact)

    return contacts_list