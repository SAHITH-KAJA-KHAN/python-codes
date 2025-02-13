x = [1,2,4,0,0,5,4,33,0]
x.sort()
print(x)

zero = 0

for i in range(len(x)):
  if x[i] ==0:
    zero += 1

print(zero)

while 0 in x:
  x.remove(0)
  
print(x)

for i in range(zero):
  
  x.append(0)
  
print(x)