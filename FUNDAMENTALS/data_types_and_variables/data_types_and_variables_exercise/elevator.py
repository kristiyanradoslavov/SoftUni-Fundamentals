people = int(input())
capacity = int(input())

number_of_courses = people // capacity
remaining = people % capacity

remainers = False

if remaining != 0:
    remainers = True

if remainers:
    number_of_courses += 1

print(number_of_courses)