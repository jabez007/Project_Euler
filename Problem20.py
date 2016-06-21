# -*- coding: utf-8 -*-
"""
n! means n * (n − 1) * ... * 3 * 2 * 1
For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in the number 100!

Answer:
    648
Completed on Wed, 2 Apr 2014, 02:46
"""


def main(n=100):
    return sum([int(digit) for digit in str(factorial(n))])


def factorial(n):
    """
    Calculates the factorial of n.
    ex: factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
    :param n: <int> the number you want the factorial of
    :return: <int> n!
    """
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

# # # #


if __name__ == '__main__':
    print main()
