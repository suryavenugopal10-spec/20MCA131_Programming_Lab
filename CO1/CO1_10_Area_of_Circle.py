import math

radius = float(input("Enter radius: "))

if radius < 0:
    print("Radius cannot be negative.")
else:
    area = math.pi * radius ** 2
    print(f"Area of circle: {area:.2f}")
