"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

Answer:
        233168
Completed on Sun, 30 Mar 2014, 17:01
"""


def main(n=1000):
    integer_list = range(n)
    sum_all = 0
    for p in [3, 5]:
        i = 1
        while p * i < n:
            if p * i in integer_list:
                sum_all += p * i
                integer_list.remove(p * i)
            i += 1
    return sum_all

# # # #


if __name__ == '__main__':
    print main()
