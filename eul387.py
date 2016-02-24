import re
import math
import random
import sys
import time

def miller_rabin_pass(a, s, d, n):
    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    for i in range(s-1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1


def miller_rabin(n):
    if n < 2: return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
	
    for repeat in range(20):
        a = 0
        while a == 0:
            a = random.randrange(n)
        if not miller_rabin_pass(a, s, d, n):
            return False
    return True


# This function will read in a file that's seperated by none A-Za-z0-9
def parseUnicodeSepFile(filePath, isInt):
  readFile = open(filePath,'r')
  results = []
  for line in readFile:
    list = []
    input = re.findall(r'\w+', line)
    for node in input:
      if isInt:
        list.append(int(node))
      else:
        list.append(node)
    results.append(list)
  return results

  
#First calculates a smaller fib number and then using doubling to get a larger fib number.
#The index is the location of the fib number you are searching for this is used to grow as
#Quickly as possible
def fibonacciFastGrow(index):
  a, b = 0, 1
  n = 1
  #Need a better way to coming to this number
  num = index
  while num > 250:
    num = num / 2
  whenStart = math.floor(num)
  while n < whenStart:
    yield (a,b,n)
    a,b = b, a+b
    n += 1
  
  while 2*n < index:
    yield (a,b,n)
    aN = a*a + b*b
    bN = b*(2*a+b)
    a = aN
    b = bN
    n = 2*n
  
  while True:
    yield (a,b,n)
    a,b = b, a+b
    n+=1
  
#Returns a list of all primes up to n
def getPrimes(n):
  list = [2]
  for x in range(3,n+1,2):
    isPrime = True
    for prime in list:
      if prime < (x ** .5)+1:
        if x % prime == 0:
          isPrime = False
      else:
        break
    if isPrime:
      list.append(x)
  return list

def getPrimeGen(n):
  yield 2
  list = [2]
  for x in range(3,n+1,2):
    if (miller_rabin(x)):
      list.append(x)
      yield x
  yield None

#Instead of getting all the primes in advance I should build this as a generating functions
def isPrime(num):
  return miller_rabin(num)


def printTiming(func):
    def wrapper(*arg):
        t1 = time.time()
        res = func(*arg)
        t2 = time.time()
        print ('%s took %0.3f ms' % (func.__name__, (t2-t1)*1000.0))
        return res
    return wrapper
  
def listPrimeComponents(num):
  if isPrime(num):
    return [num]
  p_list = []
  #Do this so I can easily start at 3
  if (num % 2 == 0):
    p_list = [2]
  while (num % 2 == 0):
    num = int(num / 2)
  for n in range(3,num+1,2):
    #Is our new number prime?  Then no more divisors and leave
    #The location of this seems wrong but if I put it in the isPart condition I go 3x slower
    if isPrime(num):
      p_list.append(num)
      return p_list
    if isPrime(n):
      isPart = False
      while (num % n == 0):
        isPart = True
        num = int(num / n)
      if isPart:
        p_list.append(n)
        
        
  #print (p_list)
  return p_list

  #Returns a list of primes and their counts
#So ((prime1,count1) (prime2, count2))
def countPrimeComponents(num):
  p_list = listPrimeComponents(num)
  components = []
  for prime in p_list:
    count = 0
    while num % prime == 0:
      count +=1
      num = int(num / prime)
    components.append((prime,count))
  return components

# Returns a list of numbers that would divide n for example n = 28: [1, 2, 4, 7, 14, 28]
def FindDivisors(n):
   if n < 1:
      print ("ERROR: n must be greater than 0")
      return []
   result = FindProperDivisors(n)
   result.append(n);
   return result

# Returns a list of numbers that would divide n not including n for example n = 28: [1, 2, 4, 7, 14]
def FindProperDivisors(n):
   result = []
   result.append(1)
   for i in range(2,int(n**0.5)+1):
      if n%i==0:
         # if I is sqrt of n only append I
         if n/i == i:
            result.append(i)
         else:
            result.append(i)
            result.append(int(n/i))
   return result

#Problem 387
#A Harshad or Niven number is a number that is divisible by the sum of its digits. 
#201 is a Harshad number because it is divisible by 3 (the sum of its digits.) 
#When we truncate the last digit from 201, we get 20, which is a Harshad number. 
#When we truncate the last digit from 20, we get 2, which is also a Harshad number. 
#Let's call a Harshad number that, while recursively truncating the last digit, always results in a Harshad number a right truncatable Harshad number.
#
#Also: 
#201/3=67 which is prime. 
#Let's call a Harshad number that, when divided by the sum of its digits, results in a prime a strong Harshad number.
#
#Now take the number 2011 which is prime. 
#When we truncate the last digit from it we get 201, a strong Harshad number that is also right truncatable. 
#Let's call such primes strong, right truncatable Harshad primes.
#
#You are given that the sum of the strong, right truncatable Harshad primes less than 10000 is 90619.
#
#Find the sum of the strong, right truncatable Harshad primes less than 1014.
#
import sys
import time

getNum = lambda nums: sum(digit * 10 ** (len(nums) - 1 - i) for i, digit in enumerate(nums))

#
#First Solution is on top, it was a bruteish force way of solving the problem when my fast
#Approach wasn't working.  I did the simpler way first so I could confirm its results against 
#The Fast way.


#Determine if the number is Harshard Prime and all prev number
def isPrimeHarshad(num):
    s_num = str(num)
    list_of_ints = [int(i) for i in s_num]
    total = sum(list_of_ints)
    if total == 0: return True
    if (num % total == 0):
        if miller_rabin(int(num / total)):
            #print("Test: " + str(num))
            return recursiveHarshad(list_of_ints[:-1])
    return False

#Determine if a number and all previous are Harshard
def recursiveHarshad(listInts):
    #print(listInts)
    if len(listInts) <= 1:
        return True
    val = getNum(listInts)
    total = sum(listInts)
    if val % total == 0:
        return recursiveHarshad(listInts[:-1])
    else:
        #print("reject: " + str(val) + " total: " + str(total))
        return False
  

#only works number n that our modulus 10
def BruteForceSum(n):
    if n % 10 != 0:
        print("Must end in a 0")
        return(0)
    n = int(n / 10)
    total = 0
    for x in range(1,n,1):
        if (isPrimeHarshad(x)):
            #print(x)
            for c in "1234567890":
                val = int(str(x)+c)
                if (miller_rabin(val)):
                    #if (True):
                    total+=val
                    #print(val)
    return total
  
#Return True if the number is a Harshard
def isHarshad(splitNum):
    total = sum(splitNum)
    if total == 0: return True
    num = getNum(splitNum)
    if (num % total != 0):
        return False
    return True

#Return True if the number is a Harshard Prime
def isHarshadPrevPrime(splitNum):
    total = sum(splitNum)
    if total == 0: return True
    num = getNum(splitNum)
    if (num % total == 0):
        if (miller_rabin(int(num / total))):
            return True
    return False
  
def findSumFast(n):
    total = 0
    num = [0]*20
    # We default to 100 because 0-99 are not valid answers
    num[-3] = 1
    #So we don't have to constantly compute length
    TOP = len(num)-1
    i = TOP - 2
    #while num[0] < 10:
    #Constantly Converting the Array to an int is a 100% time increase.
    #Could write code find the max array value and compares more constantly
    #Or if you use powers of 10 exclusively like below
    #while num[-15] < 10:
    while getNum(num) < n:
        #Clean Up step if we exceed the bounds of where we are set to 0 and go back up a spot
        if num[i] > 9:
            num[i] = 0
            i -=1
            num[i]+=1
        #If our 1-Right deliminated value a Harshad and  Reduces to a prime
        #Then go to the next highest value and check if prime
        #Else no good and increment
        elif i == TOP - 1:
            if isHarshadPrevPrime(num[:i+1]):
                i+=1
            else:
                num[i] += 1
        #If we are at the top check to see if our total number is a prime, else increment
        elif i == TOP:
            if (miller_rabin(getNum(num))):
                val = getNum(num)
                total += val
                num[TOP]+=1
            else:
                num[i]+=1
        #Every number preceding the TOP must be a Harshad, except 2nd to top thats Harshad Prime
        elif i < TOP - 1:
            if isHarshad(num[:i+1]):
                i += 1
            else:
                num[i]+=1
    return total  

  
print ("Problem 387")
total = BruteForceSum(1000000)
total = findSumFast(1000000)
total = BruteForceSum(10000000)
total = findSumFast(10000000)
#10**14 = 696067597313468
total = findSumFast(10**14)
total = findSumFast(10**12+12)
total = findSumFast(10**13+13)










import math 

def get_digit_sum(n):
    """Returns sum of digits by converting to string"""
    return sum(int(digit) for digit in str(n))

def prime(n):
    n = int(n)
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(math.sqrt(n))
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True
    
nums = []
hars = []
    
for i in range(1,10**6):
    n = i
    # prime(int(n/get_digit_sum(n))) and
    har =  n % get_digit_sum(n) == 0
    n = int(n/10)
    if not har or (n > 0 and n not in hars):
        continue    
    
    hars.append(i)
    
    # if prime(int(i/get_digit_sum(i))):
    #     test = i * 10
    #     if prime(test + 1):
    #         nums.append(test + 1)
    #     if prime(test + 3):
    #         nums.append(test + 3)
    #     if prime(test + 7):
    #         nums.append(test + 7)
    #     if prime(test + 9):
    #         nums.append(test + 9)
            
print(hars)
print(nums)
print(sum(nums))
