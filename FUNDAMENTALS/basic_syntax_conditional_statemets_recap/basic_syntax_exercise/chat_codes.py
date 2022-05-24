number_of_messages = int(input())

for i in range(1, number_of_messages + 1):
    number_of_messages = int(input())
    if number_of_messages == 88:
        print("Hello")
    elif number_of_messages == 86:
        print("How are you?")
    elif number_of_messages < 88:
        print("GREAT!")
    elif number_of_messages > 88:
        print("Bye.")