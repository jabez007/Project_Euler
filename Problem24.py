"""
A permutation is an ordered arrangement of objects. For example, 3124 is
one possible permutation of the digits 1, 2, 3 and 4. If all of the 
permutations are listed numerically or alphabetically, we call it 
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

Answer:
	2783915460
Completed on Wed, 2 Apr 2014, 03:08
"""

from itertools import permutations


def main(nth_permutation=1000000):
	permus = permutations(range(10))
	lexic = sorted(permus)
	return "".join(str(i) for i in lexic[nth_permutation-1])
	
# # # #


if __name__ == "__main__":
	print main()
