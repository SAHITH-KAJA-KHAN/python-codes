# Input: t = (1, 2, 3, 4, 5), index1 = 1, index2 = 3  
# Output: (1, 4, 3, 2, 5)

t = input().split()
t1 = list(t)
print(t1)
n1 = int(input())
n2 = int(input())

t1[n1], t1[n2] = t1[n2], t1[n1]

print(t1)
print(tuple(t1))
t2 = tuple(t1)
print(type(t2))


