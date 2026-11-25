names = input("Enter names separated by commas: ").split(",")
total_a = sum(name.strip().lower().count("a") for name in names)
print("Names:", [name.strip() for name in names])
print("Occurrences of a:", total_a)
