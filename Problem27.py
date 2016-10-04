# -*- coding: utf-8 -*-
"""
Euler discovered the remarkable quadratic formula:

	n**2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive
integer values 0≤n≤39. However, when n=40,40**2+40+41=40(40+1)+41 is 
divisible by 41, and certainly when n=41,41**2+41+41 is clearly 
divisible by 41.

The incredible formula n**2 − 79n + 1601 was discovered, which produces 
80 primes for the consecutive values 0≤n≤79. The product of the 
coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n**2 + an + b, where |a|<1000 and |b|≤1000

	where |n| is the modulus/absolute value of n
	e.g. |11|=11 and |−4|=4

Find the product of the coefficients, a and b, for the quadratic 
expression that produces the maximum number of primes for consecutive 
values of n, starting with n=0.

Answer:
	-59231
Completed on Thu, 3 Apr 2014, 17:46
"""
from Problem3 import eratosthenes_sieve
from Problem7 import is_prime


def main():
	prime_list = eratosthenes_sieve(1000)
	b_list = [-1*p for p in prime_list] + prime_list
	
	max_primes = 0
	coefficents = (0, 0)
	# a has to be odd for n = 1
	for a in range(-999, 1000, 2):
		# b has to be prime for n = 0
		for b in b_list:
			n = number_of_primes(a, b, prime_list)
			if n > max_primes:
				print a, b, n
				max_primes = n
				coefficents = (a, b)
	
	return coefficents, max_primes


def number_of_primes(a, b, prime_list=[]):
	if not prime_list:
		prime_list = eratosthenes_sieve(b)
		
	n = 0
	y = quadratic_function(n, a, b)
	while is_prime(y, prime_list):
		n += 1
		y = quadratic_function(n, a, b)
		
	return n
	

def quadratic_function(n, a=0, b=0):
	return n**2 + a*n + b
	
# # # #


if __name__ == "__main__":
	coefficents, primes = main()
	print coefficents, primes, coefficents[0]*coefficents[1]
