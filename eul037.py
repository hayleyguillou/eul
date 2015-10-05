import eul


def eul37():
    """Find the sum of the only eleven primes that are both truncatable from left to right and right to left."""
    primes = [p for p in eul.sieve(1000000) if eul.odd(p)]
    truncs = {23}
    index = 4
    while index < len(primes):
        left = right = primes[index]
        prime = True
        while left > 0 and prime:
            if left not in primes:
                prime = False
            left = int(left/10)

        if prime:
            iterator = 10
            while iterator < right:
                if right % iterator not in primes:
                    prime = False
                iterator *= 10

        if prime:
            truncs.add(primes[index])
        index += 1

    return sum(truncs)


print(eul37())
# 748317
