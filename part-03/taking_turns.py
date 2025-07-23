number = int(input("Please type in a number: "))

i = 1
last = number

while i < last:
    print(f"{i}\n{last}")
    i += 1
    last -= 1

if i == last:
    print(i)
   

# while i <= number:
#     if i > last:
#         break
#     if i == last:
#         print(i)
#         break
#     print(f"{i}\n{last}")
#     last -= 1
#     i += 1
    