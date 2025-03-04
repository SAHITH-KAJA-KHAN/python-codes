# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# # Sorting the numbers in descending order
# if a < b:
#     a, b = b, a
# if a < c:
#     a, c = c, a
# if a < d:
#     a, d = d, a
# if b < c:
#     b, c = c, b
# if b < d:
#     b, d = d, b
# if c < d:
#     c, d = d, c

# # Printing the result in the required format
# print(a, '>', b, '>', c, '>', d)


a = int(input())
b = int(input())
c = int(input())
d = int(input())

# Finding the maximum and swapping
a, b = max(a, b), a + b - max(a, b)
a, c = max(a, c), a + c - max(a, c)
a, d = max(a, d), a + d - max(a, d)
b, c = max(b, c), b + c - max(b, c)
b, d = max(b, d), b + d - max(b, d)
c, d = max(c, d), c + d - max(c, d)


print(a, ">", b, ">", c, ">", d)
