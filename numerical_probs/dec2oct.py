# Step 1: Take input from the user
decimal = int(input("Enter a decimal number: "))

# Step 2: Initialize octal and place value
octal = 0
place_value = 1  

# Step 3: Convert Decimal to Octal using repeated division
while decimal > 0:
    remainder = decimal % 8  # Get the last octal digit
    octal = (remainder * place_value) + octal  # Construct the octal number
    decimal //= 8  # Reduce the decimal number
    place_value *= 10  # Move to the next place value (1, 10, 100...)

# Step 4: Display the result
print("Octal Equivalent:", octal)
