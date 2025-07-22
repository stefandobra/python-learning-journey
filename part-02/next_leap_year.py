
year = int(input("Year: "))

leap = year + 1


while True:
    if leap % 100 == 0 and leap % 400 == 0:
        break
    elif leap % 4 == 0 and leap % 100 != 0:
        break
    leap += 1
        

print(f"The next leap year after {year} is {leap}")



