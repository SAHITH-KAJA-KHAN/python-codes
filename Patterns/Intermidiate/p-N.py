''' *********
     *******
      *****
       ***
        *    '''
# n =5       
# for row in range(1, n + 1):
#     for space in range(n - row): 
#         print(" ", end="")
#     for star in range((row*2)-1):
#         print("*", end="")
#     print() 

# n =5       
# for row in range(n):
#     for space in range(row):
#       print(" ", end="")
#     for star in range(n - row):  
#         print("* ", end="")
    
#     print()

# n =5       
# for row in range(n):
#     for space in range(row):
#       print(' ', end="")
#     for star in range(n - row):  
#         print("*", end="")
    
#     print()
    
n = 5

for row in range(n):
    for space in range(row):  # Printing leading spaces
        print(" ", end="")
    for star in range(2 * (n - row) - 1):  # Printing decreasing odd stars
        print("*", end="")
    print()  # Moving to the next line
