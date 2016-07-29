import math
from eul import prime


def eul27():
    """Find the product of the coefficients, a and b, for the quadratic expression (n^2+n+41)
    that produces the maximum number of primes for consecutive values of n, starting with n=0."""

    max_n = -1
    max_prod = (0, 0)
    y = 1000

    for a in range(-y, y+1):
        for b in range(-y, y+1):
            n = 0
            prod = n**2 + (a*n) + b
            while prime(prod):
                n += 1
                prod = n**2 + (a*n) + b
            if n > max_n:
                max_n = n
                max_prod = a * b

    return max_prod
            
print(eul27())
# -59231
