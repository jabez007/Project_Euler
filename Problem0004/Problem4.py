# -*- coding: utf-8 -*-
"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.

Answer:
    906609
Completed on Tue, 1 Apr 2014, 17:47
"""


def main():
    largest = 0
    numbers = (0, 0)
    
    three_digits = range(999, 99, -1)
    for p in three_digits:
        for q in three_digits:
            n = p * q

            if n < largest:
                '''
                since we are going through the 3-digit numbers from largest
                to smallest, as soon as we get any product smaller than the
                current largest palindrome we can break out of the nested loop
                '''
                break
            
            if is_palindrome(n):
                if n > largest:
                    largest = n
                    numbers = (p, q)
                else:
                    '''
                    again, since we are going through the 3-digit numbers in
                    reverse order, if we find a palindrome smaller than the current
                    largest palindrome we can break out of the nested loop
                    '''
                    break
                
    return largest, numbers


def is_palindrome(n):
    """

    :param n:
    :return:
    """
    return str(n) == str(n)[::-1]
        
# # # #


if __name__ == '__main__':
    print main()
