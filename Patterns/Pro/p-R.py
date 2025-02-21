'''  *********
      *     *
       *   *
        * *
         *    '''
         
n=5
for row in range(n,0,-1):
    print(" " * (n - row), end="")  # Print leading spaces

    for col in range(1, row * 2):  # Use row * 2 - 1 formula
        print("*" if col == 1 or col == (row * 2 - 1) or row == n else " ", end="")  

    print()  # Move to the next line