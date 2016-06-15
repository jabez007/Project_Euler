#all about primes and finding them
import time
from itertools import permutations as perm
from itertools import combinations as combo

def Sieve(n): #finds all the primes up to the given number (Eratosthenes)
    start = time.time()
    numberList = ["", ""]+range(2, n+1)
    for i in range(4,n+1,2): #Take car of all the evens right from the start
        numberList[i]=""
    for i in range(1,int(n**.5)+1,2): #We can automatically skip the even indecies
        if numberList[i]:
            for j in range(i**2, int(n+1), i):
                numberList[j]=""
    end = time.time()
    #print end-start
    return numberList

def generator(n): #gives primes, one at a time
    start = time.time()
    numberList = ["", ""]+range(2, n+1)
    yield 2
    for i in range(4,n+1,2):
        numberList[i]=""
    for i in range(1,int(n**.5)+1,2):
        if numberList[i]:
            yield i
            for j in range(i**2, int(n+1), i):
                numberList[j]=""
    for i in range(int(n**.5)+1,n+1):
        if numberList[i]:
            yield i
    end = time.time()
    #print end-start

def factor(n, factors="", start=""): #finds all factors of given number
    if n<=0:
        return []
    else:
        if start=="":
            start=time.time()
        if factors=="":
            factors=[]
        for i in generator(n):
            if n%i==0:
                factors.append(i)
                return factor(n/i, factors, start)
        if len(factors)==1:
            #print time.time()-start
            #print "prime"
            return factors
        else:
            #print time.time()-start
            return factors

def prod(n): #for divisors(n)
    p = 1
    for i in range(len(n)):
        p*=n[i]
    return p

def divisors(n): #returns all proper divisors of n
    factors = factor(n)
    divisors = [1]
    for i in range(1,len(factors)):
        for d in combo(factors,i):
            divisor = prod(d)
            if divisors.count(divisor)==0:
                divisors = divisors+[divisor]
    return divisors

def divisibleTriangles(limit=500): #Project Euler, problem 12
    #What is the value of the first triangle number to have over five hundred divisors?
    n = 1 #move n up to make things faster
    T = (.5)*n*(n+1) #formula for triangle numbers
    divs = divisors(T)
    print n,T,divs
    while len(divs)<(limit+1):
        n+=1
        T = (.5)*n*(n+1)
        divs = divisors(T)
        print n,T,divs
    return n,T,divs

def amicableNumbers(n=10000): #Project Euler, problem 21
    #Evaluate the sum of all the amicable numbers under 10000.
    start = time.time()
    friends = []
    for i in range(2,n+1): #amicable numbers have to be even?
        if friends.count(i)==0:
            friend = sum(divisors(i))
            if i!=friend and sum(divisors(friend))==i:
                    print i,friend
                    friends = friends+[i,friend]
    print time.time()-start
    return sum(friends)

def nonAbundantSums(n=28123): #Project Euler, problem 23
    #Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
    start = time.time()
    numbers = range(n)
    abundant = []
    primes = Sieve(n)
    for i in range(2,n+1): #look at every number, skip 0 and 1
        if primes[i]:
            continue #primes only have one proper divisor
        else:
            divs = divisors(i)
            s = sum(divs)
            if s>i:
                abundant = abundant+[i] #find all abundant numbers
    for i in range(len(abundant)):
        for j in range(i, len(abundant)):
            s = abundant[i]+abundant[j]
            if s<n:
                numbers[s] = 0 #find all numbers that are the sum of two abundant numbers
            else:
                print s
                break
    print time.time()-start
    return sum(numbers)
            
def quadratic(n=1000): #Project Euler, problem 27
    #Finds the coefficients, |(a,b)|<n,
    #for the quadratic expression, m^2+am+b,
    #that produces the maximum number of primes for consecutive values of m
    start = time.time()
    maximum = 0
    ab = (0,0)
    for a in range(-n,n+1):
        for b in generator(n):
            m = 0
            factors = factor(m**2 + a*m + b)
            while len(factors)==1:
                m+=1
                factors = factor(m**2 + a*m + b)
            if m>maximum:
                maximum = m
                ab = (a,b)
                print ab
    print time.time()-start
    return ab, maximum

def circular(limit=1000000): #Project Euler, problem 35
    #How many circular primes are there below one million?
    start = time.time()
    count = 0
    primes = Sieve(limit)
    for i in generator(limit):
        if i>5 and (str(i).find('0')!=-1 or str(i).find('2')!=-1 or str(i).find('4')!=-1 or str(i).find('5')!=-1 or str(i).find('6')!=-1 or str(i).find('8')!=-1):
            continue
        n=0
        size=0
        for j in range(len(str(i))):
            size+=1
            index=str(i)[j:]+str(i)[:j]
            if primes[int(index)]:
                n+=1
            else:
                continue
        if n==size and n!=0:
            count+=1
            print i
    print time.time()-start
    return count

def pandigital(n=7654321): #Project Euler, problem 41.
    #What is the largest n-digit pandigital prime that exists?
    start = time.time()
    if n>7654321: #there can not be any pandigital primes greater
        n=7654321
    for p in generator(n):
        if len(str(p))==4 or len(str(p))==7: #pandigital numbers of any other length are divisible by 3
        #a number is divisible by 3 iff the digit sum of the number is divisible by 3
            count = 0
            for n in range(1,len(str(p))+1): #need to shift becasue of how range works
                if str(p).find(str(n))!=-1:
                    count+=1
            if count==len(str(p)):
                print p
        else:
            continue
    print time.time()-start
                    
'''def Problem49(): #From Project Euler, Needs to be cleaned up
    #1487, 4817, 8147
    #2969, 6299, 9629
    for i in range(1000,10000):
	if primes[i]:
		for j in perm(str(primes[i]),4):
			number=""
			for k in range(4):
				number = number+j[k]
			if int(number)>i and primes[int(number)]:
				difference = int(number)-i
				if (int(number)+difference)<10000:
					if primes[int(number)+difference]:
						permutation=0
						for l in range(4):
							if number.find(str(int(number)+difference)[l:l+1])!=-1:
								permutation = permutation+1
						if permutation==4:
							print i," ",number," ",int(number)+difference
'''

def Problem50(n=1000000): #Project Euler
    #Find the prime number that is the sum of the most consecuative primes
    start = time.time()
    primes = Sieve(n)
    prime = 0
    most = []
    for i in generator(n/10):
        s = 0
        terms = []
        for j in range(i,n):
            if primes[j]:
                s+=primes[j]
                #print "+",primes[j],s,
                if s>n:
                    break
                else:
                    terms = terms+[primes[j]]
                    #print "(",s,terms,")"
                    if len(terms)>len(most) and primes[s]:
                        prime = s
                        most = terms
                        print prime, most
    print time.time()-start
    return prime, most
                        
