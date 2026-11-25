colors = [c.strip() for c in input("Enter colors separated by commas: ").split(",") if c.strip()]

if colors:
    print("First color:", colors[0])
    print("Last color:", colors[-1])
else:
    print("No colors entered.")
