"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a**2 + b**2 = c**2
    For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Answer:
    31875000
Completed on Tue, 1 Apr 2014, 18:16
"""
from Problem8 import product


def main(perimeter=1000):
    odds = range(1, perimeter, 2)  # get all the odd numbers up to the perimeter we are looking for
    for n in range(1, perimeter):
        for o in odds:
            m = n + o  # makes sure the difference between m and n is odd and that m > n
            if is_coprime(m, n):  # combined with the odd difference, make sure we get a primitive triple
                triplet = euclids_formula(m, n)
                if sum(triplet) == perimeter:
                    return triplet, 1, product(triplet)
                elif perimeter % sum(triplet) == 0:  # it might be a non-primitive triple that gives us our perimeter
                    return triplet, perimeter/sum(triplet), product(triplet)*((perimeter/sum(triplet))**3)
                elif sum(triplet) > perimeter:
                    break  # move on the the next n as soon as we overshoot our perimeter


def euclids_formula(m, n):
    """
    a fundamental formula for generating Pythagorean triples given an arbitrary
    pair of positive integers m and n with m > n
    m and n have to be coprime with m - n being odd in order to find a primitive
    triple (a triple that is not just a multiple of another)
    :param m:
    :param n:
    :return: <tuple> a, b, c such that a**2 + b**2 = c**2
    """
    a = m**2 - n**2
    b = 2*m*n
    c = m**2 + n**2
    '''
    this works because
    a**2 + b**2 = c**2
    (m**2 - n**2)**2 + (2*m*n)**2 = (m**2 + n**2)**2
    '''
    return a, b, c


def is_coprime(p, q):
    """
    uses the Euclidean Algorithm (gcd) to determine if two numbers are coprime (gcd == 1)
    :param p: <int>
    :param q: <int>
    :return: <boolean> True if p and q are coprime
    """
    return euclidean_algorithm(max(p, q), min(p, q)) == 1


def euclidean_algorithm(x=1071, y=462):
    """

    :param x:
    :param y:
    :return: <int> gcd(x, y). 1 if x and y are coprime, 0 for errors
    """
    if x < y:
        return 0
    '''
    x = y*q0 + r0
    y = r0*q1 + r1
    r0 = r1*q2 + r2
    ...
    r(n-2) = r(n-1)*qn + 0
    then gcd of x and y is r(n-1)
    '''
    if x % y == 0:
        return y
    else:
        return euclidean_algorithm(y, x % y)

# # # #


if __name__ == '__main__':
    print main()
