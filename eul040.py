from functools import reduce
from operator import mul


def eul40(n):
    """An irrational decimal fraction is created by concatenating the positive integers: 0.123456789101112131415...
    If dn represents the nth digit of the fractional part, find the value of the following expression.
    d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000..., i.e., (10^1,...n)"""
    num = ''.join([str(x) for x in range(0, 1000000)])
    return reduce(mul, [int(num[10 ** n]) for n in range(0, n)], 1)


print(eul40(6))
# 210
