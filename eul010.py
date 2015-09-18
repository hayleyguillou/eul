import eul


def eul10(n):
    """Find the sum of all the primes below n = two million."""
    return sum(eul.sieve(n))

print(eul10(2000000))
# 142913828922
