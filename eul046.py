import eul
import math


def eul46():
    """What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?"""
    primes = eul.sieve(10000)
    squares = [x**2 for x in range(1, int(math.sqrt(10000/2)))]

    for i in range(25, 10000, 2):
        if i not in primes:
            possibles = [p for p in primes if p < i]
            works = False
            for p in possibles:
                test = i
                test -= p
                if test/2 == int(test/2) and test/2 in squares:
                    works = True
                    break
            if not works:
                return i


print(eul46())
# 5777
