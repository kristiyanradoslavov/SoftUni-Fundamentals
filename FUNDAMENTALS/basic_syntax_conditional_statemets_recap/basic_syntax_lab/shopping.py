budget = int(input())

current_input = input()

remaining_budget = budget
overdraft = False

while current_input != "End":
    current_product = int(current_input)
    remaining_budget -= current_product
    if remaining_budget < 0:
        overdraft = True
        break
    current_input = input()

if overdraft is True:
    print(f"You went in overdraft!")
else:
    print("You bought everything needed.")