"""
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?

Answer:
    232792560
Completed on Mon, 31 Mar 2014, 03:59
"""
from Problem3 import eratosthenes_sieve


def main(n=20):
    """
    we can start with product of all the primes less than n.
    That will not only take care of all the primes, but also all
    the composite numbers that products of unique primes. These
    are numbers such as 6 (2 * 3) and 15 (3 * 5).
    Then to take care of composite numbers that are not the product
    unique primes (4, 8, 9, 12, ...) we have to look at exponents
    until the exponent puts us over n.
    :param n:
    :return:
    """
    product = 1
    primes = eratosthenes_sieve(n)
    for p in primes:
        product *= p
        e = 2
        while p**e <= n:
            product *= p
            e += 1
    return product

# # # #

if __name__ == '__main__':
    print main()
