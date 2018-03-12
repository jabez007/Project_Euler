# -*- coding: utf-8 -*-
"""
The sum of the squares of the first ten natural numbers is,
    1**2 + 2**2 + ... + 10**2 = 385
The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)**2 = 55**2 = 3025
Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.

Answer:
    25164150
Completed on Tue, 1 Apr 2014, 17:57
"""


def main(n=100):
    natural_numbers = range(1, n+1)
    square_sum = sum(natural_numbers) ** 2
    sum_squares = sum(n ** 2 for n in natural_numbers)
    return square_sum - sum_squares

# # # #


if __name__ == '__main__':
    print main()
