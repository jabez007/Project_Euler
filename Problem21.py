# -*- coding: utf-8 -*-
"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called
amicable numbers.
For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The
proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.

Answer:
    31626
Completed on Fri, 4 Apr 2014, 18:03
"""


def main(n=10000):
    return sum(amicable_numbers(n).keys())


def get_proper_divisors(n):
    """
    Finds all of the proper divisors of n
    :param n: <int> the number you want to find the proper divisors of
    :return: <list> the proper divisors of n
    """
    divisors = [1]  # starting out, every number has 1 as proper divisor

    for d in range(2, int(n**.5)+1):  # start at 2 and go up through the square root on n
        if n % d == 0:  # if this number evenly divides n
            if d not in divisors:
                divisors.append(d)  # add this divisor to the list of proper divisors
            if n / d not in divisors:
                divisors.append(n/d)  # also add the resulting quotient to the list of proper divisors

    return sorted(divisors)


def amicable_numbers(n):
    """
    finds all the amicable numbers up to n
    :param n: <int> the upper limit of the amicable numbers to find
    :return: <dict> the key-value pairs of which represent amicable pairs
    """
    amicable = dict()

    for i in range(220, n+1):  # start at the smallest possible amicable number
        if i not in amicable:
            i_divisors = get_proper_divisors(i)
            possible_friend = sum(i_divisors)

            if possible_friend == i:  # perfect numbers are not amicable to themselves
                continue

            if sum(get_proper_divisors(possible_friend)) == i:
                amicable[i] = possible_friend
                amicable[possible_friend] = i

    return amicable

# # # #


if __name__ == '__main__':
    print main()
