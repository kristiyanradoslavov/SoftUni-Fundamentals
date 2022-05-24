number_of_orders = int(input())

total_coffee_price = 0

for order in range(1, number_of_orders + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    require_capsules = days * capsules_needed_per_day
    coffee_price = require_capsules * price_per_capsule

    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_needed_per_day < 1 or capsules_needed_per_day > 2000:
        continue
    total_coffee_price += coffee_price
    print(f"The price for the coffee is: ${coffee_price:.2f}")


print(f"Total: ${total_coffee_price:.2f}")

    
