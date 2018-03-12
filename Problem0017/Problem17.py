"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one
hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

Answer:
    21124
Completed on Mon, 20 Jun 2016, 01:54
"""


def main(n=1000):
    letters = 0
    for number in range(1, n+1):
        letters += len(int_to_str(number))
    return letters


def int_to_str(number):
    """
    takes an integer and converts into it's English word form
    :param number: <int>
    :return: <str> The number spelled out
    """
    number = str(number)

    numbers_to_words = {'1': 'one',
                        '2': 'two',
                        '3': 'three',
                        '4': 'four',
                        '5': 'five',
                        '6': 'six',
                        '7': 'seven',
                        '8': 'eight',
                        '9': 'nine',
                        '10': 'ten',
                        '11': 'eleven',
                        '12': 'twelve',
                        '13': 'thirteen',
                        '14': 'fourteen',
                        '15': 'fifteen',
                        '16': 'sixteen',
                        '17': 'seventeen',
                        '18': 'eighteen',
                        '19': 'nineteen',
                        '20': 'twenty',
                        '30': 'thirty',
                        '40': 'forty',
                        '50': 'fifty',
                        '60': 'sixty',
                        '70': 'seventy',
                        '80': 'eighty',
                        '90': 'ninety'}

    words = ""

    digits = len(number)
    while digits > 0:

        if digits == 1:
            if number in numbers_to_words:
                words += numbers_to_words[number]

        elif digits == 2:
            if number in numbers_to_words:
                words += numbers_to_words[number]
                number = number[2:]
                digits = len(number)
                continue
            else:
                tens = number[0] + '0'
                if tens in numbers_to_words:
                    words += numbers_to_words[tens]

        elif digits == 3:
            if number[0] in numbers_to_words:
                words += numbers_to_words[number[0]] + 'hundred'
                if '00' in number[1:]:
                    number = number[3:]
                    digits = len(number)
                    continue
                else:
                    words += 'and'

        elif digits == 4:
            words += numbers_to_words[number[0]] + 'thousand'

        number = number[1:]
        digits = len(number)

    return words

# # # #


if __name__ == '__main__':
    print main()

