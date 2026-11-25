import math

start = int(input("Enter range start: "))
end = int(input("Enter range end: "))
result = []

for n in range(max(1000, start), min(9999, end) + 1):
    even_digits = all(int(digit) % 2 == 0 for digit in str(n))
    root = math.isqrt(n)

    if even_digits and root * root == n:
        result.append(n)

print("Matching numbers:", result)
