# line checker
def no_lines():
    fhand = open('database.txt')
    count = 0
    for line in fhand:
        count += 1
        print('Line count: ', count)
