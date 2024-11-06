a = 10               #1      1      1     1*1
b = 30

for i in range(a,b):
  for j in range(1, i):
    if  j*j == i:
      print(i ,"perfect square" ,end=" ")
    