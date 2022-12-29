"""
Handlers to files
"""

import csv
import os.path

from config import PATH

class WriterReaderCSV:

    @staticmethod
    def store_to_file(data_to_csv):
        fieldnames = ['last_name', 'first_name', 'phone_numbers']
        with open('database.csv', 'w', newline='') as database:
            dict_writer = csv.DictWriter(database, fieldnames=fieldnames)
            dict_writer.writeheader()
            dict_writer.writerow(data_to_csv)

    @staticmethod
    def load_from_file():
        database = []
        with open(PATH, newline='') as f:
            data = csv.DictReader(f)
            for row in data:
                database.append(row)
            return database


# data = [{'last_name': 'tt', 'first_name': 'ayyy', 'phone_numbers': '+999'},
#         {'last_name': 'yyy', 'first_name': 'rrr', 'phone_numbers': '00009'}]
#
n = WriterReaderCSV()
# n.store_to_file(data)
#
print(type(n.load_from_file()[0]))