"""
You are given the following information, but you may prefer to do some research for yourself.
    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

Answer:
    171
Completed on Fri, 4 Apr 2014, 14:27
"""


def main():
    """
    Counts the number of months that start on a Sunday between 1/1/1901 and 1/1/2001
    :return: <int>
    """
    first_sundays = 0

    months = {1: 31,
              2: 28,
              3: 31,
              4: 30,
              5: 31,
              6: 30,
              7: 31,
              8: 31,
              9: 30,
              10: 31,
              11: 30,
              12: 31}

    '''
    If the number of days since 1/1/1900 divided by 7 is congruent to 6 mod 7, then that day is a sunday
    '''
    start_days = 365
    if start_days % 7 == 6:  # is 1/1/1901 a monday?
        first_sundays += 1

    for y in range(1901, 2001):
        for m, d in months.iteritems():
            if m == 2:  # February might have 29 days instead of 28
                if y % 100 == 0 and y % 400 == 0:  # if the year is on the century and that year is divisible by 400
                    d += 1
                elif y % 4 == 0:  # of if the year is divisible by 4
                    d += 1

            start_days += d
            if start_days % 7 == 6:
                first_sundays += 1

    return first_sundays

# # # #


if __name__ == '__main__':
    print main()
