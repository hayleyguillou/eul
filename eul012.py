import eul


def eul12(n):
    """What is the value of the first triangle number to have over n = five hundred divisors?"""
    total = 1
    curr = 2
    while len(eul.get_factors(total)) < n:
        total += curr
        curr += 1
    return total

print(eul12(500))
# 76576500
