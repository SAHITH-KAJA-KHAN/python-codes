octal_num = int(input("Enter an octal number: "))
decimal_num = 0
power = 0

while octal_num > 0:
        last_digit = octal_num % 10 
        decimal_num += last_digit *  pow(8,power) #(8 ** power)  
        octal_num //= 10  
        power += 1  
   
print (decimal_num) 
