import os
from time import sleep
# moved all the helper functions to a separate file for cleaner code - this imports it all in
from functions import *
from db_functions import *


def clr():
    # Clears the terminal - at some point we can use the clear function from the os module
    print("\n"*100)


def invalid():
    print("\n Option not avialable on the menu \n Please try again:")
    print("Returning to product menu...")
    sleep(2)
    return product_menu()


def prompt():
    try:
        output = str(
            input("Would you like to go back to the product menu? (Y/N): "))
    except ValueError:
        print("You did not enter Y or N, please try again")
        prompt()
    if output == ('Y' or 'y'):
        product_menu()
    else:
        print("Goodbye")
        sleep(0.5)
    exit()


def show_products():
    print("Fetching database one moment \n")
    sleep(1)
    display_db()
    prompt()


def create_product():
    product = new_product()
    print("Great you have added {} to the database".format(product))
    sleep(2)
    prompt()


def update_product():
    print("===Under Construction===\n")
    sleep(2)
    clr()
    prompt()


def delete_product():
    print("===Under Construction===\n")
    sleep(2)
    clr()
    prompt()


def exit_app():
    clr()
    print("Goodbye")
    sleep(2)
    clr()
    exit()


def product_menu():
    print('''
 ________________________
|PRODUCT MENU            |
|________________________|
|RETURN TO MAIN MENU...|0|
|SHOW PRODUCTS.........|1|
|CREATE NEW PRODUCT....|2|
|UPDATE PRODUCT........|3|
|DELETE PRODUCT........|4|
|________________________|
    ''')

    def input_reciever(user_input):
        return {
            0: main_menu,
            1: show_products,
            2: create_product,
            3: update_product,
            4: delete_product,
        }.get(user_input, invalid)  # Invalid input is default if user_input is not found

    try:
        user_input = int(input("Type Here: "))
    except ValueError:
        print("Oops looks like you did not enter a integer, Please try again")
        sleep(1)
        product_menu()

    result_function = input_reciever(user_input)  # uncalled function here
    result_function()  # gets called here


def main_menu():
    print('''
 ________________
|    MAIN MENU   |
|________________|
|EXIT APP... | 0 |
|PRODUCTS... | 1 |
|___________ | _ |
    ''')

    try:
        user_input = int(input("Type Here: "))
    except ValueError:
        print("Oops looks like you did not enter a integer, Please try again")
        sleep(1)
        main_menu()

    def input_reciever(user_input):
        return {
            0: exit_app,
            1: product_menu,

        }.get(user_input, invalid)

    result_function = input_reciever(user_input)
    result_function()


clr()
main_menu()
