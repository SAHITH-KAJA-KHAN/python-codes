# Merge Two Sorted Arrays

# Problem: Merge two sorted arrays into a single sorted array.
# Test Case: arr1 = [1, 3, 5], arr2 = [2, 4, 6]
# Output: [1, 2, 3, 4, 5, 6]







lst1= list(map(int,input().split()))
lst2= list(map(int,input().split()))

#lst2= input().split()
lst1.extend(lst2)
lst1.sort()



print (lst1)



