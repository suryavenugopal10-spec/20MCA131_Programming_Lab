a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a == b == c:
    print("All three numbers are equal.")
else:
    print("Biggest number:", max(a, b, c))
    if a == b or b == c or a == c:
        print("Two or more numbers are equal.")
