amount = int(input())
denominations = [500, 100, 50, 20, 10, 5, 2]

for denom in denominations:
    count = amount // denom  
    print(denom, "-", count)
    amount %= denom

