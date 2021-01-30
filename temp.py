valid_input = [0, 1, 2]


def test():
    user_input = input("> ")

    while True:
        if int(user_input) in valid_input:
            print("working")
            break
        else:
            print("not working")
            test()


def work():
  while int(input("\n".join(range(3) + "\nplease input a number from the options: ")) not in [0, 1, 2]:
      print("not working")
