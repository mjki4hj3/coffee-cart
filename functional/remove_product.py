
# Temporarily assigns f with open('database.txt') output

with open('database.txt') as f:
    mydb = f.read().splitlines()  # adds each item on a line to a list

mydb.remove('Latte')  # Explicity tell each


with open('database.txt', 'w+') as f:
    for item in mydb:
        string = item + '\n'
        f.write(string)
print(mydb)
