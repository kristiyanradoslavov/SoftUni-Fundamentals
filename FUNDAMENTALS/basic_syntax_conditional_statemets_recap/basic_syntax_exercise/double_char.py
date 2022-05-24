current_string = input()

while current_string != "End":
    if current_string == "SoftUni":
        current_string = input()
        continue
    doubled_string = ""
    for i in current_string:
        double = i * 2
        doubled_string += double
    print(doubled_string)
    doubled_string = ""

    current_string = input()