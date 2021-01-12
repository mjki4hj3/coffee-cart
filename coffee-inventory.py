import os
from time import sleep


def clr():
    # Clears the terminal - at some point we can use the clear function from the os module
    print("\n"*100)


def show_products():
    print("===Under Construction===\n")
    sleep(1)
    clr()
    main_menu()


def create_product():
    print("===Under Construction===\n")
    sleep(2)
    clr()
    main_menu()


def update_product():
    print("===Under Construction===\n")
    sleep(2)
    clr()
    main_menu()


def delete_product():
    print("===Under Construction===\n")
    sleep(2)
    clr()
    main_menu()


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

    def input_checker(user_input):
        return {
            0: main_menu,
            1: show_products,
            2: create_product,
            3: update_product,
            4: delete_product
        }.get(user_input, "===Invalid Input===\n")  # Invalid input is default if user_input is not found

    user_input = int(input("Type Here: "))
    result_function = input_checker(user_input)  # uncalled function here
    result_function()  # gets called here


def main_menu():
    clr()
    print('''
 _____________
| MAIN MENU |
|_____________ |
|EXIT APP... | 0 |
|PRODUCTS... | 1 |
|___________ | _|
    ''')

    def input_checker(user_input):
        return {
            0: exit_app,
            1: product_menu
        }.get(user_input, "===Invalid Input===\n")  # Invalid input is default if user_input is not found

    user_input = int(input("Type Here: "))
    result_function = input_checker(user_input)
    result_function()


clr()
main_menu()
