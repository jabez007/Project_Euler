"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

Answer:
    6857
Completed on Mon, 31 Mar 2014, 14:58
"""


def main(n=600851475143):
    return max(prime_factorization(n).keys())


def prime_factorization(n):
    """
    inefficient "trial and error" method to find factors
    :param n: <int> the number we want to factor
    :return: <dict> the prime factors of n with associated exponents. Keys == primes, Values == exponents
    """
    factors = {}

    if n <= 1:
        '''
        nice try
        '''
        return factors

    '''
    To save on memory, start with primes up to the square root of n
    REMINDER: The largest possible prime factor of n would be the prime 
    p such that p*2 = n
    '''
    primes = eratosthenes_sieve(int(n ** .5))

    while n not in primes:
        orig_n = n
        for p in primes:
            if n % p == 0:
                add_to_factors(factors, p)
                n = n / p
                break
        '''
        if we make it through all the primes but couldn't divide n break
        out of the while loop
        '''
        if n == orig_n:
            break

    '''
    if we haven't found any factors after going through all the primes 
    up to the square root of n, n is probably prime itself
    '''
    if not factors:
        return {n: 1}

    '''
    rebuild the primes now that we've shrunk n down to something we 
    should be able to fit into memory
    '''
    primes = eratosthenes_sieve(n)

    if n in primes:
        '''
        grab the last prime factor
        '''
        add_to_factors(factors, n)

    return factors


def add_to_factors(factors, factor):
    """
    used to keep track of prime factors and associated exponents
    :param factors: <dict> currently known primes and exponents
    :param factor: <int> factor to incorporate into factors either by adding a new value or incrementing an exponent
    :return: <dict> directly modifies passed in factors
    """
    '''
    Python passes parameters by object reference,
    so I can append to factors as long as I don't reassign
    the passed in variable
    '''
    if factor in factors:
        factors[factor] += 1
    else:
        factors[factor] = 1


def eratosthenes_sieve(n=100):
    """
    finds all of the prime numbers up to n using the Sieve of Eratosthenes
    :param n: <int> the upper limit of the prime numbers to find. Default is 100
    :return: <list> the primes up to n
    """
    sieve = [None, None, 2] + [switch(integer) for integer in integer_generator(n)]

    for i in integer_generator(n):
        m = i  # start at i**2
        while i * m <= n:
            '''
            remove all the multiples of i from the list of integers
            '''
            sieve[i * m] = None
            '''
            Using the index to set non-prime elements to None is faster 
            for large n than using list.remove()
            list.remove() searches through the list every time in order 
            to remove the first instance it finds
            '''
            m += 1

    return [p for p in sieve if p]  # now a list of all the primes less than n


def integer_generator(n):
    """
    Creating a generator instead of using range so we're not taking up 
    memory with an extra list
    :param n: <int> the largest integer you want
    :return: <generator> the integers 3 to n, including n
    """
    i = 3
    while i <= n:
        yield i
        i += 1


def switch(case):
    """
    Primes (pun intended) the "sieve" for Eratosthenes by pre-excluding 
    evens greater than 2
    :param case: <int>
    :return: <int/None>
    """
    if case % 2 == 0:
        return None
    else:
        return case

# # # #


if __name__ == '__main__':
    print main()
