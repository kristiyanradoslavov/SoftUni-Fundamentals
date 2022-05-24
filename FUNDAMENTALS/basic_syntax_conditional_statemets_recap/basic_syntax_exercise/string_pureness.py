number_of_strings = int(input())

for all_strings in range(number_of_strings):
    string = input()
    string_is_pure = True
    for char in string:
        if char == "_" or char == "," or char == ".":
            string_is_pure = False
            break
    if string_is_pure:
        print(f"{string} is pure.")
    else:
        print(f"{string} is not pure!")
