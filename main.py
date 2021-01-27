import os
from time import sleep
from menu import *
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
                self.clear()
                print("Goodbye, please come again")
                sleep(1)
                self.clear()
                exit()
            elif user_input == '1':
                self.clear()
                self.menu()
            else:
                print("Oops looks like you did not enter one of the options")
                break

    def menu(self):
        options_menu()
        user_input = self.prompt("Please select a menu option")

        while True:
            if user_input == '0':
                self.clear()
                print("Returning to main menu")
                self.clear()
                self.options()
                break
            elif user_input == '1':
                self.clear()
                self.menu()
            elif user_input == '2':
                self.clear()

            elif user_input == '3':
                self.clear()
                return "Under Construction"

            elif user_input == '4':
                self.clear()
                return "Under Construction"

            else:
                print("Oops looks like you did not enter one of the options")
                break

    def db_activator(self, database_filename):
        db = Database(database_filename)


# Main
if __name__ == "__main__":
    main = MiniProject()  # Initialize programme
    while True:
        main.options()


#
# want to create a function that
#
