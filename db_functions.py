import re
DB_GLOBAL = 'database.txt'

# read database


def read_db():
    try:
        fhand = open(DB_GLOBAL, 'r')
    except:
        print('Following file cannot be opened: {}'.format(fhand))
        exit()
    return fhand


def display_db():
    file = read_db()
    for line in file:
        print(line)

# number of lines in db


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

# updating the database


def update_database():
    file = open(DB_GLOBAL)
    lines = file.readlines()
    old_product = 'Mocha'
    updated_product = 'Hot Chocolate'

    for line in lines:
        if old_product in line:
            # filters out for the id which also doubles as the position number
            position = int(re.sub('\D', '', line))
            break
        else:
            continue
        print("This drink is not in the database")

    lines[position] = "{:3d}) {}".format(position, updated_product) + '\n'

    file = open(DB_GLOBAL, 'w')
    file.writelines(lines)


update_database()
