import eul


def eul21(n):
    """Evaluate the sum of all the amicable numbers under n = 10000."""
    return sum([x for x in range(1, n) if
                x != sum(eul.get_proper_divisors(x)) and sum(
                    eul.get_proper_divisors(sum(eul.get_proper_divisors(x)))) == x])


print(eul21(10000))
# 31626
