# Python program to convert decimal into other number systems
# dec = 344

# print("The decimal value of", dec, "is:")
# print(bin(dec), "in binary.")
# print(oct(dec), "in octal.")
# print(hex(dec), "in hexadecimal.")
# # The decimal number is converted to binary, octal, and hexadecimal using the bin(), oct(), and hex() functions, respectively.
# # The output is displayed using the print() function.



# # Step 1: Take binary input as an integer
# binary = int(input("Enter a binary number: "))  

# # Step 2: Convert Binary to Decimal
# decimal = 0  # Initialize decimal result as 0
# power = 0  # This will track the position of the binary digit (2^power)

# while binary > 0:
#     last_digit = binary % 10  # Extract the last digit of binary number
#     decimal = decimal + (last_digit * (2 ** power))  # Convert to decimal value
#     power = power + 1  # Move to the next power of 2
#     binary = binary // 10  # Remove the last digit of the binary number

# # Step 3: Convert Decimal to Octal
# octal = 0  # Initialize octal result as 0
# place_value = 1  # Place value to store octal digits (1, 10, 100, etc.)

# while decimal > 0:
#     remainder = decimal % 8  # Get remainder when dividing by 8
#     octal = (remainder * place_value) + octal  # Construct the octal number
#     decimal = decimal // 8  # Reduce decimal number
#     place_value = place_value * 10  # Increase place value for next digit

# # Step 4: Print the Octal Number
# print("Octal Equivalent:", octal)



b = int(input())
de = 0
p = 0
while b > 0:
    ld = b%10
    de = de + (ld * (2 ** p))
    p = p + 1
    b = b//10
    
oct = 0
pv = 1
while de > 0:
    rem = de % 8
    oct = (rem * pv) + oct
    de = de // 8
    pv = pv * 10
    
print("Octal Equivalent:", oct)



# binary = input("Enter a binary number: ")
# decimal = int(binary, 2)
# octal = oct(decimal)[2:]  # Convert decimal to octal
# print("Octal:", octal)
# print(decimal)
# # The input is a binary number, which is converted to decimal using int() with base 2.
# # The decimal number is then converted to octal using the oct() function.


