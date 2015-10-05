import eul


def eul41():
    """What is the largest n-digit pandigital prime that exists?"""
    for p in range(7654321, 1, -2):
        if eul.pandigital(p, 7) and eul.prime(p):
            return p


print(eul41())
# 7652413
