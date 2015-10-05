from itertools import permutations


def eul43():
    """Find the sum of all 0 to 9 pandigital numbers with this property (See online)"""
    def is_divisible(p):
        divisors = [2, 3, 5, 7, 11, 13, 17]
        for i in range(0, len(divisors)):
            num = 100 * int(p[i + 1]) + 10 * int(p[i + 2]) + int(p[i + 3])
            if num % divisors[i] != 0:
                return False
        return True

    init = [''.join(p) for p in permutations('0123456789') if p[0] != '0' and p[5] == '5' and int(p[3]) % 2 == 0]
    return sum([int(p) for p in init if is_divisible(p)])


print(eul43())
# 16695334890
