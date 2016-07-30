"""The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating
them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime.
The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime."""
from eul import sieve, append_ints, prime


# 4 deep trees???

def check(m, n):
    return prime(append_ints(m, n)) and prime(append_ints(n, m))


def check_list(lst, oks, prime):
    for p in lst:
        if p in oks:
            continue
        if not check(p, prime):
            return False
    return True


checker = [set() for _ in range(10000)]



def eul60():
    primes = sieve(10000)
    sums = [999999999]

    for i in range(len(primes)):
        prime1 = primes[i]
        lists = []
        for j in range(i+1, len(primes)):
            prime2 = primes[j]

            if prime2 in checker[prime1] or check(prime1, prime2):
                checker[prime2].add(prime1)
                for k in range(len(lists)):
                    lst = lists[k]
                    if sum(lst)+prime2 > min(sums):
                        continue
                    if check_list(lst, checker[prime2], prime2):
                        checker[prime2] |= set(lst)
                        lst.append(prime2)
                lists.append([prime1, prime2])
                #print(lists)
        for lst in lists:
            if len(lst) == 5:
                sums.append(sum(lst))
        print(prime1, sums)

    return min(sums)



print(eul60())
