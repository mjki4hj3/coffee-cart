import csv


class Database:
    def __init__(self, database_filename):
        self.database_filename = database_filename
        self.db_data = []

    def load_db(self):
        with open(self.database_filename, 'r') as csv_file:
            csv_dict = csv.DictReader(csv_file)
            for row in csv_dict:
                self.db_data.append(row)

        return self.db_data  # returns list of dictionaries

    def write_db(self, dictionary):
        with open(self.database_filename, 'w', newline='\n') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)

            writer.writeheader()
            writer.writerow(dictionary)

    def read_db(self):
        with open(self.database_filename, 'r') as csv_file:
            csv_dict = csv.DictReader(csv_file)
            for line in csv_dict:
                print(str(line) + '\n')

    def add_id(self):
        data = self.db_data
        data[-1]['id'] = str(int(data[-1]['id']) + 1)
        print(data[-1]['id'])

    def fieldnames(self):
        field_names = []
        with open(self.database_filename, 'r') as csv_file:
            reader = csv.reader(csv_file)  # list
            field_names = next(reader)
        return field_names

    def print_fieldnames(self):
        field_names = self.fieldnames()
        for key, field_name in enumerate(field_names):
            print(f"{key}: {field_name}")

    def update(self, id):
        data = self.load_db()  # list of dictionaries
