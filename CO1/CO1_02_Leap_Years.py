from datetime import date

current_year = date.today().year
final_year = int(input("Enter final year: "))

if final_year < current_year:
    print("Final year must be greater than or equal to the current year.")
else:
    print("Leap years:")
    for year in range(current_year, final_year + 1):
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            print(year, end=" ")
    print()
