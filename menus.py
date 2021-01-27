def main_menu():
    print('''
    ________________
    |    MAIN MENU   |
    |________________|
    |EXIT APP... | 0 |
    |PRODUCTS... | 1 |
    |___________ | _ |
    ''')


def options_menu():
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


def menu_dict():
    return {
        0: main_menu,
        1: show_products,
        2: create_product,
        3: update_product,
        4: delete_product,
    }
