import eul


def eul47():
    """Find the first four consecutive integers to have four distinct prime factors.
    What is the first of these numbers?"""
    curr_n = 0
    primes = eul.sieve(200000)
    for n in range(20000, 200000):
        if eul.num_prime_factors(primes, n) != 4:
            curr_n = 0
        elif not curr_n:
            curr_n = n
        elif n - curr_n == 3:
            return curr_n


print(eul47())
# 134043
