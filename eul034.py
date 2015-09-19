import math
import eul


def eul34():
    """Find the sum of all numbers which are equal to the sum of the factorial of their digits."""
    return sum([i for i in range(3, 100000) if sum([math.factorial(x) for x in eul.get_digits(i)]) == i])


print(eul34())
# 40730
