count_of_snowballs = int(input())

current_result = 0
best_weigh = 0
best_time = 0
best_quality = 0

for snowball in range(1, count_of_snowballs + 1):
    weight = int(input())
    time = int(input())
    quality = int(input())
    result = (weight / time) ** quality
    if result > current_result:
        current_result = result
        best_weigh = weight
        best_time = time
        best_quality = quality

print(f"{best_weigh} : {best_time} = {current_result:.0f} ({best_quality})")
