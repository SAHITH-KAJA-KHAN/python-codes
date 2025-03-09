n = 5
num1 = 1
num2 = n * (n + 1) // 2 + 1  # Start number for the second pyramid

# Printing the joined pyramids
for row in range(n):
    for space in range(row):
        print("   ", end="")  # Two spaces for alignment

    # First pyramid (left side)
    for col in range(n - row):
        print(format(num1, "02d"), end=" ")  # Formatting numbers with leading zeros
        num1 += 1

    # Second pyramid (right side)
    for col in range(n - row):
        print(format(num2, "02d"), end=" ")  
        num2 += 1

    print()
