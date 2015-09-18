def eul9(n):
    """There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc."""
    for a in range(1, int(n/2)):
        for b in range(1, n - (2 * a)):
            c = n - a - b
            if (a ** 2) + (b ** 2) == (c ** 2):
                return a * b * c

print(eul9(1000))
# 31875000
