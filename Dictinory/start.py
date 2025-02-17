#  key : value pairs unordered,mutable
# dict = {     key:value,    key:value,   key:value,  }

info = {
  #"key":"value",
  "name":"John",
  "midname" : ["mathew","khan"],
  "sub": {
    "math":80,
    "science":90,
    "english":75,
    
  },
   "age":30, 
 # 30: "age", 
  "city" : "New York"
}
info["name"] = "sahith"
info["surname"] = "kaja"
print(info.items())
#print(info.keys())
#print(tuple(info.values()))
#print(info.keys())
#print (info)