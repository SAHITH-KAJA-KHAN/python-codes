# import re

# s = input()
# numbers = re.findall(r'\d+', s)  # Find all numbers in the string
# total_sum = sum(map(int, numbers))  # Convert to int and sum them
# print(total_sum)

s = input()
num = ""
total_sum = 0

for char in s:
    if char.isdigit():
        num += char  # Build the number
    else:
        if num:
            total_sum += int(num)  # Add the complete number
            num = ""  # Reset for the next number

if num:
    total_sum += int(num)  # Add the last number if any

print(total_sum)
