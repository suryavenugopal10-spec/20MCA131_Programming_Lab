list1 = [x.strip() for x in input("Enter color-list1: ").split(",") if x.strip()]
list2 = [x.strip() for x in input("Enter color-list2: ").split(",") if x.strip()]

result = [color for color in list1 if color not in list2]
print("Colors only in list1:", result)
