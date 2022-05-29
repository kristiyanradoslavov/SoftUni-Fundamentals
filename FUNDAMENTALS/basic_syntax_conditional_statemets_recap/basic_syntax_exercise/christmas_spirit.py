quantity = int(input())
days = int(input())

single_ornament_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15

ornament_spirit_points = 5
tree_skirt_points = 3
tree_garland_points = 10
tree_lights_points = 17

total_funds_spent = 0
total_spirit = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        total_funds_spent += single_ornament_price * quantity
        total_spirit += ornament_spirit_points
    if day % 3 == 0:
        total_funds_spent += (tree_skirt_price + tree_garland_price) * quantity
        total_spirit += tree_skirt_points + tree_garland_points
    if day % 5 == 0:
        total_funds_spent += tree_lights_price * quantity
        total_spirit += tree_lights_points
        if day % 3 == 0:
            total_spirit += 30
    if day % 10 == 0:
        total_spirit -= 20
        total_funds_spent += tree_skirt_price + tree_garland_price + tree_lights_price

if days % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_funds_spent:.0f}")
print(f"Total spirit: {total_spirit:.0f}")

