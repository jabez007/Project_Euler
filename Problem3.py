"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

Answer:
    6857
Completed on Mon, 31 Mar 2014, 14:58
"""


def main(n=600851475143):
    return prime_factorization(n)[-1]


def prime_factorization(n, factors=[], primes=[]):
    """
    inefficient "trial and error" method to find factors
    :param n: <int> the number we want to factor
    :param factors: <list> the prime factors of the number
    :param primes: <list> the primes we want to test as factors
    :return: <list> the prime factors of n
    """
    if not primes:
        '''
        we can start with only checking the primes up to
        the square root of n to conserve memory resources
        Though the largest possible prime factor of n would
        be the prime p such that p*2 = n
        '''
        primes = eratosthenes_sieve(int(n ** .5))

    if n in primes:
        factors.append(n)
    else:
        for p in primes:
            if n % p == 0:
                factors.append(p)
                '''
                Python passes parameters by object reference,
                so I can append to factors as long as I don't reassign
                the passed in variable
                '''
                return prime_factorization(n/p, factors, primes)
        '''
        if we make it out of the for loop,
        then we didn't find a prime factor in this
        last pass which would be odd if this
        is a composite number.
        So, reset the primes to be all primes up to the
        current n and check again
        '''
        primes = eratosthenes_sieve(n)
        return prime_factorization(n, factors, primes)

    return factors


def eratosthenes_sieve(n=100):
    """
    finds all of the prime numbers up to n using the Sieve of Eratosthenes
    :param n: <int>
    :return: <list> the primes up to n
    """
    integer_list = range(3, n + 1)  # MemoryError - only pick of the odds, as the evens are obviously not prime
    sieve = [None, None, 2] + [switch(integer) for integer in integer_list]

    for i in integer_list:
        m = i  # start at i**2
        while i * m <= n:
            '''
            remove all the multiples of i from the list of integers
            '''
            sieve[i * m] = None
            '''
            Using the index to set non-prime elements to None is faster for large n than using list.remove()
            list.remove() searches through the list every time in order to remove the first instance it finds
            '''
            m += 1

    return [p for p in sieve if p]  # now a list of all the primes less than n


def switch(case):
    """
    Primes (pun intended) the "sieve" for Eratosthenes by pre-excluding evens greater than 2
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
