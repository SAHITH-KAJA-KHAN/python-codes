x = input().split()
#x=[1,2,3,4,5,1]

# def remove_duplicates(x):
#   unique_elements = list(set(x))
#   unique_elements.sort()
#   return unique_elements

# print(remove_duplicates(x))

x.sort() #3567789
def remove_duplicates(x):
  for i in range(len(x)-1):
    if x[i] == x[i+1]:
      return True
  return False
print(remove_duplicates(x))
