# Find the Missing Number in an Array

# Problem: Find the missing number in an array of integers from 1 to N.
# Test Case: arr = [1, 2, 4, 5, 6], N = 6
# Output: 3

def missing_number(n, arr):
    total_sum = sum(arr)  # Sum of given numbers
    this_sum = n * (n + 1) // 2  # Expected sum of 1 to N
    missing = this_sum - total_sum  # Missing number
    return missing

# Input from user
n = int(input("Enter N: "))  
arr = list(map(int, input("Enter numbers: ").split()))  

# Call the function and print the missing number
print("Missing Number:", missing_number(n, arr))
