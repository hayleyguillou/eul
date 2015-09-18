import eul


def eul3(n):
    """What is the largest prime factor of the number n = 600851475143 ?"""
    return max(eul.get_prime_factors(n))


print(eul3(600851475143))
# 6857
