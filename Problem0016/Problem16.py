"""
2 ** 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2 ** 1000?

Answer:
    1366
Completed on Wed, 2 Apr 2014, 02:20
"""


def main(n=1000):
    """
    Python handles large numbers fairly well, so we just go right for the obvious solution here
    :param n: <int>
    :return: answer
    """
    return sum([int(digit) for digit in str(2**n)])

# # # #


if __name__ == '__main__':
    print main()
