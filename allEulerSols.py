import eul
import math
import functools
import operator
import itertools
import calendar
import re
import collections


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
        for factor in range(1, 20 + 1):
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


def eul15():
    """How many such routes are there through a 20×20 grid?"""
    d = [[1 for x in range(20 + 1)] for x in range(20 + 1)]
    for i in range(1, 20 + 1):
        for j in range(1, 20 + 1):
            d[i][j] = d[i - 1][j] + d[i][j - 1]
    return d[20][20]


def eul16():
    """What is the sum of the digits of the number 2^n = 1000?"""
    return sum([x for x in eul.get_digits(2 ** 1000)])


def eul17():
    """If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
    how many letters would be used?"""

    def get_digits(i):
        three = {1, 2, 6, 10}
        four = {4, 5, 9}
        five = {3, 7, 8, 40, 50, 60}
        six = {11, 12, 20, 30, 80, 90}
        seven = {15, 16, 70}
        eight = {13, 14, 18, 19}
        nine = {17}

        if i in three:
            return 3
        elif i in four:
            return 4
        elif i in five:
            return 5
        elif i in six:
            return 6
        elif i in seven:
            return 7
        elif i in eight:
            return 8
        elif i in nine:
            return 9
        else:
            return 0

    def inspect_num(m):
        digits = get_digits(m)

        if m == 1000:
            return 11
        elif m == 0:
            return 0
        elif digits != 0:
            return digits

        else:
            if m > 99:
                if m % 100 == 0:
                    return get_digits(int(m / 100)) + 7
                else:
                    return get_digits(int(m / 100)) + 10 + inspect_num(m % 100)
            else:
                return get_digits(m - (m % 10)) + inspect_num(m % 10)

    num = 0
    for d in range(1, 1000 + 1):
        num += inspect_num(d)
    return num


def eul18():
    """Find the maximum total from top to bottom of the triangle below (maximumPath1.txt):"""
    text_file = open("resources/maximumPath1.txt", "r")
    data = [[int(n) for n in line.split()] for line in text_file]
    text_file.close()

    for i in range(len(data) - 2, -1, -1):
        for j in range(len(data[i])):
            data[i][j] += max(data[i + 1][j], data[i + 1][j + 1])
    return data[0][0]


def eul19():
    """How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?"""
    return len([(year, month) for year in range(1901, 2000 + 1) for month in range(1, 12 + 1)
                if calendar.weekday(year, month, 1) == 6])


def eul20():
    """Find the sum of the digits in the number n = 100!"""
    return sum(int(digit) for digit in str(math.factorial(100)))


def eul21():
    """Evaluate the sum of all the amicable numbers under 10000."""
    return sum([x for x in range(1, 10000) if
                x != sum(eul.get_proper_divisors(x)) and sum(
                    eul.get_proper_divisors(sum(eul.get_proper_divisors(x)))) == x])


def eul22():
    """What is the total of all the name scores in the file (names.txt)?"""
    with open('resources/names.txt') as f:
        names = f.read().split(',')
        names.sort()
    return sum(i * sum(ord(c) - 64 for c in x.strip('"')) for i, x in enumerate(names, 1))


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


def eul26():
    """Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part."""
    chain = 0
    d = 0

    for i in range(1000, -1, -1):
        if chain > i:
            break

        remainders = [0] * i
        value = 1
        position = 0

        while remainders[value] == 0 and value != 0:
            remainders[value] = position
            value *= 10
            value %= i
            position += 1

        if position - remainders[value] > chain:
            chain = position - remainders[value]
            d = i
    return d


def eul27():
    """Find the product of the coefficients, a and b, for the quadratic expression (n^2+n+41)
    that produces the maximum number of primes for consecutive values of n, starting with n=0."""

    max_n = -1
    max_prod = (0, 0)
    y = 1000

    for a in range(-y, y+1):
        for b in range(-y, y+1):
            n = 0
            prod = n**2 + (a*n) + b
            while eul.prime(prod):
                n += 1
                prod = n**2 + (a*n) + b
            if n > max_n:
                max_n = n
                max_prod = a * b
    return max_prod


def eul28():
    """What is the sum of the numbers on the diagonals in a 1001 * 1001 spiral formed by
    starting with the number 1 and moving to the right in a clockwise direction?"""
    sq_size = 1001
    iterations = int((sq_size - 1) / 2)
    s, curr, adder = 1, 1, 2

    for i in range(iterations):
        for j in range(4):
            curr += adder
            s += curr
        adder += 2
    return s


