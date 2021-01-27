def menu_dict():
    return {
        0: 'main_menu',
        1: 'show_products',
    }


while True:
    user_input = input("Pick 1 or 0: ")

    if user_input == '0':
        dictionary = menu_dict()
        print(dictionary[int(user_input)])
    elif user_input == '1':
        dictionary = menu_dict()
        print(dictionary[int(user_input)])
