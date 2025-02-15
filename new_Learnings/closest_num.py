def find_closest_number(arr, target):
    # Initialize the closest number as the first element
    closest_number = arr[0]  

    low, high = 0, len(arr) - 1  # Binary search boundaries
    
    while low <= high:
        mid = (low + high) // 2  # Find the middle element

        # If we find the exact target, return it immediately
        if arr[mid] == target:
            return arr[mid]
        
        # Check if arr[mid] is closer than the current closest_number
        if abs(arr[mid] - target) < abs(closest_number - target):
            closest_number = arr[mid]  # Update closest number
        elif abs(arr[mid] - target) == abs(closest_number - target):
            closest_number = min(arr[mid], closest_number)  # Pick the smaller one if distances are equal

        # Adjust search range using binary search
        if arr[mid] < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half

    return closest_number  # Return the closest number found

# Test Cases
numbers = [1, 3, 6, 8, 12]  # Sorted array
target = 7
print(find_closest_number(numbers, target))  # Expected Output: 6

numbers = [2, 5, 10, 20]
target = 10
print(find_closest_number(numbers, target))  # Expected Output: 10 (Exact match)
