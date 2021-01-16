from coffee import *

DB_GLOBAL = 'database.txt'

# read database


def read_db():
    try:
        fhand = open(DB_GLOBAL)
        for line in fhand:
            print(line)
    except:
        print('Following file cannot be opened: ', fhand)
        exit()
    return fhand


# line checker


def no_lines():
    file = open(DB_GLOBAL, 'r')
    count = 0
    for line in file:
        count += 1
    return count


# enumerate database


def enumerate_product(name):
    len = no_lines()
    enumerated_product = list(enumerate(name.split(), len))
    return enumerated_product

# writing to database


def new_product():
    file = open(DB_GLOBAL, 'a+')
    print("So you would like to add a new product ey, let's see... \n")
    try:
        product_name = str(input(
            "What coffee type would you like to add to the database?: "))
    except:
        print("Oops something went wrong, please enter a string only: ")

    # c = Coffee(name)  # new instance of the coffee class

    new_product = enumerate_product(product_name)

    for count, item in new_product:

        file.write("{:3d}) {}".format(count, item) + '\n')

    file.close()
    return product_name
