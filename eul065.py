def get_digit_sum(n):
    """Returns sum of digits by converting to string"""
    return sum(int(digit) for digit in str(n))

level = 100
num, den = 0,1
for i in range(level,0,-1):
    if i == 1:
        num += 2 * den
    elif i%3 == 0:
        num += (2/3 * i) * den
        num,den = den,num
    else:
        num += den
        num,den = den,num
print(level,":",num,"/",den)
print(num)
print(get_digit_sum(num))
