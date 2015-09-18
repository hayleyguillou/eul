import eul


def eul7(n):
    """What is the n = 10001st prime number?"""
    i, primes = 1, eul.sieve(10)
    while len(primes) <= n:
        i += 1
        primes = eul.sieve(10**i)

    return primes[n-1]

print(eul7(10001))
# 104743
