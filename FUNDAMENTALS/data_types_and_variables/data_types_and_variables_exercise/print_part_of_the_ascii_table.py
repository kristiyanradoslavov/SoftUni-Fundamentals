start_number = int(input())
end_number = int(input())

for current_number in range(start_number, end_number + 1):
    character = chr(current_number)
    print(character, end=" ")
