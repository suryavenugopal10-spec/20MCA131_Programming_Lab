numbers = list(map(int, input("Enter integers: ").split()))
odds = [n for n in numbers if n % 2 != 0]
print("List after removing even numbers:", odds)