def eul29():
    """How many distinct terms are in the sequence generated by a^b for 2 ≤ a ≤ n =100 and 2 ≤ b ≤ n = 100?"""
    return len(set([(a ** b) for a in range(2, 101) for b in range(2, 101)]))


def eul30():
    """Find the sum of all the numbers that can be written as the sum of fifth powers of their digits."""
    return sum([x for x in range(2, 1000000) if sum([y ** 5 for y in eul.get_digits(x)]) == x])


def eul31():
    """How many different ways can n = 200p be made using any number of coins?"""
    target = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [0] * (target + 1)
    ways[0] = 1

    for i in range(len(coins)):
        for j in range(coins[i], target + 1):
            ways[j] += ways[j - coins[i]]

    return ways[target]


def eul32():
    """"Find the sum of all products whose multiplicand/multiplier/product identity can be written as a
    1 through 9 pandigital."""
    products = set()
    for product in range(1000, 10000):
        if len(set(eul.get_digits(product))) == len(str(product)):
            for i in eul.get_proper_divisors(product):
                j = int(product / i)
                test = ''.join([str(i), str(j), str(i * j)])
                if len(test) == 9 and eul.pandigital(test):
                    products.add(i * j)
    return sum(products)


def eul33():
    """If the product of these four fractions is given in its lowest common terms, find the value of the denominator."""
    fracs = []
    for d in range(10, 100):
        for n in range(10, d):
            common = set(eul.get_digits(n)).intersection(eul.get_digits(d))
            for digit in common:
                if digit:
                    r_n = int(str(n).replace(str(digit), "", 1))
                    r_d = int(str(d).replace(str(digit), "", 1))
                    if r_d and r_n / r_d == n / d:
                        fracs.append((n, d))
    n = d = 1
    for frac in fracs:
        n *= frac[0]
        d *= frac[1]
    return d / math.gcd(n, d)


def eul34():
    """Find the sum of all numbers which are equal to the sum of the factorial of their digits."""
    return sum([i for i in range(3, 100000) if sum([math.factorial(x) for x in eul.get_digits(i)]) == i])


def eul35():
    """How many circular primes are there below one million?"""

    def check_digits(m):
        while m > 0:
            digit = m % 10
            if digit == 5 or digit % 2 == 0:
                return False
            m = int(m / 10)
        return True

    primes = [p for p in eul.sieve(1000000) if check_digits(p)]

    circulars = {2, 5}
    for prime in primes:
        if prime not in circulars:
            perms = {prime}
            for i in range(0, len(str(prime)) - 1):
                prime = int(str(prime)[1:]) * 10 + int(str(prime)[0])
                perms.add(prime)
            circular = True
            for perm in perms:
                if perm not in primes:
                    circular = False
                    break
            if circular:
                circulars.update(perms)
    return len(circulars)


def eul36():
    """Find the sum of all numbers, less than n = one million, which are palindromic in base 10 and base 2."""
    return sum([x for x in range(1, 1000001) if eul.palindrome(x) and eul.palindrome(str(bin(x))[2:])])


def eul37():
    """Find the sum of the only eleven primes that are both truncatable from left to right and right to left."""
    primes = [p for p in eul.sieve(1000000) if eul.odd(p)]
    truncs = {23}
    index = 4
    while index < len(primes):
        left = right = primes[index]
        prime = True
        while left > 0 and prime:
            if left not in primes:
                prime = False
            left = int(left / 10)

        if prime:
            iterator = 10
            while iterator < right:
                if right % iterator not in primes:
                    prime = False
                iterator *= 10

        if prime:
            truncs.add(primes[index])
        index += 1

    return sum(truncs)


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


def eul39():
    """For which value of p ≤ 1000, is the number of solutions maximised?"""
    max_sols = 0
    result = 0

    for p in range(2, 1001, 2):
        sols = 0
        for a in range(2, int(p / 3)):
            if p * (p - 2 * a) % (2 * (p - a)) == 0:
                sols += 1
        if sols > max_sols:
            max_sols = sols
            result = p
    return result


def eul40():
    """An irrational decimal fraction is created by concatenating the positive integers: 0.123456789101112131415...
    If dn represents the nth digit of the fractional part, find the value of the following expression.
    d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000"""
    num = ''.join([str(x) for x in range(0, 1000000)])
    return functools.reduce(operator.mul, [int(num[10 ** n]) for n in range(0, 6)], 1)


