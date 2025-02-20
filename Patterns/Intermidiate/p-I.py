''' 1 2 3 4 5
    1 2 3 4 
    1 2 3
    1 2 
    1    '''
    
n=5
for row in range(1,n+1):
  for col in range(n-(row-1)):
    print(col+1,end=" ")
  print()