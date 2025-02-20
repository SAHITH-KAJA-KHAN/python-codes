'''      *
        **
       ***
      ****
     *****
'''
n = int(input("Enter n: "))

for row in range(1, n + 1):
    for space in range(n - row): 
        print(" ", end="")
    for star in range(row):  
        print("*", end="")
    print()

