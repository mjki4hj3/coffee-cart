import os


def dbs():
    output = os.listdir('./DB')
    return print(output)


dbs()
