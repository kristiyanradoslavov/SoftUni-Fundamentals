current_name = input()

voldemort_entered = False

while current_name != "Welcome!":
    if current_name == "Voldemort":
        voldemort_entered = True
        break
    char_counter = 0
    for char in range(0, len(current_name)):
        char_counter += 1
    if char_counter < 5:
        print(f"{current_name} goes to Gryffindor.")
    elif char_counter == 5:
        print(f"{current_name} goes to Slytherin.")
    elif char_counter == 6:
        print(f"{current_name} goes to Ravenclaw.")
    elif char_counter > 6:
        print(f"{current_name} goes to Hufflepuff.")

    char_counter = 0
    current_name = input()

if voldemort_entered:
    print(f"You must not speak of that name!")
else:
    print(f"Welcome to Hogwarts.")
