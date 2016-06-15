"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.
What is the 10,001st prime number?

Answer:
    104743
Completed on Mon, 31 Mar 2014, 16:56
"""
from math import log
from Problem3 import eratosthenes_sieve


def main(n=10001):
    return n_primes(n)[n-1]


def n_primes(n, primes=[]):
    """
    using the Prime number theorem, we know the nth prime number can be
    approximated by n*ln(n)
    :param n: <int> the number of primes you want to find
    :param primes: <list> the primes you might have already found
    :return: <list> the first n primes
    """
    if not primes:
        nth_prime = int(n * log(n))
        primes.extend(eratosthenes_sieve(nth_prime))

    increment = 1
    while len(primes) < n:
        '''
        while we don't have n primes, go from the largest prime we do have and
        look for the next one
        '''
        if is_prime(primes[-1]+increment, primes[:len(primes)/2]):
            # realistically, we should only need to check divisibility with the first half of the primes we have
            '''
            We found another prime! Add that to the ones we already have, then
            use this new prime to find the next one.
            '''
            primes.append(primes[-1]+increment)
            increment = 1
        else:
            increment += 1

    return primes


def is_prime(n, primes=[]):
    """
    (very inefficient)
    determine if a given number is prime by attempting to divide it by each of the primes
    up to the square root of the number. If we haven't found a factor by then, we won't.
    :param n: <int> number you want to determine whether or not it is prime
    :param primes: <list> primes you want to use to in testing n
    :return: <boolean> True if we are not able to divide n by any of the given primes
    """
    if not primes:
        primes.extend(eratosthenes_sieve(int(n ** .5)))

    for p in primes:
        if n % p == 0:
            return False

    return True

# # # #


if __name__ == '__main__':
    print main()
