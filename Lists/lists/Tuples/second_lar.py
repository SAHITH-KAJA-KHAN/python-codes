tup = (1,2,2,2,3,4,5)


x=tuple(sorted(set(tup)))
print(type(x))
print(x)

t1 = (5, 1, 8)
t2 = (2, 7, 4)
result = tuple((sorted(t1 + t2)))
print(result)
print(type(result))