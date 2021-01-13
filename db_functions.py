from coffee import *

DB_GLOBAL = 'database.txt'

# read database


def read_db():
    try:
        fhand = open(DB_GLOBAL)
    except:
        print('Following file cannot be opened: ', fhand)
        exit()
    return fhand

# line checker


def no_lines():
    fhand = read_db
    count = 0
    for line in fhand:
        count += 1
        print('Line count: ', count)

# writing to database


def new_product():
    fout = open(DB_GLOBAL, 'w')

    name = input(
        "What coffee type would you like to add to the database?: ")
    if not name.isalpha():  # checks if the name entered is a string only
        print("Oops something went wrong, please enter a string only: ")
        new_product()

    price = float(input("What is the price/unit?: "))

    # docs - https://docs.python.org/3/library/functions.html#isinstance
    if not isinstance(price, float):
        print("Oops something went wrong, please enter a string only: ")
        new_product()  # I wonder if we can get it to restart by asking what the price is rather than starting it all ove again

    c = Coffee(name, price)  # new instance of the coffee class

    fout.write(c.name, c.price)
    fout.close()  # close that file boii


new_product()
