import os
from time import sleep
from menus import *
from dbClass import Database


class MiniProject:
    def __init__(self, project="MiniProject"):
        # do i have to have more than argument for the constructor function
        self.project = project

    def clear(self):
        sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

    def prompt(self, prompt_text=""):
        user_input = input(f"{prompt_text}: ")
        return user_input.strip()

    def options(self):
        main_menu()
        user_input = self.prompt("Type here: ")
        while True:
            if user_input == '0':
                # self.clear()
                print("Goodbye, please come again")
                sleep(1)
                # self.clear()
                exit()
            elif user_input == '1':
                # self.clear()
                self.menu()
            else:
                print("Oops looks like you did not enter one of the options")
                break

    def menu(self):
        options_menu()
        user_input = self.prompt("Please select a menu option")

        while True:
            if user_input == '0':  # return to main menu
                # self.clear()
                print("Returning to main menu")
                # self.clear()
                self.options()
                break
            elif user_input == '1':  # show products
                # self.clear()
                db = self.db_selection()
                db.read_db()
                exit()

            elif user_input == '2':  # create new product
                db = self.db_selection()
                db.print_fieldnames()
                exit()

            elif user_input == '3':  # update database
                db = self.db_selection()
                idx = self.update_id_request(db)
                updated_dictionary = self.update_input(db, idx)

                db.update(updated_dictionary)
                exit()

            elif user_input == '4':
                db = self.db_selection()
                db.delete()
                exit()
            else:
                self.menu()
                break

    def db_selection(self):
        database_filename = ''

        # returns the files in the database directory as a list
        databases = os.listdir('./DB')

        for key, database in enumerate(databases):
            database = database.replace(".csv", "")
            print(f"{key}: {database}")

        user_input = self.prompt(
            "Please choose a database to update from the above databases by inputing its associated number")

        valid_input = list(range(len(databases)))

        if int(user_input) in valid_input:
            database_filename = databases[int(user_input)]
        else:
            print(
                "\n Oops, looks like you did not enter a valid option, please try again \n")
            self.db_selection()

        db = Database('DB/' + database_filename)
        return db

    def update_id_request(self, db):
        # self.clear()
        db.read_db()
        try:
            user_input = int(self.prompt(
                "Please select an id to choose what database item you wish to update"))
        except ValueError:
            self.clear()
            print("Oops it looks like you did not enter an integer, please try again")
            self.update_id_request(db)
        return user_input

    def update_input(self, db, index):
        database_items = db.load_db()  # list of dicitionaries
        print("Press enter to skip updating that item")
        field_names = db.fieldnames()

        for key in field_names[1:]:  # removes id from list
            user_input = input(f"{key}: ")

            if user_input == "":
                continue
            else:
                database_items[index][key] = user_input
        return database_items


# Main
if __name__ == "__main__":
    main = MiniProject()  # Initialize programme
    while True:
        main.options()
