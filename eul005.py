import eul
import math
import functools
import operator


def eul5(n):
    """What is the smallest positive number that is evenly divisible by all of the numbers from 1 to n = 20?"""
    primer = functools.reduce(operator.mul, eul.sieve(n), 1)
    for i in range(primer, math.factorial(n) + 1, primer):
        divisible = True
        for factor in range(1, n+1):
            if i % factor != 0:
                divisible = False
                break
        if divisible:
            return i
    return math.factorial(n)


print(eul5(20))
# 232792560
