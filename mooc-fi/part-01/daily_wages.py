hourly_wage = float(input("Hourly wage: "))
hours_worked = int(input("Hours worked: "))
day = input("Day of the week: ")
wages = hourly_wage * hours_worked
if day == "Sunday" or day == "sunday":
    print(f"Daily wages: {wages * 2} euros")
else: print(f"Daily wages: {wages:.1f} euros")