def eul41():
    """What is the largest n-digit pandigital prime that exists?"""
    for p in range(7654321, 1, -2):
        if eul.pandigital(p, 7) and eul.prime(p):
            return p


def eul42():
    """Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common
    English words, how many are triangle words?"""

    with open('resources/p042_words.txt') as f:
        words = f.read().replace("\"", "").split(',')
        words.sort()

    triangles = [(0.5 * (i * (i + 1))) for i in range(50)]
    count = 0
    for word in words:
        if sum([ord(letter.lower()) - ord('a') + 1 for letter in word]) in triangles:
            count += 1
    return count


def eul43():
    """Find the sum of all 0 to 9 pandigital numbers with this property (See online)"""

    def is_divisible(p):
        divisors = [2, 3, 5, 7, 11, 13, 17]
        for i in range(0, len(divisors)):
            num = 100 * int(p[i + 1]) + 10 * int(p[i + 2]) + int(p[i + 3])
            if num % divisors[i] != 0:
                return False
        return True

    init = [''.join(p) for p in itertools.permutations('0123456789') if
            p[0] != '0' and p[5] == '5' and int(p[3]) % 2 == 0]
    return sum([int(p) for p in init if is_divisible(p)])


def eul44():
    """Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal
    and D = |Pk − Pj| is minimised; what is the value of D?"""
    for i in range(2, 3000):
        n = i * (3 * i - 1) / 2
        for j in range(i - 1, 0, -1):
            m = j * (3 * j - 1) / 2
            if eul.pentagonal(n - m) and eul.pentagonal(n + m):
                return int(n-m)


def eul45():
    """Find the next triangle number that is also pentagonal and hexagonal."""
    i = 143
    while i:
        i += 1
        hexagonal = i * (2 * i - 1)
        if eul.pentagonal(hexagonal):
            return hexagonal


def eul46():
    """What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?"""
    primes = eul.sieve(10000)
    squares = [x**2 for x in range(1, int(math.sqrt(10000/2)))]

    for i in range(25, 10000, 2):
        if i not in primes:
            possibles = [p for p in primes if p < i]
            works = False
            for p in possibles:
                test = i
                test -= p
                if test/2 == int(test/2) and test/2 in squares:
                    works = True
                    break
            if not works:
                return i


def eul47():
    """Find the first four consecutive integers to have four distinct prime factors.
    What is the first of these numbers?"""
    curr_n = 0
    primes = eul.sieve(200000)
    for n in range(20000, 200000):
        if eul.num_prime_factors(primes, n) != 4:
            curr_n = 0
        elif not curr_n:
            curr_n = n
        elif n - curr_n == 3:
            return curr_n


def eul48():
    """Find the last ten digits of the series, 1 + 2 + 3 + ... + n = 1000."""
    return sum([(i**i) % (10**10) for i in range(1, 1001)]) % (10**10)


def eul49():
    """What 12-digit number do you form by concatenating the three n=4-digit terms in this sequence where
     (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another?"""
    primes = eul.sieve(10000)
    for prime in primes:
        if prime > 1000:
            perms = set([int(''.join(p)) for p in itertools.permutations(str(prime)) if int(''.join(p)) > 1000])
            inter = sorted(list(perms.intersection(primes)))
            if len(inter) >= 3:
                for combo in itertools.combinations(inter, 3):
                    if combo[0] != 1487 and combo[2]-combo[1] == combo[1]-combo[0]:
                        return ''.join(sorted([str(p) for p in combo]))


def eul50():
    """Which prime, below n = one-million, can be written as the sum of the most consecutive primes?"""
    primes = eul.sieve(1000000)
    consecutive = 0
    maximum = 0

    for start in range(0, len(primes) - 2):
        r = 2 + consecutive
        for num in range(r, len(primes) - start):
            test = sum(primes[i] for i in range(start, start + num))
            if test > 1000000:
                break
            if test in primes and num > consecutive:
                consecutive = num
                maximum = test
    return maximum


