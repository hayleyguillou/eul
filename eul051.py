import re
from itertools import product
from collections import Counter
from eul import sieve


def eul51(n):
    """Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits)
    with the same digit, is part of an n = eight prime value family."""

    digits = 6  # for n = 8, assume 6 digit prime family
    primes = " ".join([str(i) for i in sieve(10**digits) if i > 10**(digits-1)])
    combos = product(range(2), repeat=digits)

    for combo in combos:
        if len(set(combo)) == 1:
            continue
        possibilities = []
        for i in range(10):
            reg = r""
            for digit in range(digits):
                if combo[digit] == 1:
                    reg += "["+str(i)+"]"
                else:
                    reg += "\d"
            p = re.compile(reg)
            possibilities.extend(p.findall(primes))

        for i in range(digits):
            if combo[i] == 1:
                n_p = []
                for p in possibilities:
                    l = list(p)
                    l[i] = "*"
                    n_p.append("".join(l))
                possibilities = n_p
        c = Counter(possibilities)
        if c.most_common(1)[0][1] == n:
            num = c.most_common(1)[0][0]
            reg = r""
            f = True
            for i in num:
                if i == "*":
                    if f:
                        reg += r"(\d)"
                        f = False
                    else:
                        reg += r"\1"
                else:
                    reg += r"["+str(i)+r"]"
            p = re.compile(reg)
            return min([x.group(0) for x in p.finditer(primes)])

print(eul51(8))
# 121313
