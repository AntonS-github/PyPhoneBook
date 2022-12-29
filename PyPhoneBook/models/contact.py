"""
Persistence layer - Model Class
"""


class Contact:

    def __init__(self, first_name, last_name, phone_numbers):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_numbers = phone_numbers

    def __str__(self):
        return f'last name: {self.last_name}\nfirst name: {self.first_name}\nphone numbers: {self.phone_numbers}'
