from collections import Counter
x = (1,1,1,1,2,2,2,3,3,4) #giving desending order of frequency
x1=sorted(x)
c = Counter(x1)
print(c)