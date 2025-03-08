
''' 1 1 1 1 1 2
    3 2 2 2 2 2
    3 3 3 3 3 4
    5 4 4 4 4 4
    5 5 5 5 5 6 '''


n = 5  # Number of rows

for i in range(1, n + 1):
    for j in range(n + 1):
        if i % 2 == 0:  
            if j == 0:
                print(i + 1, end=" ")
            else:
                print(i, end=" ")
        else:  
            if j == n:
                print(i + 1, end=" ")
            else:
                print(i, end=" ")
    print()
