divisor = int(input())
boundary = int(input())

divisor_found = False
max_multiple = 0

for current_bound in range(boundary, 0, -1):
    if current_bound % divisor == 0:
        divisor_found = True
        max_multiple = current_bound
        break
    else:
        continue
print(max_multiple)