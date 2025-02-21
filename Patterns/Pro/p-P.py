''' * * * * *
     * * * *
      * * *
       * *
        *
        *
       * *
      * * *
     * * * *
    * * * * *  '''
    

n =5       
for row in range(n):
    for space in range(row):
      print(" ", end="")
    for star in range(n - row):  
        print(" *", end="")
    print()
for row in range(n):
    for space in range(n-row):
      print(" ", end="")
    for star in range(row+1):  
        print("* ", end="")
    
    print()
