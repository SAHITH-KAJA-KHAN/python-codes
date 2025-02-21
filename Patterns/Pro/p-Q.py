'''      *
        * *
       *   *
      *     *
     *********   '''
     


# for row in range(n):
#     for space in range(n - row - 1):  # Printing leading spaces
#         print(" ", end="")
    
#     for col in range(2 * row + 1):  # Printing stars and spaces
#         if col == 0 or col == 2 * row or row == n - 1:  # First/last star or last row
#             print("*", end="")
#         else:
#             print(" ", end="")  # Middle spaces
    
#     print()  # Move to next line

n = 5



for row in range(1, n + 1):
    print(" " * (n - row), end="")  # Print leading spaces

    for col in range(1, row * 2):  # Use row * 2 - 1 formula
        print("*" if col == 1 or col == (row * 2 - 1) or row == n else " ", end="")  

    print()  # Move to the next line
