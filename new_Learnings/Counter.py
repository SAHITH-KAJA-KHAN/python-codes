from collections import Counter
x = (1,2,3,4,5,5,5,5,6,6,6)
x1=sorted(x)
c = Counter(x1)
print(c)