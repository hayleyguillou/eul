import math


# TODO: Optimize
def eul44():
    """Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal
    and D = |Pk − Pj| is minimised; what is the value of D?"""
    ps = [((p * (3 * p - 1)) / 2) for p in range(1, 3000)]

    for p in ps:
        for q in ps[ps.index(p):]:
            if (p + q) in ps and math.fabs(p - q) in ps:
                print(math.fabs(p - q))


eul44()
# 5482660
