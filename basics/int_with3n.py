# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5 
# Expected Result : 615

n = int(input("Enter a number: "))

res = (n + n*11 + n*111)

print(res)