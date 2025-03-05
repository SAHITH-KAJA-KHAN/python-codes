# input : abddagf
# output : a2 b1 d2 g1 f1

s = input()

for i in s:
  print(i,s.count(i),end=" ")
 # s = s.replace(i,"")
print()


s = input()
visited_char = []  

for i in s:
    if i not in visited_char:  
        print(i,s.count(i), end=" ")
        visited_char.append(i) 
