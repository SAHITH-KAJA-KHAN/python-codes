def compress_string(s):
    if not s:  
        return ""  # Handle empty input case

    result = []  # Using list for efficient concatenation
    count = 1  

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:  
            count += 1  
        else:
            result.append(f"{count}{s[i - 1]}" if s[i - 1] != " " else " ")  # Store result efficiently
            count = 1  # Reset count

    result.append(f"{count}{s[-1]}" if s[-1] != " " else " ")  # Append last group

    return "".join(result)  # Convert list to string efficiently

# Test Case
input_str = "AAA BB CC"
print(compress_string(input_str))  # Output: "3A 2B 2C"
