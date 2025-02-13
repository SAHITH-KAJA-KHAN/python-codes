str = input().lower()
vowels = "aeiou"
vowel_count = consonant_count = 0
for char in str:
    if char in vowels:
        vowel_count += 1
    elif char.isalpha():  # Check if the character is a letter
        consonant_count += 1
print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")
