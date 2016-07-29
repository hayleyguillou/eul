import math


def eul53():
    """How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?"""
    fac = math.factorial
    count = 0
    for n in range(23, 101):
        for r in range(n, 0, -1):
            val = fac(n)/(fac(r)*fac(n-r))
            if val > 1000000:
                count += 1
    return count

print(eul53())
# 4075
