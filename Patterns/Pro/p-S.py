'''      *
        * *
       *   *
      *     *
     *       *
      *     *
       *   *
        * *
         *     '''
n = 5
# for row in range(n):
#     for space in range(n-row):
#         print(" ", end="")
#     for star in range(1, row*2):
#         print("*" if star == 1 or star == (row*2-1) else " ", end="")
#     print()


for row in range(1, n + 1):
    print(" " * (n - row), end="")  # Print leading spaces

    for col in range(1, row * 2):  # Use row * 2 - 1 formula
        print("*" if col == 1 or col == (row * 2 - 1) else " ", end="")  

    print()  # Move to the next line
    
for row in range(n-1,0,-1):
    print(" " * (n - row), end="")  # Print leading spaces

    for col in range(1, row * 2):  # Use row * 2 - 1 formula
        print("*" if col == 1 or col == (row * 2 - 1) else " ", end="")  

    print()  # Move to the next line