# input : abddagf
# output : a2 b1 d2 g1 f1

s = input()

for i in s:
  print(i,s.count(i),end=" ")
 # s = s.replace(i,"")
print()


s = input()
unique_chars = []  

for i in s:
    if i not in unique_chars:  
        print(i,s.count(i), end=" ")
        unique_chars.append(i) 
