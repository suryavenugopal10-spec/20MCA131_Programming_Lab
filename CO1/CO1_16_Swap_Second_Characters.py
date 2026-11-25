s1 = input("Enter first string (at least 2 characters): ")
s2 = input("Enter second string (at least 2 characters): ")

if len(s1) < 2 or len(s2) < 2:
    print("Both strings must contain at least two characters.")
else:
    new_s1 = s1[0] + s2[1] + s1[2:]
    new_s2 = s2[0] + s1[1] + s2[2:]
    print("Combined string:", new_s1 + " " + new_s2)
