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
        fieldnames = self.fieldnames()
        with open(self.database_filename, 'w', newline='\n') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(dictionary)

    def append_db(self, dictionary):
        fieldnames = self.fieldnames()
        with open(self.database_filename, 'a+', newline='\n') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow(dictionary)

    def read_db(self):
        with open(self.database_filename, 'r') as csv_file:
            csv_dict = csv.DictReader(csv_file)
            for line in csv_dict:
                print(str(line) + '\n')

    def add_id(self, dictionary):
        last_id = int(self.load_db()[-1]['id'])
        dictionary['id'] = last_id + 1
        return dictionary

    def reset_id(self, dictionary):
        counter = 0
        for row in dictionary:
            dictionary[counter]['id'] = counter
            counter += 1

        return dictionary

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

    def create(self, dictionary):
        updated_dictionary = self.add_id(dictionary)
        self.append_db(updated_dictionary)
        print("\n Updated database: ")
        self.read_db()

    def update(self, dictionary):
        self.write_db(dictionary)
        print("\n Updated database: ")
        self.read_db()

    def delete(self, dictionary):
        updated_dictionary = self.reset_id(dictionary)
        self.write_db(updated_dictionary)
        print("\n Updated database: ")
        self.read_db()
