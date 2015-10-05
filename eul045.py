import eul


def eul45bf():
    """Find the next triangle number that is also pentagonal and hexagonal."""
    T, H, P = set(), set(), set()
    for n in range(1, 200000):
        t = n + 285
        p = n + 165
        h = n + 143
        T.add((t * (t + 1)) / 2)
        P.add((p * (3 * p - 1)) / 2)
        H.add(h * (2 * h - 1))
    return (T & H & P).pop()


# all triangular number based on an odd n is a hexagonal numbers
def eul45():
    """Find the next triangle number that is also pentagonal and hexagonal."""
    i = 143
    while i:
        i += 1
        hexagonal = i * (2 * i - 1)
        if eul.pentagonal(hexagonal):
            return hexagonal


print(eul45())
# 1533776805
