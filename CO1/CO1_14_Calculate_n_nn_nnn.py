n = input("Enter a single digit (0-9): ").strip()

if len(n) == 1 and n.isdigit():
    total = int(n) + int(n * 2) + int(n * 3)
    print(f"{n} + {n * 2} + {n * 3} = {total}")
else:
    print("Please enter exactly one digit.")
