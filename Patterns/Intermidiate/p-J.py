

''' *
    **
    ***
    ****
    *****
    ****
    ***
    **
    *
'''

n = int(input())  # Taking user input

for row in range(1, (2 * n)):  
    colTimes = row if row <= n else (2 * n) - row  
    for col in range(colTimes):  
        print("*", end="")  
    print() 
