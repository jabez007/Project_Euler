# -*- coding: utf-8 -*-
"""
using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value
by its alphabetical position in the list to obtain a name score.
For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the
938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
What is the total of all the name scores in the file?

Answer:
    871198282
Completed on Tue, 21 Jun 2016, 18:12
"""
import csv


def main(f='names.txt'):
    names = get_names(f)

    scores_sum = 0
    for i, n in enumerate(names):
        scores_sum += get_name_score(n) * i

    return scores_sum


def get_names(f):
    """
    extracts all the names from the given file and formats them into a sorted list
    :param f: <str> the path for the file holding the names
    :return: <list> the names from f in alphabetical order
    """
    names = ['']

    with open(f, 'r') as names_file:
        reader = csv.reader(names_file)
        for row in reader:
            names.extend(row)

    return sorted(names)


def get_name_score(name):
    """
    calculates the score for a name
    ex: COLIN -> 3 + 15 + 12 + 9 + 14 = 53
    :param name: <str> the name you want to find the score for
    :return: <int> the score of the given name
    """
    name = name.upper()
    name_score = 0

    alphabet = {'A': 1,
                'B': 2,
                'C': 3,
                'D': 4,
                'E': 5,
                'F': 6,
                'G': 7,
                'H': 8,
                'I': 9,
                'J': 10,
                'K': 11,
                'L': 12,
                'M': 13,
                'N': 14,
                'O': 15,
                'P': 16,
                'Q': 17,
                'R': 18,
                'S': 19,
                'T': 20,
                'U': 21,
                'V': 22,
                'W': 23,
                'X': 24,
                'Y': 25,
                'Z': 26}

    for l in name:
        name_score += alphabet[l]

    return name_score

# # # #


if __name__ == '__main__':
    print main()
