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
    __________________________________
    |PRODUCT MENU                     |
    |_________________________________|
    |RETURN TO MAIN MENU............|0|
    |SHOW ITEMS IN DATABASE.........|1|
    |CREATE NEW ITEM IN DATABASE....|2|
    |UPDATE ITEM IN DATABASE........|3|
    |DELETE ITEM IN DATABASE........|4|
    |_________________________________|
        ''')


def menu_dict():
    return {
        0: main_menu,
        1: show_products,
        2: create_product,
        3: update_product,
        4: delete_product,
    }
