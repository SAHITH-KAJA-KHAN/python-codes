''' 5 5 5 5 5
    4 4 4 4
    3 3 3
    2 2
    1   '''
  
  
n =5
for row in range(1,n+1):
  for col in range(n-(row-1)):
    print(n-(row-1),end=" ")
  print()