"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top
to bottom is 23.
       3
      7 4
     2 4 6
    8 5 9 3
That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom of the triangle below:
                                75
                              95 64
                            17 47 82
                          18 35 87 10
                        20 04 82 47 65
                      19 01 23 75 03 34
                    88 02 77 73 07 63 67
                  99 65 04 28 06 16 70 92
                41 41 26 56 83 40 80 70 33
              41 48 72 33 47 32 37 16 94 29
            53 71 44 65 25 43 91 52 97 51 14
          70 11 33 28 77 73 17 78 39 68 17 57
        91 71 52 38 17 14 91 43 58 50 27 29 48
      63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67,
is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a
clever method! ;o)

Answer:
    1074
Completed on Mon, 20 Jun 2016, 22:32
"""


def main(string):
    """
    My first idea was to start from the top and to decide left or right by which number was larger. That didn't work.
        75 + 95 + 47 + 87 + 82 + 75 + 73 + 28 + 83 + 47 + 43 + 73 + 91 + 67 + 98 = 1064

    My second idea, work from the bottom up. Condense the triangle down to just two rows, then the answer is easy.

    :param string: <str> triangle of integers
    :return: <tuple> the largest sum with the path that gets us there
    """
    triangle = str_to_triangle(string)
    return condense_triangle(triangle)


def str_to_triangle(string):
    """
    takes a triangle of integers as a string and formats it into a list of lists
    :param string: <str> a triangle of integers
    :return: <list> the triangle of integers formatted into a list of lists of integers
    """
    triangle = list()
    for r in string.split("\n"):
        row = [int(n) for n in r.split(" ")]
        triangle.append(row)
    return triangle


def condense_triangle(triangle):
    """
    Condenses a given triangle down to its largest possible sum if we were fall through it Plinko style
    :param triangle: <list> of lists of integers with length of each subsequent row increasing by 1
    :return: <tuple> the max possible sum and the used to get there
    """
    track = dict()  # some how keep track of the terms that give us the max sum

    while len(triangle) > 1:
        condensed_row = list()
        for i, elm in enumerate(triangle[-2]):  # go through all of the elements of the second to last row
            '''
            add the larger of the right and left elements from the row below to create the new, condensed row.
            '''
            if triangle[-1][i] >= triangle[-1][i+1]:
                max_bottom = triangle[-1][i]
                max_bottom_index = i
            else:
                max_bottom = triangle[-1][i+1]
                max_bottom_index = i+1

            max_sum = elm + max_bottom
            condensed_row.append(max_sum)
            '''
            And keep track of the terms of each branch as we go
            '''
            if i in track:
                track[i] = [elm] + track[max_bottom_index]
            else:
                track[i] = [elm, max_bottom]

        triangle = triangle[:-2] + [condensed_row]  # then replace the bottom two rows with the new, condensed row.

    return triangle[0][0], track[0]

# # # #

if __name__ == '__main__':
    tri = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
    answer = main(tri)
    print answer
    print sum(answer[1])
