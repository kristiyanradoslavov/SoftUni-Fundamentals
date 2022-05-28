first_string = input()
second_string = input()

last_string = first_string

for i in range(0, len(second_string)):
    first_letter = first_string[i+1:]
    second_letter = second_string[:i+1]
    final_string = second_letter + first_letter
    if final_string == last_string:
        continue
    print(final_string)
    last_string = final_string