def eul51():
    """Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits)
    with the same digit, is part of an eight prime value family."""

    primes = " ".join([str(i) for i in eul.sieve(1000000) if i > 100000])
    combos = itertools.product(range(2), repeat=6)

    for combo in combos:
        if len(set(combo)) == 1:
            continue
        possibilities = []
        for i in range(10):
            reg = r""
            for digit in range(6):
                if combo[digit] == 1:
                    reg += "["+str(i)+"]"
                else:
                    reg += "\d"
            p = re.compile(reg)
            possibilities.extend(p.findall(primes))

        for i in range(6):
            if combo[i] == 1:
                new_p = []
                for p in possibilities:
                    l = list(p)
                    l[i] = "*"
                    new_p.append("".join(l))
                possibilities = new_p
        c = collections.Counter(possibilities)
        if c.most_common(1)[0][1] == 8:
            num = c.most_common(1)[0][0]
            reg = r""
            f = True
            for i in num:
                if i == "*":
                    if f:
                        reg += r"(\d)"
                        f = False
                    else:
                        reg += r"\1"
                else:
                    reg += r"["+str(i)+r"]"
            p = re.compile(reg)
            return min([x.group(0) for x in p.finditer(primes)])


def eul52():
    """Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits."""
    i = 1
    while 1:
        n = eul.get_sorted_digits(2*i)
        if eul.get_sorted_digits(3*i)== n:
            if eul.get_sorted_digits(4*i) == n:
                if eul.get_sorted_digits(5*i) == n:
                    if eul.get_sorted_digits(6*i) == n:
                        break
        i += 1
    return i


def eul53():
    """How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?"""
    fac = math.factorial
    count = 0
    for n in range(23, 101):
        for r in range(n, 0, -1):
            val = fac(n)/(fac(r)*fac(n-r))
            if val > 1000000:
                count += 1
    return count


def eul67():
    """Find the maximum total from top to bottom of the triangle below (maximumPath2.txt):"""
    text_file = open("resources/maximumPath2.txt", "r")
    data = [[int(n) for n in line.split()] for line in text_file]
    text_file.close()

    for i in range(len(data) - 2, -1, -1):
        for j in range(len(data[i])):
            data[i][j] += max(data[i + 1][j], data[i + 1][j + 1])
    return data[0][0]


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
print("Euler solution 15:  ", eul15())
print("Euler solution 16:  ", eul16())
print("Euler solution 17:  ", eul17())
print("Euler solution 18:  ", eul18())
print("Euler solution 19:  ", eul19())
print("Euler solution 20:  ", eul20())
print("Euler solution 21:  ", eul21())
print("Euler solution 22:  ", eul22())
print("Euler solution 23:  ", eul23())
print("Euler solution 24:  ", eul24())
print("Euler solution 25:  ", eul25())
print("Euler solution 26:  ", eul26())
print("Euler solution 27:  ", eul27())
print("Euler solution 28:  ", eul28())
print("Euler solution 29:  ", eul29())
print("Euler solution 30:  ", eul30())
print("Euler solution 31:  ", eul31())
print("Euler solution 32:  ", eul32())
print("Euler solution 33:  ", eul33())
print("Euler solution 34:  ", eul34())
print("Euler solution 35:  ", eul35())
print("Euler solution 36:  ", eul36())
print("Euler solution 37:  ", eul37())
print("Euler solution 38:  ", eul38())
print("Euler solution 39:  ", eul39())
print("Euler solution 40:  ", eul40())
print("Euler solution 41:  ", eul41())
print("Euler solution 42:  ", eul42())
print("Euler solution 43:  ", eul43())
print("Euler solution 44:  ", eul44())
print("Euler solution 45:  ", eul45())
print("Euler solution 46:  ", eul46())
print("Euler solution 47:  ", eul47())
print("Euler solution 48:  ", eul48())
print("Euler solution 49:  ", eul49())
print("Euler solution 50:  ", eul50())
print("Euler solution 51:  ", eul51())
print("Euler solution 52:  ", eul52())
print("Euler solution 53:  ", eul53())
print("Euler solution 54:  ")
print("Euler solution 55:  ")
print("Euler solution 56:  ")
print("Euler solution 57:  ")
print("Euler solution 58:  ")
print("Euler solution 59:  ")
print("Euler solution 60:  ")
print("Euler solution 61:  ")
print("Euler solution 62:  ")
print("Euler solution 63:  ")
print("Euler solution 64:  ")
print("Euler solution 65:  ")
print("Euler solution 66:  ")
print("Euler solution 67:  ", eul67())
print("Euler solution 68:  ")
print("Euler solution 69:  ")
