
import math
N = input()
sum_fact = sum(math.factorial(int(char)) for char in N)
print("Yes" if sum_fact == int(N) else "No")
