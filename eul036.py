import eul


def eul36(n):
    """Find the sum of all numbers, less than n = one million, which are palindromic in base 10 and base 2."""
    return sum([x for x in range(1, n + 1) if eul.palindrome(x) and eul.palindrome(str(bin(x))[2:])])

print(eul36(1000000))
# 872187
