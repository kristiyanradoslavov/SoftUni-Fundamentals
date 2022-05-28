count_of_inputs = int(input())

capacity = 255
filled_water = 0

for liters in range(1,count_of_inputs + 1):
    current_liters = int(input())
    filled_water += current_liters
    if filled_water > capacity:
        print("Insufficient capacity!")
        filled_water -= current_liters
        continue

print(filled_water)