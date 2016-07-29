from eul import prime


def eul58(n):
    """See web for spiral pattern.
     If this process is continued, what is the side length of the square spiral for which the ratio of primes
     along both diagonals first falls below n = 10%?"""
    num_diag = 5
    num_primes = 3
    curr = 9
    adder = 4

    while num_primes/num_diag > n/100:
        for j in range(4):
            curr += adder
            num_diag += 1
            if prime(curr):
                num_primes += 1
        adder += 2

    return adder - 1

print(eul58(10))
# 26241
