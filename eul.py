import math
import numpy
from functools import reduce


# ---------------------------------------------------------------------------------------
# DIGIT FUNCTIONS
# ---------------------------------------------------------------------------------------

def get_digit_sum(n):
    """Returns sum of digits by converting to string"""
    return sum(int(digit) for digit in str(n))


def get_digits(n):
    return [int(i) for i in str(n)]


# ---------------------------------------------------------------------------------------
# DIVISOR FUNCTIONS
# ---------------------------------------------------------------------------------------

def get_proper_divisors(n):
    return {x for x in range(1, (n + 1) // 2 + 1) if n % x == 0 and n != x}
    

def get_factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def get_prime_factors(n):
    primes = sieve(int(math.sqrt(n)) + 1)
    factors, i = [], 0
    while n > 1:
        while n % primes[i] == 0:
            factors.append(primes[i])
            n /= primes[i]
        i += 1
    return factors


# ---------------------------------------------------------------------------------------
# PRIME NUMBER FUNCTIONS
# ---------------------------------------------------------------------------------------

def sieve(n):
    # returns all primes between 2 and n
    s = [True]*(n + 1)
    s[0], s[1] = False, False

    for i in range(2, int(math.sqrt(n))):
        curr = i + i
        while curr <= n:
            s[curr] = False
            curr += i
    return [i for i in range(len(s)) if s[i] is True]


def sieve8(n):
    """Return an array of the primes below n."""
    prime = numpy.ones(n//3 + (n % 6 == 2), dtype=numpy.bool)
    for i in range(3, int(n**.5) + 1, 3):
        if prime[i // 3]:
            p = (i + 1) | 1
            prime[p*p//3::2*p] = False
            prime[p*(p-2*(i & 1)+4)//3::2*p] = False
    result = (3 * prime.nonzero()[0] + 1) | 1
    result[0] = 3
    return numpy.r_[2, result]


def palindrome(n):
    return True if (str(n))[::-1] == str(n) else False
