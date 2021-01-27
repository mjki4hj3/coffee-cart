import os
from time import sleep
from menu import *
import csv


class MiniProject:
    def __init__(self, project="MiniProject"):
        self.project = project  # Look into this further at somepoint

    def clear(self):
        sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

    def options(self):
        main_menu()
        user_input = input("Type here: ")
        while True:
            if user_input == '0':
                self.clear()
                print("Goodbye, please come again")
                sleep(2)
                self.clear()
                exit()
            elif user_input == '1':
                self.clear()
                options_menu()
                self.menu()
            else:
                print("Oops looks like you did not enter one of the options")
                break

    def read_db(self, db):
        with open(db, 'r') as csv_file:
            reader = csv.DictReader(csv_file)

            for line in reader:
                print(line)

    def add_to_db(self):
        return "under construction"

    def update_db(self):
        return "under construction"


# Main
if __name__ == "__main__":
    main = MiniProject()  # Initialize programme
    while True:
        main.options()
