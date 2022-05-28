current_year = int(input())

this_year = False
current_set = {}

while not this_year:
    current_year += 1
    year_to_str = str(current_year)
    for year in range(0, len(year_to_str)):
        current_digit = int(year_to_str[year])
        current_set += current_digit



