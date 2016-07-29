import itertools
from eul import sieve


def eul49(n):
    """What 12-digit number do you form by concatenating the three n=4-digit terms in this sequence where
     (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another?"""
    primes = sieve(10**n)
    for prime in primes:
        if prime > 10**(n-1):
            perms = set([int(''.join(p)) for p in itertools.permutations(str(prime)) if int(''.join(p)) > 10**(n-1)])
            inter = sorted(list(perms.intersection(primes)))
            if len(inter) >= 3:
                for combo in itertools.combinations(inter, 3):
                    if combo[0] != 1487 and combo[2]-combo[1] == combo[1]-combo[0]:
                        return ''.join(sorted([str(p) for p in combo]))

print(eul49(4))
# 296962999629
