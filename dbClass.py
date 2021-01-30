import csv


class Database:
    def __init__(self, database_filename):
        self.db = database_filename

    def read_db(self):
        with open(self.db, 'r') as csv_file:
            reader = csv.DictReader(csv_file)

            for line in reader:
                print(str(line) + '\n')

    def add_to_db(self):
        return "under construction"

    def update_db(self):
        return "under construction"
