x=input().split()
for i in range(len(x)):  # Step 2: Loop through the list using index
    x[i] = int(x[i])  # Convert each element to an integer and store it back
print(x)
print(max(x))  # Step 3: Print the list of integers

