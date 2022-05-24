current_number = float(input())

while current_number < 1 or current_number > 100:
    current_number = float(input())

if 1 <= current_number <= 100:
    print(f"The number {current_number} is between 1 and 100")

