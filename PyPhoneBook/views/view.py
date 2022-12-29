"""
команды из консоли
"""

from models.contact import Contact
from models.service import PhoneBookService
import sys


class ConsoleView:
    def __init__(self, service):
        self.service = service

    def add_contact(self, last_name, first_name, phone_numbers):
        # contact = Contact(last_name, first_name, phone_numbers)
        self.service.add_contact(last_name, first_name, phone_numbers)
        print('Contact added')

    def get_contact(self, elem):
        contact = self.service.get_contact(elem)
        if contact is None:
            print('Contact not found')
        else:
            print(contact)

    def get_all(self):
        contacts = self.service.get_all()
        print(contacts)

    def remove_contact(self, elem):
        self.service.remove_contact(elem)

    def update_contact(self, old_contact, new_contact):
        self.service.update_contact(old_contact, new_contact)

    def run(self):
        while True:
            print("1. Add new contact")
            print("2. Get contact")
            print("3. Get all contacts")
            print("4. Remove contact")
            print("5. Update contact")
            print("6. Exit the program")
            print("Enter your choice: ", end="")
            choice = int(input())
            if choice == 1:
                last_name = str(input('Enter last name: '))
                first_name = str(input('Enter first name: '))
                phone_numbers = list(input('Enter phone number(s) (comma sep): '))
                self.add_contact(last_name, first_name, phone_numbers)
            elif choice == 2:
                search = str(input('Enter lastname or firstname of the contact for searching: '))
                self.get_contact(search)
            elif choice == 3:
                self.get_all()
            elif choice == 4:
                delete = str(input('Enter lastname or firstname of the contact for deleting: '))
                self.remove_contact(delete)
            elif choice == 5:
                old_contact = str(input('Enter lastname or firstname of the contact for update: '))
                self.remove_contact(old_contact)
                last_name = str(input('Enter last name: '))
                first_name = str(input('Enter first name: '))
                phone_numbers = list(input('Enter phone number(s) (comma sep): '))
                self.add_contact(last_name, first_name, phone_numbers)
            elif choice == 6:
                sys.exit('Exit program. Good bye!')
