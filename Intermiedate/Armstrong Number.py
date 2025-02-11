
    
    
    
    

n = int(input()) #153
st = str(n) #"1" "5" "3"
length = len(st) #3
arm = 0
for i in st:
  arm += int(i) ** length 

  
if(n==arm):
  print("Armstrong")
else:
  print("Not Armstrong")