import math
import eul


# BF method
def eul44bf():
    """Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal
    and D = |Pk − Pj| is minimised; what is the value of D?"""
    ps = [((p * (3 * p - 1)) / 2) for p in range(1, 3000)]

    for p in ps:
        for q in ps[ps.index(p):]:
            if (p + q) in ps and math.fabs(p - q) in ps:
                print(math.fabs(p - q))


# using inverse method
def eul44():
    """Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal
    and D = |Pk − Pj| is minimised; what is the value of D?"""
    for i in range(2,3000):
        n = i * (3 * i - 1) / 2
        for j in range(i - 1, 0, -1):
            m = j * (3 * j - 1) / 2
            if eul.pentagonal(n - m) and eul.pentagonal(n + m):
                return int(n-m)


print(eul44())
# 5482660
