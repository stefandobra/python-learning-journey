person_1_name = input(f"Person 1:\nName: ")
person_1_age = int(input("Age: "))
person_2_name = input(f"Person 2:\nName: ")
person_2_age = int(input("Age: "))

if person_1_age > person_2_age:
    print(f"The elder is {person_1_name}")
elif person_1_age < person_2_age:
    print(f"The elder is {person_2_name}")
else:
    print(f"{person_1_name} and {person_2_name} are the same age")
