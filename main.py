import os
from time import sleep
from menus import *
from dbClass import Database


class MiniProject:
    def __init__(self, project="MiniProject"):
        self.project = project  # Look into this further at somepoint

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
            if user_input == '0':
                # self.clear()
                print("Returning to main menu")
                # self.clear()
                self.options()
                break
            elif user_input == '1':
                # self.clear()
                self.menu()
            elif user_input == '2':
                self.clear()

            elif user_input == '3':
                # self.clear()
                self.db_selection()

            elif user_input == '4':
                # self.clear()
                return "Under Construction"

            else:
                print("Oops looks like you did not enter one of the options")
                break

    def db_selection(self):
        databases = os.listdir('./DB')
        for key, database in enumerate(databases):
            database = database.replace(".csv", "")
            print(f"{key}: {database}")

        user_input = self.prompt(
            "Please choose a database to update from the above databases by inputing its associated number")

        while True:
            if user_input == '0':
                database_filename = databases[int(user_input)]
                break
            elif user_input == '1':
                database_filename = databases[int(user_input)]
                break
            else:
                print(
                    "Oops, looks like you did not enter a valid option, please try again")
                sleep(1)

        return database_filename

    def db_load(self):  # think of a better name than this

        database_filename = self.db_selection()
        db = Database(database_filename)


# Main
if __name__ == "__main__":
    main = MiniProject()  # Initialize programme
    while True:
        main.options()
