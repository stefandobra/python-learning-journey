year = int(input("Year: "))

leap = False

if year % 100 == 0:
    if year % 400 == 0:
        leap = True
elif year % 4 == 0:
    leap = True

if leap:
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")