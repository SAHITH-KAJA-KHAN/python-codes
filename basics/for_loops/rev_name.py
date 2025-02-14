# x = input("enter name")
# print (x.reversed())

# s = "sahith kaja khan"
# rev = s[::-1]
# print(rev)

# s = "sahith kaja khan"
# words = s.split()
# rev_words = [word[::-1] for word in words]
# rev_s = ' '.join(rev_words)
# print(rev_s)

name = "sahith kaja khan" 


words = name.split()


words.reverse()
print(words)

reversed_name = " ".join(words)


print("Reversed name:", reversed_name)
