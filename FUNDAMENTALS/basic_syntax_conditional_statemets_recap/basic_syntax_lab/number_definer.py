input_number = float(input())

negative_number = False
current_number = 0


if input_number == 0:
    print("zero")
elif input_number > 0:
    if input_number < 1:
        print("small positive")
    elif input_number > 1000000:
        print("large positive")
    else:
        print("positive")

if input_number < 0:
    negative_number = True

if negative_number is True:
    current_number = abs(input_number)
    if current_number < 1:
        print("small negative")
    elif current_number > 1000000:
        print("large negative")
    else:
        print("negative")
