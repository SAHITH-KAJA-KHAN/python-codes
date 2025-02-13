n = int(input()) #121

st = str(n) #"121" ==  121 ?
if(st == st[::-1]):
  print("The number is a palindrome")
else:
  print("The number is not a palindrome")
    