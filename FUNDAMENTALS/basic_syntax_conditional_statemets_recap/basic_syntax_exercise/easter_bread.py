budget = float(input())
price_for_flour_per_kg = float(input())

price_for_eggs = 0.75 * price_for_flour_per_kg
price_for_milk = 1.25 * price_for_flour_per_kg
milk_needed = 0.25 * price_for_milk

one_loaf = price_for_eggs + price_for_flour_per_kg + milk_needed

loafs_made = 0
remaining_budget = budget
colored_eggs = 0
third_loaf = False

while one_loaf <= remaining_budget:
    loafs_made += 1
    remaining_budget -= one_loaf
    colored_eggs += 3

for eggs in range(3, loafs_made + 1, 3):
    egg_to_subtract = eggs - 2
    colored_eggs -= egg_to_subtract

print(f"You made {loafs_made} loaves of Easter bread! Now you have {colored_eggs} eggs and {remaining_budget:.2f}BGN left.")