# -*- coding: utf-8 -*-
"""
The following iterative sequence is defined for the set of positive integers:
    n → n/2 (n is even)
    n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.

Answer:
    837799
Completed on Fri, 17 Jun 2016, 02:25
"""


def main(n=1000000):
    max_length = 0
    max_sequence = []
    sequences = get_sequences(n)
    for seq in sequences.values():
        if len(seq) > max_length:
            max_length = len(seq)
            max_sequence = seq
    return max_sequence[0], max_length


def get_sequences(n):
    """
    Finds all the Collatz sequences for the integers up to n
    :param n: <int> the upper limit for the Collatz sequences to calculate
    :return: <dict> Key = starting integer, Value = Collatz sequence for starting integer
    """
    track = {}
    for i in range(1, n):
        if i in track:
            continue
        sequence = collatz_sequence(i)
        '''
        keep track of the sequences we've calculated so far
        '''
        track[i] = sequence

        for j, k in enumerate(sequence):
            if k in track:
                continue
            '''
            terms in the sequence can go over n, but we don't want to keep track of those
            '''
            if k > n:
                continue
            '''
            we can also keep track of all the sub-sequences so we don't have to actually calculate all 1,000,000
            '''
            track[k] = sequence[j:]
    return track


def collatz_sequence(n=13):
    """
    Given a starting number n, calculates a list of integers that terminates with 1 such that
        n → n/2 (n is even)
        n → 3n + 1 (n is odd)
    :param n: <int> starting number for the list of integers
    :return: <list> integers that make up the Collatz sequence for n
    """
    sequence = list()

    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1

    sequence.append(n)  # add the 1 that ends the sequence on to the end
    return sequence

# # # #


if __name__ == "__main__":
    print main()
