valid_input = [0, 1, 2]

user_input = input("please input a value: ")

while True:
    if int(user_input) in valid_input:
        print("working")
    else:
        print("not working")
        break

print("OOL")
