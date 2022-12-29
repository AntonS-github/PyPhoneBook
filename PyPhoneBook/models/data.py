"""
Database layer - Repository Class
"""
from models.contact import Contact
from utils.utils import WriterReaderCSV



class ContactsRepo:
    def __init__(self):
        self.contacts_base = []

    def add_contact(self, last_name, first_name, phone_numbers):
        self.contacts_base = WriterReaderCSV.load_from_file()
        contact = {'last_name': last_name, 'first_name': first_name, 'phone_numbers': phone_numbers}
        self.contacts_base.append(contact)
        WriterReaderCSV.store_to_file(self.contacts_base)
        WriterReaderCSV.store_to_file(contact)

    def get_contact(self, elem):
        for contact in self.contacts_base:
            for val in contact.values():
                if val == elem:
                    return contact
            raise Exception("Requested person not found")

    def get_all(self):
        self.contacts_base = WriterReaderCSV.load_from_file()
        return self.contacts_base

    def remove_contact(self, elem):
        flag = True
        for contact in self.contacts_base:
            for val in contact.values():
                if val == elem:
                    flag = False
                    self.contacts_base.remove(contact)
        if flag:
            raise Exception("Requested person not found")

    def update_contact(self, old_contact, new_contact):
        self.remove_contact(old_contact)
        self.add_contact(new_contact[0], new_contact[1], new_contact[2])

    # def add_phone(self, phone_number):
    #     self.phone_numbers.append(phone_number)
    #
    # def remove_phone(self, phone_number):
    #     for p in self.phone_numbers:
    #         if p == phone_number:
    #             self.phone_numbers.remove(p)
    #             return
    # #     raise Exception('Phone number is not found')
    #
    # def __str__(self):
    #     return f'last name: {self.last_name}\nfirst name: {self.first_name}\nphone numbers: {self.phone_numbers}'
