import eul


def eul35(n):
    """How many circular primes are there below n = one million?"""
    def check_digits(m):
        while m > 0:
            digit = m % 10
            if digit == 5 or digit % 2 == 0:
                return False
            m = int(m / 10)
        return True

    primes = [p for p in eul.sieve(n) if check_digits(p)]

    circulars = {2, 5}
    for prime in primes:
        if prime not in circulars:
            perms = {prime}
            for i in range(0, len(str(prime)) - 1):
                prime = int(str(prime)[1:]) * 10 + int(str(prime)[0])
                perms.add(prime)
            circular = True
            for perm in perms:
                if perm not in primes:
                    circular = False
                    break
            if circular:
                circulars.update(perms)
    return len(circulars)


print(eul35(1000000))
