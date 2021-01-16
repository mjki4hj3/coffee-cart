from main import product_menu


def prompt():
    input = str(
        input("Would you like to go back to the product menu? (Y/N)"))
    if input == ('Y' or 'y'):
        product_menu()
    else:
        print("Goodbye")
    exit()
