n = int(input("Enter a non-zero integer: "))

if n == 0:
    print("Zero has infinitely many non-zero integer divisors.")
else:
    factors = []
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            factors.append(i)

    print("Positive factors:", factors)
