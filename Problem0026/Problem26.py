# -*- coding: utf-8 -*-
"""
A unit fraction contains 1 in the numerator. The decimal representation 
of the unit fractions with denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1 

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. 
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring 
cycle in its decimal fraction part.

Answer:
	983
Completed on Thu, 3 Apr 2014, 16:56
"""
from Problem3 import eratosthenes_sieve


def main(n=1000):
	'''
	https://en.wikipedia.org/wiki/Repeating_decimal#Fractions_with_prime_denominators
	
	A fraction in lowest terms with a prime denominator other than 2 or 
	5 (i.e. coprime to 10) always produces a repeating decimal. The 
	length of the repetend (period of the repeating decimal) of 1/p is 
	equal to the order of 10 modulo p. If 10 is a primitive root modulo 
	p, the repetend length is equal to p − 1; if not, the repetend 
	length is a factor of p − 1. This result can be deduced from 
	Fermat's little theorem, which states that 10**(p−1) ≡ 1 (mod p).
	
	So we can focus on just prime denominators, work our way down 
	from 100 to find the first prime that meets the above conditions, 
	then the length of the cycle will be p-1 and we know that will be 
	the larget possible cycle under 1000
	'''
	primes = eratosthenes_sieve(n)
	# find the largest prime with 10 as a primative root
	for p in reversed(primes):
		if multiplicative_order(10, p) == p-1:
			divisor = p
			break
			
	# <Extra Credit> find the cycle for this divisor
	
	return divisor, reciprocal_cycle(divisor)
	
	
def multiplicative_order(a, n):
	"""
	In number theory, given an integer a and a positive integer n with 
	gcd(a,n) = 1, the multiplicative order of a modulo n is the smallest
	positive integer k with a**k ≡ 1 (mod n)
	"""
	for k in range(1, n):
		if (a**k)%n == 1:
			return k
			

def is_primative_root(m, n):
	"""
	 If the multiplicative order of a number m modulo n is equal to φ(n)
	 (the order of Z[n*×]), then it is a primitive root.
	"""
	return
			
			
def reciprocal_cycle(d):
	"""
	finds all the long division remainders until they start to repeat
	"""
	d = int(d)  # make sure we dont get weird decimals in the return
	quotient = [1/d]
	remainders = [1%d]
	
	while len(quotient) < d:  # the length of the cycle cannot be greater then the divisor
		q = (remainders[-1]*10) / d  # multiply by 10 to bring the zero down in long division
		r = (remainders[-1]*10) % d  
		
		quotient.append(q)
		if r in remainders:
			break	
		remainders.append(r)
		
	return "".join(str(q) for q in quotient[1:])  # skip the 0 that would be on the left side of the decimal

# # # #


if __name__ == "__main__":
	print main()
