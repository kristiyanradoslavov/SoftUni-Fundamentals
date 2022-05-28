input_number = int(input())

for i in range(0, input_number):
    for k in range(0, input_number):
        for j in range(0, input_number):
            print(f"{chr(97 + i)}{chr(97 + k)}{chr(97 + j)}")
