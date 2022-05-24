command = input()

total_cups_of_coffee = 0

while command != "END":
    if command == "coding":
        total_cups_of_coffee += 1
    elif command == "CODING":
        total_cups_of_coffee += 2
    elif command == "dog" or command == "cat":
        total_cups_of_coffee += 1
    elif command == "DOG" or command == "CAT":
        total_cups_of_coffee += 2
    elif command == "movie":
        total_cups_of_coffee += 1
    elif command == "MOVIE":
        total_cups_of_coffee += 2

    command = input()

if total_cups_of_coffee > 5:
    print("You need extra sleep")
else:
    print(f"{total_cups_of_coffee}")