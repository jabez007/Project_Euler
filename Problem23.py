"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the
sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum
exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two
abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as
the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is
known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

Answer:
    4179871
Completed on Fri, 11 Apr 2014, 16:18
"""
from Problem21 import get_proper_divisors


def main(n=28123):
    abundant_numbers = get_abundant_numbers(n)  # find all the abundant numbers up to n

    integers = range(n+1)
    '''
    then find all the sums that could be made from those abundant numbers, and remove those from the list of integers
    '''
    for i, a in enumerate(abundant_numbers):
        for b in abundant_numbers[i:]:  # we only need to start at the same element that the outer loop is on
            abundant_sum = a + b

            if abundant_sum > n:
                break  # break out of the inner for loop once we go over n

            integers[abundant_sum] = 0

    return sum(integers)


def get_abundant_numbers(n):
    """
    finds all abundant numbers (sum of proper divisors greater than number) less than or equal to n
    :param n: <int> the upper limit of abundant numbers to find
    :return: <list> of abundant numbers
    """
    abundant_numbers = list()
    for i in range(12, n+1):  # 12 if the smallest abundant number, so start there
        if is_abundant_number(i):
            abundant_numbers.append(i)
    return abundant_numbers


def is_abundant_number(n):
    """
    determines if n is abundant (sum of proper divisors of n is greater than n)
    :param n: <int> number to test the abundance of
    :return: <boolean> True if n is abundant
    """
    return sum(get_proper_divisors(n)) > n

# # # #


if __name__ == '__main__':
    print main()
