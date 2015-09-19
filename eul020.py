import math


def eul20(n):
    """Find the sum of the digits in the number n = 100!"""
    return sum(int(digit) for digit in str(math.factorial(n)))

print(eul20(100))
# 648
