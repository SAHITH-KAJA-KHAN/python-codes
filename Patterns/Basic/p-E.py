''' 1
    0 1
    1 0 1
    0 1 0 1
    1 0 1 0 1  
'''

n = 5
for i in range(1, n + 1):  
    num = i % 2  
    for j in range(i): 
        print(num, end=' ')  
        num = 1 - num  #num ^ 1
    print()  
