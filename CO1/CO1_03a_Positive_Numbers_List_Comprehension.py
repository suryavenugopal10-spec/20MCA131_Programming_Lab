numbers = list(map(int, input("Enter integers: ").split()))
positive = [n for n in numbers if n > 0]
print("Positive numbers:", positive)
