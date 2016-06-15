"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

Answer:
    142913828922
Completed on Mon, 31 Mar 2014, 17:34
"""
from Problem3 import eratosthenes_sieve


def main(n=2e6):
    return sum(eratosthenes_sieve(int(n)))

# # # #


if __name__ == '__main__':
    print main()
