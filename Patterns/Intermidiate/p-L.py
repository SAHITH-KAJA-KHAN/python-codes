'''  *****
      ****
       ***
        **
         *  '''
# n =5       
# for row in range(n):
#     for space in range(row):
#       print(" ", end="")
#     for star in range(n - row):  
#         print("* ", end="")
    
#     print()
n =5       
for row in range(n):
    for space in range(row):
      print(row, end="")
    for star in range(n - row):  
        print("*", end="")
    
    print()
