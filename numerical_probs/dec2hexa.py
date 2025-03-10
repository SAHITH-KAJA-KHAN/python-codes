decimal_num = int(input("Enter a decimal number: "))

hex_digits = "0123456789ABCDEF"
hex_result = ""

while decimal_num > 0:
    remainder = decimal_num % 16  # Get remainder when divided by 16
    hex_result = hex_digits[remainder] + hex_result  # Add hex digit
    decimal_num //= 16  # Reduce decimal number

print("Hexadecimal:", hex_result)
