import math
def lcmfunc(arr):
  maxi =0
  for i in range(len(arr)-1):
    lcm = (arr[i] * arr[i+1]) // math.gcd(arr[i], arr[i+1])
    maxi = max(maxi,lcm)
  return maxi

arr = list(map(int, input().split()))
print(lcmfunc(arr))



