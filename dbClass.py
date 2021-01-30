import csv


class Database:
    def __init__(self, database_filename):
        self.db = database_filename

    def read_db(self):
        with open(self.db, 'r') as csv_file:
            csv_dict = csv.DictReader(csv_file)
            for line in csv_dict:
                print(str(line) + '\n')

    def fieldnames(self):
        field_names = []
        with open(self.db, 'r') as csv_file:
            reader = csv.reader(csv_file)
            field_names = next(reader)

        return field_names

    def print_fieldnames(self, field_names):

        for key, field_name in enumerate(field_names):
            print(f"{key}: {field_name}")

    def update(self):
        return "under construction"
