lost_fight_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_expenses = 0
broken_shield_counter = 0
helmet_broken = False

for fights in range(1, lost_fight_count + 1):
    if fights % 2 == 0:
        total_expenses += helmet_price
        helmet_broken = True
    if fights % 3 == 0:
        total_expenses += sword_price
        if helmet_broken:
            total_expenses += shield_price
            broken_shield_counter += 1
            if broken_shield_counter == 2:
                total_expenses += armor_price
                broken_shield_counter = 0
    helmet_broken = False

print(f"Gladiator expenses: {total_expenses:.2f} aureus")


