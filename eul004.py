import eul


def eul4(n):
    """Find the largest palindrome made from the product of two n=3-digit numbers."""
    return max([x * y for x in range(10 ** (n - 1), 10 ** n) for y in
                range(10 ** (n - 1), 10 ** n) if eul.palindrome(x * y)])

print(eul4(3))
# 906609
