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


def num_len(n):
    return int(math.log10(n)) + 1


def pandigital(n, s=9):
    n = str(n)
    return len(n) == s and not '1234567890'[:s].strip(n)


def odd(n):
    return True if len([d for d in str(n) if int(d) % 2 == 0]) == 0 else False


# ---------------------------------------------------------------------------------------
# DIVISOR FUNCTIONS
# ---------------------------------------------------------------------------------------

def get_proper_divisors(n):
    return {x for x in range(1, (n + 1) // 2 + 1) if n % x == 0 and n != x}


def get_factors(n):
    return set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))


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
    s = [True] * (n + 1)
    s[0], s[1] = False, False

    for i in range(2, int(math.sqrt(n))):
        curr = i + i
        while curr <= n:
            s[curr] = False
            curr += i
    return [i for i in range(len(s)) if s[i] is True]


def prime(n):
    n = int(n)
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(math.sqrt(n))
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True


# ---------------------------------------------------------------------------------------
# OTHER NUMBER FUNCTIONS
# ---------------------------------------------------------------------------------------


def palindrome(n):
    return True if (str(n))[::-1] == str(n) else False


def pentagonal(n):
    p = (math.sqrt(24 * n + 1) + 1)/6
    return int(p) == p
