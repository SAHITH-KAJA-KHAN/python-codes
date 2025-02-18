# def move_zeros(arr):
#     non_zero = [num for num in arr if num != 0]
#     return non_zero + [0] * (len(arr) - len(non_zero))

# print(move_zeros([0, 1, 0, 3, 12]))  # Output: [1, 3, 12, 0, 0]
#zero = 0
# for i in range(len(x)):
#   if x[i] ==0:
#     zero += 1

x = [1,2,4,0,0,5,4,33,0]
x.sort()
print(x)


zero = x.count(0)

print(zero)

while 0 in x:
  x.remove(0)
  
print(x)

for i in range(zero):
  
  x.append(0)
  
print(x)


#Efficient

def move_zeros(arr):
    j = 0  

    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]  
            j += 1  

arr = [1, 2, 4, 0, 0, 5, 4, 33, 0]
move_zeros(arr)
print(arr)  
