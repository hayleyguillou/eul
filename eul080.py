from decimal import *

def get_digit_sum(n):
    """Returns sum of digits by converting to string"""
    return sum(int(digit) for digit in str(n))

maximum = 100
power = 10 ** (100 - 1)
s = 0
getcontext().prec = 102

for n in range(2,maximum):
    test = Decimal(n).sqrt()
    if int(test)**2 != n:
        s += get_digit_sum(int(test * power))
        
        
print (s)
