from itertools import permutations


def eul24(n):
    """What is the n = millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?"""
    return sorted([''.join(p) for p in permutations('0123456789')])[n - 1]


def eul24bf():
    """What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?"""
    maximum = 10

    checker = [False] * maximum
    num = 1
    for a in range(0, maximum):
        checker[a] = True
        for b in range(0, maximum):
            if not checker[b]:
                checker[b] = True
                for c in range(0, maximum):
                    if not checker[c]:
                        checker[c] = True
                        for d in range(0, maximum):
                            if not checker[d]:
                                checker[d] = True
                                for e in range(0, maximum):
                                    if not checker[e]:
                                        checker[e] = True
                                        for f in range(0, maximum):
                                            if not checker[f]:
                                                checker[f] = True
                                                for g in range(0, maximum):
                                                    if not checker[g]:
                                                        checker[g] = True
                                                        for h in range(0, maximum):
                                                            if not checker[h]:
                                                                checker[h] = True
                                                                for i in range(0, maximum):
                                                                    if not checker[i]:
                                                                        checker[i] = True
                                                                        for j in range(0, maximum):
                                                                            if not checker[j]:
                                                                                checker[j] = True
                                                                                if num % 1000000 == 0:
                                                                                    return int(
                                                                                        str(a) + str(b) + str(c) + str(
                                                                                            d) + str(e) + str(f) + str(
                                                                                            g) + str(h) + str(i) + str(
                                                                                            j))
                                                                                num += 1
                                                                                checker[j] = False
                                                                        checker[i] = False
                                                                checker[h] = False
                                                        checker[g] = False
                                                checker[f] = False
                                        checker[e] = False
                                checker[d] = False
                        checker[c] = False
                checker[b] = False
        checker[a] = False


print(eul24(1000000))
# 2783915460
