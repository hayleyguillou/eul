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





#python3
def euler14():
    maxChain = 0
    maxNum = 0
    for i in range(1000000,1,-1):
        chain = 1
        num = i
        while i != 1:
            if i % 2 != 0:
                i = 3*i + 1
            else:
                i = i / 2
            chain = chain + 1
        if chain > maxChain:
            maxChain = chain
            maxNum = num
            print ("Max: ", maxChain, maxNum)
    print (maxChain, maxNum)
    

def euler16():
    num = 1
    digits = list()

    for i in range (1,1001):
        num = num *2
        if i == 1000:
            while num > 0:
                digits.append(num%10)
                num = int(num / 10)

    print(sum(digits))


def euler17():
    def getDigits(n):
        three = {1,2,6,10}
        four = {4,5,9}
        five = {3,7,8,40,50,60}
        six = {11,12,20,30,80,90}
        seven = {15,16,70}
        eight = {13,14,18,19}
        nine = {17}

        if n in three:
            return 3
        elif n in four:
            return 4
        elif n in five:
            return 5
        elif n in six:
            return 6
        elif n in seven:
            return 7
        elif n in eight:
            return 8
        elif n in nine:
            return 9

        else :
            return 0


    def inspectNum(n):
        digits = getDigits(n)

        if n == 1000:
            return 11
        elif n == 0:
            return 0
        elif digits != 0:
            return digits

        else :
            if n > 99:
                if n%100 == 0:
                    return getDigits(int(n/100)) + 7 
                else:
                    return getDigits(int(n/100)) + 10 + inspectNum(n%100)
            else:
                return getDigits(n - (n%10)) + inspectNum(n%10)

    num = 0
    for i in xrange(1, 1000 + 1):
        num = num + inspectNum(i)

    print num
   

    
def euler23():
    def factors(n):
	   return {x for x in range(1, (n + 1) // 2 + 1) if n % x == 0 and n != x}

    upper = 28123

    abundants = set()
    for i in range(12, upper):
        if sum(factors(i)) > i:
            abundants.add(i)

    abunSums = set()
    for i in abundants:
        for j in abundants:
            if i+j > upper:
                break
            abunSums.add(i+j)

    allNums = set()
    for i in range(1, upper):
        allNums.add(i)

    print (sum(list(allNums - abunSums)))

    
def euler24():
    max = 10

    checker = [False]*max
    num = 1
    for a in range(0,max):
        checker[a] = True
        for b in range(0,max):
            if not checker[b]:
                checker[b] = True
                for c in range(0,max):
                    if not checker[c]:
                        checker[c] = True
                        for d in range(0,max):
                            if not checker[d]:
                                checker[d] = True
                                for e in range(0,max):
                                    if not checker[e]:
                                        checker[e] = True
                                        for f in range(0,max):
                                            if not checker[f]:
                                                checker[f] = True
                                                for g in range(0,max):
                                                    if not checker[g]:
                                                        checker[g] = True
                                                        for h in range(0,max):
                                                            if not checker[h]:
                                                                checker[h] = True
                                                                for i in range(0,max):
                                                                    if not checker[i]:
                                                                        checker[i] = True
                                                                        for j in range(0,max):
                                                                            if not checker[j]:
                                                                                checker[j] = True
                                                                                if num %1000000 == 0:
                                                                                    print (a,b,c,d,e,f,g,h,i,j)
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

        
def euler25():
    index = 1
    a, b = 0, 1
    while len(str(b)) < 1000:
        a, b = b, a + b
        index += 1    
    print (index)


def euler29():
    return (len(set([(a**b) for a in range(2,101) for b in range(2,101)])))

def euler30():
    print (sum([x for x in range(2,1000000) if sum([y**5 for y in getDigits(x)]) == x]))

#
def euler34():
    import math

    specials = []
    for i in range(3,100000):
        digits = []
        temp = i
        while temp > 0:
            digits.append(temp % 10)
            temp = int(temp/10)

        factorialSum = sum([ math.factorial(x) for x in digits ])

        if factorialSum == i:
            specials.append(i)
            print (specials)


def euler35():
	import math
	from itertools import permutations
	
	def check_digits(n):
	    while n > 0:
	        digit = n % 10
	        if digit==5 or digit%2==0:
	            return False
	        n = int(n/10)
	    return True
	
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
	
	def eul35(n):
	    """How many circular primes are there below n = one million?"""
	    primes = [p for p in sieve(n) if check_digits(p)]
	
	    circs = {2,5}
	    for prime in primes:
	        if prime not in circs:
	
	            perms = {prime}
	            for i in range(0, len(str(prime))-1):
	                prime = int(str(prime)[1:]) * 10 + int(str(prime)[0])
	                perms.add(prime)
	
	            circ = True
	            for perm in perms:
	                if perm not in primes:
	                    circ = False
	                    break
	            if circ:
	                circs.update(perms)
	
	    return len(circs)
	
	print(eul35(1000000))
	
	#2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.


def euler36():
    return sum([ x  for x in range(1, 1000001) if isPalindrome(x) and isPalindrome(str(bin(x))[2:]) ])

def euler38():
    max = 0
    check = set([1,2,3,4,5,6,7,8,9])
    for i in range(1,100000):
        concat, iter = "", 1
        while len(concat) < 10:
            concat = concat + str(i * iter)
            if len(concat) == 9:
                if set([int(x) for x in concat]) == check:
                    if int(concat) > max: 
                        max = int(concat)
            iter += 1
    print(max)
    
    
def euler40():
    num = ''.join([str(x) for x in range(0,1000000)])
    print(int(num[1]) * int(num[10]) * int(num[100]) * int(num[1000]) * int(num[10000]) * int(num[100000]) * int(num[1000000]))
    
    
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
    
    
def euler48():
    print (sum([ (i**i)%(10**10) for i in range(1, 1001) ])%(10**10))


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
