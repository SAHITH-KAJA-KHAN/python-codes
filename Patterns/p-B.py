''' where n=5 
    
    *
    **
    ***
    ****
    *****  ''' 
    
n = int(input())
for i in range(1,n+1):
    print("*" * i)
print()
    
    
n = 5
for i in range(n):  # Outer loop for rows
    for j in range(i + 1):  # Inner loop for columns
        print('*', end='')  # Print star without newline
    print()  # Move to next line
