'''       *****
         *   *
        *   *
       *   *
      *****    '''
n = 5  # Number of rows

for i in range(n):  # Loop for rows
    for j in range(n - i - 1):  # Loop for leading spaces
        print(" ", end="")
    
    for j in range(n):  # Loop for stars and spaces inside
        if j == 0 or j == n - 1 or i == 0 or i == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    
    print()  # Move to the next line
