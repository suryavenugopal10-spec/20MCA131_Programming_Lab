numbers = list(map(int, input("Enter integers: ").split()))
updated = ["over" if n > 100 else n for n in numbers]
print("Updated list:", updated)
