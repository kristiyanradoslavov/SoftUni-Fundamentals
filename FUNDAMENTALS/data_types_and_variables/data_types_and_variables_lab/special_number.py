number = int(input())

digit_sum = 0
for num in range(1, number + 1):
    num_to_str = str(num)
    for index in range(0, len(num_to_str)):
        digit = int(num_to_str[index])
        digit_sum += digit

    if digit_sum == 5 or digit_sum == 7 or digit_sum == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")

digit_sum = 0

