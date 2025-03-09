# decimal = int(input("Enter a decimal number: "))
# binary = bin(decimal)[2:]  # Using built-in function
# print("Binary:", binary)

dec = int(input())


binary = 0
pv = 1

while dec > 0:
  rem = dec % 2
  binary  = (rem * pv) + binary
  dec = dec // 2
  pv  =pv * 10
  
print("Binary Equivalent:", binary)

