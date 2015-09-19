import eul


def eul23():
    """Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers."""
    upper = 28123
    abundants = set([x for x in range(12, upper) if sum(eul.get_proper_divisors(x)) > x])
    abundant_sums = set([(i + j) for i in abundants for j in abundants if i+j < upper])
    return sum(set([x for x in range(1, upper)]) - abundant_sums)

print(eul23())
# 4179871
