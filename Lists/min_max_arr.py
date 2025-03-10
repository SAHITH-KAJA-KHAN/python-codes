
def find_min_max(arr):
    if not arr:  # Check if the array is empty
        return None, None

    min_val = max_val = arr[0]  # Initialize min and max with the first element

    for num in arr[1:]:  # Iterate through the array starting from index 1
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num

    return min_val, max_val  # Return the min and max values

# Example usage:
arr = [17, 5, 9, 21, 3, 11]
print(find_min_max(arr))  # Output: (3, 21)
