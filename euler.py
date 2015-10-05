#Recovery Key: 591851-6fi6YZtYSdSusoklQGP9MW5UplAqgk0ceKKWQ9op
#Generated: Tue, 15 Sep 2015, 09:47.51

#common defs
import math
from functools import reduce

def getDigitSum(n):
    return sum(int(digit) for digit in str(n))

def getProperDivisors(n):
    return {x for x in range(1, (n + 1) // 2 + 1) if n % x == 0 and n != x}
    
def getDigits(n):
    return [int(i) for i in str(n)]

def getFactors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def sieveIt(n):
    sieve = [True]*(n + 1)
    sieve[0],sieve[1] = False, False

    for i in range(2,int(math.sqrt(n))):
        curr = i + i
        while curr <= n:
            sieve[curr] = False
            curr += i
    return sieve

def isPalindrome(n):
    if (str(n))[::-1] == str(n):
        return True
    else:
        return False
    
    
#problem solutions


        
def euler25():
    index = 1
    a, b = 0, 1
    while len(str(b)) < 1000:
        a, b = b, a + b
        index += 1    
    print (index)




    
def euler39():
    maxlen = 0
    the_p = 0
    for p in range(3,1001):
        sols = set()
        for c in range(int(p/3)+ 1, p-1):
            for b in range(1, p-c-1):
                a = p - c - b
                if a**2 + b**2 == c**2:
                    sols.add(tuple(sorted([a,b,c])))
        if len(sols) > maxlen:
            maxlen = len(sols)
            the_p = p
        print(p, the_p, maxlen)
            
    print(p)
    
    
def euler40():
    num = ''.join([str(x) for x in range(0,1000000)])
    print(int(num[1]) * int(num[10]) * int(num[100]) * int(num[1000]) * int(num[10000]) * int(num[100000]) * int(num[1000000]))

def euler41():
    import math

    def is_pandigital(n, s=9): n=str(n); return len(n)==s and not '1234567890'[:s].strip(n)
    
    def is_prime(n):
        n = int(n)
        if n == 2 or n == 3: return True
        if n < 2 or n%2 == 0: return False
        if n < 9: return True
        if n%3 == 0: return False
        r = int(math.sqrt(n))
        f = 5
        while f <= r:
            if n%f == 0: return False
            if n%(f+2) == 0: return False
            f +=6
        return True
    
        
    
    for p in range(7654321,1,-2):
        if is_pandigital(p, 7) and is_prime(p):
            print(p)
            break
    
def euler43():
    from itertools import permutations
    
    def is_divisible(p):
    	divisors = [2,3,5,7,11,13,17]
    	for i in range(0, len(divisors)):
    		num = 100 * int(p[i+1]) + 10 * int(p[i+2]) + int(p[i+3])
    		if num % divisors[i] != 0:
    			return False
    	return True
    
    def eul43():
    	"""Find the sum of all 0 to 9 pandigital numbers with this property (See online)"""
    	init = [''.join(p) for p in permutations('0123456789') if p[0]!='0' and p[5]=='5' and int(p[3])%2==0]
    	return sum([int(p) for p in init if is_divisible(p)])
    
    print(eul43())
    # 16695334890
    
def euler44():
    P = [ ( ( p * (3 * p - 1 ) ) / 2 ) for p in range(1, 3000) ]

    for p in P:
        for q in P[P.index(p):]:
            if (p+q) in P and math.fabs(p-q) in P:
                print (math.fabs(p-q))
                
                
def euler45():
    T,H,P = set(), set(), set()
    for n in range(1,200000):
        t = n + 285
        p = n + 165
        h = n + 143
        T.add( ( t * (t+1) ) / 2 )
        P.add( ( p * (3 * p - 1 ) ) / 2 )
        H.add( h * (2 * h - 1 ) )
    print(T&H&P)
    
    
def euler46():
    import math
    def sieve(n):
        # returns all primes between 2 and n
        s = [True]*(n + 1)
        s[0], s[1] = False, False
    
        for i in range(2, int(math.sqrt(n))):
            curr = i + i
            while curr <= n:
                s[curr] = False
                curr += i
        return [i for i in range(len(s)) if s[i] is True]
        
    primes = sieve(10000)
    squares = [x**2 for x in range(1,int(math.sqrt(10000/2)))]
    print(squares)
    
    for i in range(25,10000,2):
        if i not in primes:
            possibles = [p for p in primes if p < i ]
            works = False
            for p in possibles:
                test = i
                test -= p
                if test/2 == int(test/2) and test/2 in squares:
                    works = True
                    #return i
                    #print(i,' = ',p,' + 2 * ',test/2)
                    break
            if not works:
                print('Sol:', i)
                break
    
def euler47():
    import math
    import itertools
    def sieve(n):
        # returns all primes between 2 and n
        s = [True]*(n + 1)
        s[0], s[1] = False, False
    
        for i in range(2, int(math.sqrt(n))):
            curr = i + i
            while curr <= n:
                s[curr] = False
                curr += i
        return [i for i in range(len(s)) if s[i] is True]
    
    def get_proper_divisors(n):
        return {x for x in range(1, (n + 1) // 2 + 1) if n % x == 0 and n != x}
        
    def eul47():
        curr_n = 0
        primes = sieve(1000000)
        for n in range(20000,2000000):
            if len(set(get_proper_divisors(n).intersection(primes))) != 4:
                curr_n = 0
            elif not curr_n:
                curr_n = n
            elif n - curr_n == 3:
                return curr_n
            if curr_n: print(n, n-curr_n)
    print(eul47())
    
    
def euler48():
    print (sum([ (i**i)%(10**10) for i in range(1, 1001) ])%(10**10))


def euler49():
	import math
    import itertools
    def sieve(n):
        # returns all primes between 2 and n
        s = [True]*(n + 1)
        s[0], s[1] = False, False
    
        for i in range(2, int(math.sqrt(n))):
            curr = i + i
            while curr <= n:
                s[curr] = False
                curr += i
        return [i for i in range(len(s)) if s[i] is True]
    
    def eul49():    
        primes = sieve(10000)
        for prime in primes:
            if prime > 1000:
                perms = set([int(''.join(p)) for p in itertools.permutations(str(prime)) if int(''.join(p)) > 1000])
                inter = sorted(list(perms.intersection(primes)))
                if len(inter) >= 3:
                    for combo in itertools.combinations(inter, 3):
                        if combo[0] != 1487 and combo[2]-combo[1] == combo[1]-combo[0]:
                            return ''.join(sorted([str(p) for p in combo]))
    print(eul49())

def euler50():
    #DOESN'T STOP????
	import math
    
    def sieve(n):
        # returns all primes between 2 and n
        s = [True]*(n + 1)
        s[0], s[1] = False, False
    
        for i in range(2, int(math.sqrt(n))):
            curr = i + i
            while curr <= n:
                s[curr] = False
                curr += i
        return [i for i in range(len(s)) if s[i] is True]
        
        
    primes = sieve(1000000)
    print(len(primes))
    
    conseq = 0
    maximum = 0
    
    for start in range(0, len(primes) - 2):
        for num in range(2, len(primes) - start):
            test = sum(primes[i] for i in range(start, start + num))
            if test > 1000000:
                break
            if test in primes and num > conseq:
                conseq = num
                maximum = test
                print(maximum)
                print(test,start, num)


def euler52():
    def getDigits(n):
        return sorted([int(i) for i in str(n)], key=int)

    found = False
    i = 1
    while not found:
        n = getDigits(2*i)
        if getDigits(3*i)== n:
            if getDigits(4*i) == n:
                if getDigits(5*i) == n:
                    if getDigits(6*i)== n:
                        print (i)
                        found = True
        i += 1

        
def euler53():
    fac = math.factorial
    count = 0
    for n in range(23,101):
        for r in range(n,0, -1):
            val = fac(n)/(fac(r)*fac(n-r))
            if val > 1000000:
                count += 1
    print (count)


def euler55():
    lycs = []

    for num in range(1, 10000):
        i = num
        found, iter = False, 0
        while not found and iter < 50:
            i += int((str(i))[::-1])
            if (str(i))[::-1] == str(i):
                found = True
            iter += 1
        if not found:
            lycs.append(num)

    print (len(lycs))
        
def euler56():
    def digits(n):
        d = []
        while n > 0:
            d.append(n % 10)
            n = int(n/10)
        return d

    import math

    maxDigitSum = 0

    for base in range(1, 100):
        for expo in range(1, 100):
            digitSum = sum(digits(math.pow(base, expo)))
            if digitSum > maxDigitSum:
                maxDigitSum = digitSum
            print (base, expo, digitSum, maxDigitSum)    

    print (maxDigitSum)
    
def euler63():
    p = set()
    for base in range(1,10):
        for expo in range(1,50):
            num = base**expo
            leng = len(str(num))
            if leng > expo:
                break
            elif leng == expo:
                p.add(num)
    print (len(p))
    
    
def euler71():
    #this is some bullshite
    from fractions import gcd
    from math import fabs
    
    propers = []
    for d in range(1,1000001):
        for n in range(int((d*3)/7), int((d*3)/7)+1):
            if gcd(n,d) == 1:
                if fabs(3/7 - n/d) < 0.0000005:
                    propers.append((n/d,n,d))
                    #print(n,d,len(propers))
    
    lst = sorted(propers, key=lambda x: x[0])
    print(lst)
    
def euler73():
    from fractions import gcd


    count = 0
    for d in range(1,12000 +1):
    	for n in range(int(d/3),int(d/2)+1):
    		if gcd(n,d) == 1:
    			if n/d > 1/3 and n/d < 1/2:
    				count += 1
    				if count % 1000000 == 0: print(count)
    
    print(count)
    
def euler74():
    count = 0
    for i in range (1,1000000):
        chain = set([i])
        next = sum([math.factorial(int(x)) for x in str(i)])
        while next not in chain:
            chain.add(next)
            next = sum([math.factorial(int(x)) for x in str(next)])

        if len(chain) == 60:
            count += 1
            print (i, len(chain), count)

    print(count)
    
#so bf its nuts
def euler92():
    loop = set([4,89])
    count = 0
    for x in range(1,10000000):
        s = x
        chain = set([x])
        while x != 1 and x not in loop:
            x = sum([int(n)**2 for n in str(x)])
            chain.add(x)
            #print ("chain: ",chain)
        if x in loop:

            count += 1
            if count%19084 == 0: print(s, count, len(loop))
    print("**",len(loop))
    print(count)     
    
    
def euler95():
    def get_proper_divisors(n):
        return {x for x in range(1, (n + 1) // 2 + 1) if n % x == 0 and n != x}
        
    maxlen = 0
    minel = 0
    
    
    for x in range(12496,1000000):
        chain = [x]
        next = sum(get_proper_divisors(x))
        while next not in chain and next != 1 and next < 1000000:
            chain.append(next)
            next = sum(get_proper_divisors(next))
        if x == next:
            if len(chain) > maxlen:
                maxlen = len(chain)
                minel = min(chain)
        print(x,maxlen,minel)
    
    
def euler112():
    prop, numBouncy, curr = 0,0,0
    while prop < 0.99:
        curr += 1


        n = curr
        increasing, decreasing = False, False
        a, b = n % 10, 0
        n = int(n/10)
        while n > 0:
            b = a
            a = n % 10
            n = int(n/10)

            if b < a: 
                increasing = True
            elif a < b: 
                decreasing = True



        if increasing and decreasing:
            numBouncy += 1
            #print(curr, numBouncy, prop)

        prop = numBouncy/curr

    print(curr, prop)


def euler125():
    import math
    
    def palindrome(n):
        return True if (str(n))[::-1] == str(n) else False
    
    def eul125(n):
        palins = set()
        for starting_num in range(1,int(math.sqrt(n))):
            conseq = 2
            s = 0
            while s < n:
                s = sum([(starting_num + x)**2 for x in range(0,conseq)])
                if s < n and palindrome(s) :
                    palins.add(s)
                    print(sum(palins))
                conseq += 1
                    
    eul125(100000000)
    
    
def euler179():
    n = [0]*10000001
    for i in range(2, int(10000000/2)):
        for j in range(i * 2, 10000001, i):
            n[j] += 1
            
    print(len([i for i in range(2,10000000) if n[i] == n[i+1]]))
    
    
def euler348():
    from itertools import count
    import math
    
    def getPalindrome():
        """
            Generator for palindromes.
            Generates palindromes, starting with 0.
            A palindrome is a number which reads the same in both directions.
        """
        yield 0
        for digits in count(1):
            first = 10 ** ((digits - 1) // 2)
            for s in map(str, range(first, 10 * first)):
                yield int(s + s[-(digits % 2)-1::-1])
    
    def allPalindromes(minP, maxP):
        """Get a sorted list of all palindromes in intervall [minP, maxP]."""
        palindromGenerator = getPalindrome()
        palindromeList = []
        for palindrome in palindromGenerator:
            if palindrome > maxP:
                break
            if palindrome < minP:
                continue
            palindromeList.append(palindrome)
        return palindromeList
        
    palindromes = allPalindromes(5229225, 10**10)
    min5 = set()
    for p in palindromes:
        cube_limit = int(math.pow(p, 1/3)) - 1
        count = 0
        for c in range(1,cube_limit):
            s = math.sqrt(p - c**3)
            if s == int(s):
                count += 1
        if count == 4:
            min5.add(p)
            if len(min5) == 5:
                break
            print(p)
    print(min5)
    print(sum(min5))



def euler491()
#NOT DONE
    from itertools import permutations

    all = set([int(''.join(x)) for x in permutations('001122334455') if x[0] != '0'])
    print(len(all))
    print(len([x for x in all if x%11==0]))
