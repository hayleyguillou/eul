import eul
import functools
import operator


def eul1():
    """Find the sum of all the multiples of 3 or 5 below 1000."""
    return sum([x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0])


def eul2():
    """By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the
    even-valued terms."""
    a, b, fib = 1, 2, []
    while b < 4000000:
        a, b = b, a + b
        fib.append(a)

    return sum([x for x in fib if x % 2 == 0])


def eul3():
    """What is the largest prime factor of the number 600851475143 ?"""
    return max(eul.get_prime_factors(600851475143))


def eul4():
    """Find the largest palindrome made from the product of two 3-digit numbers."""
    return max([x * y for x in range(100, 1000) for y in range(100, 1000) if eul.palindrome(x * y)])


def eul6():
    """Find the difference between the sum of the squares of the first one hundred natural numbers and the
    square of the sum."""
    return sum([x for x in range(1, 101)]) ** 2 - sum([x ** 2 for x in range(1, 101)])


def eul7():
    """What is the 10001st prime number?"""
    i, primes = 1, eul.sieve(10)
    while len(primes) <= 10001:
        i += 1
        primes = eul.sieve(10 ** i)
    return primes[10000]


def eul8():
    """Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
    What is the value of this product?"""
    test = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858' + \
           '6156078911294949545950173795833195285320880551112540698747158523863050715693290963295227443043557668966' + \
           '4895044524452316173185640309871112172238311362229893423380308135336276614282806444486645238749303589072' + \
           '9629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010' + \
           '5336788122023542180975125454059475224352584907711670556013604839586446706324415722155397536978179778461' + \
           '7406495514929086256932197846862248283972241375657056057490261407972968652414535100474821663704844031998' + \
           '9000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294' + \
           '7654568284891288314260769004224219022671055626321111109370544217506941658960408071984038509624554443629' + \
           '8123098787992724428490918884580156166097919133875499200524063689912560717606058861164671094050775410022' + \
           "5698315520005593572972571636269561882670428252483600823257530420752963450"
    return max([functools.reduce(operator.mul, [int(x) for x in word], 1) for word in
                [test[i:i + 13] for i in range(len(test) - 13)]])


def eul9():
    """There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc."""
    for a in range(1, int(1000 / 2)):
        for b in range(1, 1000 - (2 * a)):
            c = 1000 - a - b
            if (a ** 2) + (b ** 2) == (c ** 2):
                return a * b * c


def eul10():
    """Find the sum of all the primes below two million."""
    return sum(eul.sieve(2000000))


def eul12():
    """What is the value of the first triangle number to have over five hundred divisors?"""
    total = 1
    curr = 2
    while len(eul.get_factors(total)) < 500:
        total += curr
        curr += 1
    return total


def eul14():
    """n → n/2 (n is even)
       n → 3n + 1 (n is odd)
       Which starting number, under one million, produces the longest chain?"""
    chains = [0] * 1000001
    for i in range(1, 1000000):
        chain = 1
        num = i
        while i > 1:
            if i % 2 != 0:
                i = 3 * i + 1
            else:
                i /= 2
            chain += 1
        chains[num] = chain
    return chains.index(max(chains))


def eul16():
    """What is the sum of the digits of the number 2^n = 1000?"""
    return sum([x for x in eul.get_digits(2 ** 1000)])


def eul20():
    """Find the sum of the digits in the number n = 100!"""
    return sum(int(digit) for digit in str(math.factorial(100)))


print("Euler solution 1:   ", eul1())
print("Euler solution 2:   ", eul2())
print("Euler solution 3:   ", eul3())
print("Euler solution 4:   ", eul4())
print("Euler solution 6:   ", eul6())
print("Euler solution 7:   ", eul7())
print("Euler solution 8:   ", eul8())
print("Euler solution 9:   ", eul9())
print("Euler solution 10:  ", eul10())
print("Euler solution 12:  ", eul12())
print("Euler solution 14:  ", eul14())
print("Euler solution 16:  ", eul16())
