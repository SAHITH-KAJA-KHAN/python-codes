# s = input()
# print("min word " + min(s))
# print("max word " + max(s))



# s = input().split()
# print("smallest word:", min(s, key=len))  # Based on length
# print("largest word:", max(s, key=len))  # Based on length


s = input().split()

# Initialize min_word and max_word with the first word
min_word = s[0]
max_word = s[0]

# Iterate through the list to find the min and max words
for word in s:
    if word < min_word:  # Lexicographically smaller
        min_word = word
    if word > max_word:  # Lexicographically larger
        max_word = word

print("min word:", min_word)
print("max word:", max_word)


s = input().split()

# Initialize with the first word
min_word = s[0]
max_word = s[0]

# Iterate through words
for word in s:
    if len(word) < len(min_word):  # Shortest word
        min_word = word
    if len(word) > len(max_word):  # Longest word
        max_word = word

print("min word:", min_word)
print("max word:", max_word)
