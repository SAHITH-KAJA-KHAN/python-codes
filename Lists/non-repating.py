from collections import Counter

def first_non_repeating(arr):
    freq = Counter(arr)  # Count occurrences of each number
    for num in arr:
        if freq[num] == 1:  # Find the first element with count 1
            return num
    return -1  # If no unique element

# Example usage
arr = list(map(int, input().split()))
print(first_non_repeating(arr))
