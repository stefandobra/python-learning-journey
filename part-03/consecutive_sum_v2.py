limit = int(input("Limit: "))
number = 1
sum = 1

string = "The consecutive sum: 1"

while sum < limit:
    number += 1
    sum += number
    string += f" + {number}"

print(f"{string} = {sum}")