st = input()
for i in st:
    if i in "aeiou AEIOU":
        print(i, end = ' ')
        print()
    elif i not in "aeiou AEIOU":
        print(i, end = ' ')
      