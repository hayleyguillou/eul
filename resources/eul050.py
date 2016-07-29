from eul import sieve


def eul50(n):
    """Which prime, below n = one-million, can be written as the sum of the most consecutive primes?"""
    primes = sieve(n)
    consecutive = 0
    maximum = 0

    for start in range(0, len(primes) - 2):
        r = 2 + consecutive
        for num in range(r, len(primes) - start):
            test = sum(primes[i] for i in range(start, start + num))
            if test > n:
                break
            if test in primes and num > consecutive:
                consecutive = num
                maximum = test
    return maximum

print(eul50(1000000))
# 997651
