'''    ****
       *  *
       *  *
       *  *
       ****  '''
       


n = 5  # Height of the rectangle
width = n - 1  # Width should be 4 instead of 5

for i in range(n):  # Loop for rows
    for j in range(width):  # Loop for columns
        if i == 0 or i == n - 1 or j == 0 or j == width - 1:  
            print("*", end="")  # Print '*' at the border positions
        else:
            print(" ", end="")  # Print spaces inside the rectangle
    print()  # Move to the next line
