'''     *
       ***
      *****
     *******
    *********  '''
n =5       
for row in range(1, n + 1):
    for space in range(n - row): 
        print(" ", end="")
    for star in range((row*2)-1):
        print("*", end="")
    print() 