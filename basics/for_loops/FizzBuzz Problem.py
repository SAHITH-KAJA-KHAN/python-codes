# Problem: Print numbers from 1 to N.

# If a number is divisible by 3, print "Fizz".
# If a number is divisible by 5, print "Buzz".
# If a number is divisible by both 3 and 5, print "FizzBuzz".

# Solution
N = int(input())
for i in range(1, N+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")

    