# Write a Python program to check a triangle is valid or not 

def check_triangle(l1,l2,l3):
  if l1==l2+l3 or l2==l1+l3 or l3==l1+l2:
    return "triangle"
  elif l1==l2==l3:
    return "Triangle"
  else:
    return "not triangle"



l1=20
l2=20
l3=20

print(check_triangle(l1,l2,l3))