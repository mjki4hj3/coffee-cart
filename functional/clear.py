from time import sleep
from db_functions import DB_GLOBAL


def clear():
    try:
        output = str(
            input("Would you like to clear the database? (Y/N): "))
    except ValueError:
        print("You did not enter Y or N, please try again")
        clear()
    if output == ('Y' or 'y'):
        file = open(DB_GLOBAL, 'w')
        file.write('')
    elif output == ('N' or 'n'):
        print("Goodbye")
        sleep(0.5)
        exit()
    else:
        print("You did not enter Y or N, please try again")
        clear()


clear()
