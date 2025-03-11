n = 4 # Change this value for different sizes

for i in range(2 * n - 1):  # Loop through rows (0 to 6)
    for j in range(2 * n - 1):  # Loop through columns (0 to 6)
        num = n - min(i, j, (2 * n - 2) - i, (2 * n - 2) - j)  # Compute value at (i, j)
        print(num, end=" ")
    print()  # Move to the next row
