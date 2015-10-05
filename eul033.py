import math
import eul


def eul33():
    """If the product of these four fractions is given in its lowest common terms, find the value of the denominator."""
    fracs = []
    for d in range(10, 100):
        for n in range(10, d):
            common = set(eul.get_digits(n)).intersection(eul.get_digits(d))
            for digit in common:
                if digit:
                    r_n = int(str(n).replace(str(digit), "", 1))
                    r_d = int(str(d).replace(str(digit), "", 1))
                    if r_d and r_n / r_d == n / d:
                        fracs.append((n, d))
    n = d = 1
    for frac in fracs:
        n *= frac[0]
        d *= frac[1]

    return d / math.gcd(n, d)


print(eul33())
