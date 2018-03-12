# -*- coding: utf-8 -*-
"""
Surprisingly there are only three numbers that can be written as the sum
of fourth powers of their digits:

    1634 = 1**4 + 6**4 + 3**4 + 4**4
    8208 = 8**4 + 2**4 + 0**4 + 8**4
    9474 = 9**4 + 4**4 + 7**4 + 4**4

As 1 = 1**4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth 
powers of their digits.

Answer:
	443839
Completed on Tue, 11 Oct 2016, 00:35
"""


def main(e=5):
    digit_power_sums = list()
    for n in range(10**3, 10**(e+1)):
        if sum(int(d)**e for d in str(n)) == n:
            digit_power_sums.append(n) 
    return sum(digit_power_sums), digit_power_sums
    
# # # #


if __name__ == "__main__":
    print main()
