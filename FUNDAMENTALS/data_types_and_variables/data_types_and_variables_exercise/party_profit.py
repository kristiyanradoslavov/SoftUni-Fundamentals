group_size = int(input())
days = int(input())

coin_earned = 0
motivational_party = False

for days in range(1, days + 1):
    if days % 10 == 0:
        group_size -= 2
    if days % 15 == 0:
        group_size += 5
    coin_earned += 50
    companion_expenses = 2 * group_size
    coin_earned -= companion_expenses
    if days % 3 == 0:
        motivational_party = True
        drinking_expenses = 3 * group_size
        coin_earned -= drinking_expenses
    if days % 5 == 0:
        monster_slayed = 20 * group_size
        coin_earned += monster_slayed
        if motivational_party:
            additional_expenses = 2 * group_size
            coin_earned -= additional_expenses
    motivational_party = False

final_coins = coin_earned // group_size

print(f"{group_size} companions received {final_coins} coins each.")
