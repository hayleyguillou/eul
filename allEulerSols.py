import eul
import math
import functools
import operator
import itertools


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


def eul5():
    """What is the smallest positive number that is evenly divisible by all of the numbers from 1 to n = 20?"""
    primer = functools.reduce(operator.mul, eul.sieve(20), 1)
    for i in range(primer, math.factorial(20) + 1, primer):
        divisible = True
        for factor in range(1, 20+1):
            if i % factor != 0:
                divisible = False
                break
        if divisible:
            return i
    return math.factorial(20)


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


def eul11():
    """What is the greatest product of four adjacent numbers in the same direction
    (up, down, left, right, or diagonally) in the 20×20 grid (largestProduct.txt)?"""
    text_file = open("resources/largestProduct.txt", "r")
    data = [[int(n) for n in line.split()] for line in text_file]
    text_file.close()

    max_product = 0
    # rows/columns
    for i in range(20):
        for j in range(16):
            product = data[i][j] * data[i][j + 1] * data[i][j + 2] * data[i][j + 3]
            if product > max_product:
                max_product = product
            product = data[j][i] * data[j + 1][i] * data[j + 2][i] * data[j + 3][i]
            if product > max_product:
                max_product = product

    # diagonals
    for i in range(16):
        for j in range(16):
            product = data[i][j] * data[i + 1][j + 1] * data[i + 2][j + 2] * data[i + 2][j + 3]
            if product > max_product:
                max_product = product
            product = data[i][19 - j] * data[i + 1][18 - j] * data[i + 2][17 - j] * data[i + 3][16 - j]
            if product > max_product:
                max_product = product

    return max_product


def eul12():
    """What is the value of the first triangle number to have over five hundred divisors?"""
    total = 1
    curr = 2
    while len(eul.get_factors(total)) < 500:
        total += curr
        curr += 1
    return total


def eul13():
    """Work out the first ten digits of the sum of the following one-hundred 50-digit numbers (largeSum.txt)"""
    text_file = open("resources/largeSum.txt", "r")
    data = [int(n) for n in text_file]
    text_file.close()
    return int(str(sum(data))[0:10])


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


def eul21():
    """Evaluate the sum of all the amicable numbers under 10000."""
    return sum([x for x in range(1, 10000) if
                x != sum(eul.get_proper_divisors(x)) and sum(
                    eul.get_proper_divisors(sum(eul.get_proper_divisors(x)))) == x])


def eul23():
    """Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers."""
    upper = 28123
    abundants = set([x for x in range(12, upper) if sum(eul.get_proper_divisors(x)) > x])
    abundant_sums = set([(i + j) for i in abundants for j in abundants if i + j < upper])
    return sum(set([x for x in range(1, upper)]) - abundant_sums)


def eul24():
    """What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?"""
    return sorted([''.join(p) for p in itertools.permutations('0123456789')])[1000000 - 1]


def eul25():
    """What is the index of the first term in the Fibonacci sequence to contain 1000 digits?"""
    index, a, b = 1, 0, 1
    while eul.num_len(b) < 1000:
        a, b = b, a + b
        index += 1
    return index


def eul29():
    """How many distinct terms are in the sequence generated by a^b for 2 ≤ a ≤ n =100 and 2 ≤ b ≤ n = 100?"""
    return len(set([(a ** b) for a in range(2, 101) for b in range(2, 101)]))


def eul30():
    """Find the sum of all the numbers that can be written as the sum of fifth powers of their digits."""
    return sum([x for x in range(2, 1000000) if sum([y ** 5 for y in eul.get_digits(x)]) == x])


def eul34():
    """Find the sum of all numbers which are equal to the sum of the factorial of their digits."""
    return sum([i for i in range(3, 100000) if sum([math.factorial(x) for x in eul.get_digits(i)]) == i])


def eul36():
    """Find the sum of all numbers, less than n = one million, which are palindromic in base 10 and base 2."""
    return sum([x for x in range(1, 1000001) if eul.palindrome(x) and eul.palindrome(str(bin(x))[2:])])


def eul38():
    """What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer
     with (1,2, ... , n) where n > 1?"""
    pandigitals = []
    check = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    for n in range(1, 100000):
        concat, i = "", 1
        while len(concat) < 10:
            concat += str(n * i)
            if len(concat) == 9:
                if set([int(x) for x in concat]) == check:
                    pandigitals.append(int(concat))
            i += 1
    return max(pandigitals)


def eul40():
    """An irrational decimal fraction is created by concatenating the positive integers: 0.123456789101112131415...
    If dn represents the nth digit of the fractional part, find the value of the following expression.
    d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000"""
    num = ''.join([str(x) for x in range(0, 1000000)])
    return functools.reduce(operator.mul, [int(num[10 ** n]) for n in range(0, 6)], 1)


print("Euler solution 1:   ", eul1())
print("Euler solution 2:   ", eul2())
print("Euler solution 3:   ", eul3())
print("Euler solution 4:   ", eul4())
print("Euler solution 5:   ", eul5())
print("Euler solution 6:   ", eul6())
print("Euler solution 7:   ", eul7())
print("Euler solution 8:   ", eul8())
print("Euler solution 9:   ", eul9())
print("Euler solution 10:  ", eul10())
print("Euler solution 11:  ", eul11())
print("Euler solution 12:  ", eul12())
print("Euler solution 13:  ", eul13())
print("Euler solution 14:  ", eul14())
print("Euler solution 16:  ", eul16())
print("Euler solution 20:  ", eul20())
print("Euler solution 21:  ", eul21())
print("Euler solution 23:  ", eul23())
print("Euler solution 24:  ", eul24())
print("Euler solution 25:  ", eul25())
print("Euler solution 29:  ", eul29())
print("Euler solution 30:  ", eul30())
print("Euler solution 34:  ", eul34())
print("Euler solution 36:  ", eul36())
print("Euler solution 38:  ", eul38())
print("Euler solution 40:  ", eul40())
