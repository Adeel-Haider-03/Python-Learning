a=7
b=6

if a>b:
    print("a is greater than b")
elif a<b:
    print("a is less than b")
else:
    print("a and b are equal")

if a==b:
    pass        # Placeholder for future code, does nothing for now but fulfills syntax requirements


# match statement (switch-case alternative in Python)

day=3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:     # Use the underscore character _ as the last case value if you want a code block to execute when there are not other matches:
        print("Invalid day")


match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")

# Example of using match with patterns
point = (1, 0)
match point:
    case (0, 0):
        print("Origin")
    case (x, 0):
        print(f"X={x} on the X-axis")
    case (0, y):
        print(f"Y={y} on the Y-axis")
    case (x, y):
        print(f"Point at X={x}, Y={y}")