import calendar

year = int(input("Enter the final year: "))

current_year = 2026

print("Leap years:")
for i in range(current_year, year + 1):
    if calendar.isleap(i):
        print(i)