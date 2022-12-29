"""
Service layer - Business logic
"""
from utils.utils import WriterReaderCSV

class PhoneBookService:

    def __init__(self, repository):
        self.repository = repository

    def add_contact(self, last_name, first_name, phone_numbers):
        self.repository.add_contact(last_name, first_name, phone_numbers)

    def get_contact(self, elem):
        return self.repository.get_contact(elem)

    def get_all(self):
        return self.repository

    def remove_contact(self, elem):
        self.repository.remove_contact(elem)

    def update_contact(self, old_contact, new_contact):
        self.repository.update_contact(old_contact, new_contact)



