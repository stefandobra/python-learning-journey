string = input("string: ")
substring = input("substring: ")

first_occ = string.find(substring)
second_occ = -1
lenght_substring = len(substring)



if first_occ >= 0:
    sec_string = string[lenght_substring + first_occ:]
    second_occ = sec_string.find(substring)
    len_dif = len(string) - len(sec_string)
if second_occ >= 0:
    print(f"The second occurrence of the substring is at index {second_occ + len_dif}.")
else:
    print("The substring does not occur twice in the string.")
