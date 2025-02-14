# Input: [1, 2, 3, 4, 5]  
# Output: True  
# x = [1,2,9,6,8]

# # Using all() function to check if all elements in the list are greater than 0

# print(all(i > 0 for i in x))


    
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:  # If an element is greater than the next, not sorted
            return False
    return True

# 📌 User Input
numbers = input("Enter numbers separated by spaces: ")
arr = list(map(int, numbers.split()))  # Convert input to a list of integers

# ✅ Check if sorted
if is_sorted(arr):
    print("True (The array is sorted)")
else:
    print("False (The array is not sorted)")
