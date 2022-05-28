# ch = ord("A")
# print(ch)

count_of_letters = int(input())

counter = 0

for letter in range(count_of_letters):
    current_letter = input()
    asci_number = ord(current_letter)
    counter += asci_number

print(f"The sum equals: {counter}")