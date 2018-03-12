# -*- coding: utf-8 -*-
"""
In the 20×20 grid below, four numbers along a diagonal line have been marked.
    08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
    49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
    81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
    52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
    22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
    24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
    32 98 81 28 64 23 67 10 '26' 38 40 67 59 54 70 66 18 38 64 70
    67 26 20 68 02 62 12 20 95 '63' 94 39 63 08 40 91 66 49 94 21
    24 55 58 05 66 73 99 26 97 17 '78' 78 96 83 14 88 34 89 63 72
    21 36 23 09 75 00 76 44 20 45 35 '14' 00 61 33 97 34 31 33 95
    78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
    16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
    86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
    19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
    04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
    88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
    04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
    20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
    20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
    01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally)
 in the 20×20 grid?

Answer:
    70600674
Completed on Wed, 15 Jun 2016, 02:43
"""
from Problem8 import product


def main(grid, n=4):
    """
    break the N by N grid down into n by n sub grids
    then find the row, column, and diagonal products of each of those sub grids
    compare the max of the sub grid products to the current max overall product
    :param grid: <string> N by N grid of integers
    :param n: <int> the number of adjacent integers to use to form a product
    :return: <int> max n product of the grid
    """
    max_product = 0

    list_of_lists = format_grid(grid)

    for sub_grid in generate_subgrids(list_of_lists, n):
        subgrid_products = get_products(sub_grid)
        max_subgrid_product = max(subgrid_products)
        if max_subgrid_product > max_product:
            max_product = max_subgrid_product

    return max_product


def format_grid(grid):
    """
    formats the grid into a list of lists
    :param grid: <string> N by N grid of integers
    :return: <list> formatted grid
    """
    matrix = []

    for row in grid.split("\n"):
        matrix.append([int(col) for col in row.split(" ")])

    return matrix


def generate_subgrids(grid, n):
    """
    breaks the formatted parent grid into n by n sub grids
    :param grid: <list> parent (N by N) grid
    :param n: <int> dimension of the sub grids
    :return: <generator> n by n sub grid
    """
    for i in range(len(grid) - n):
        rows = grid[i: i + n]
        '''
        get the rows from the grid in groups of n
        '''
        for j in range(len(rows[0]) - n):
            sub_matrix = [cols[j: j + n] for cols in rows]
            '''
            grab the columns from those rows in groups of n
            '''
            yield sub_matrix


def get_products(sub_grid):
    """
    gets the row, column, and diagonal products of a sub grid
    :param sub_grid: <list> n by n sub grid
    :return: <list> row, column, and diagonal products
    """
    dimensions = len(sub_grid)
    products = []
    '''
    get the product for each row
    '''
    for row in sub_grid:
        products.append(product(row))
    '''
    get the product for each column
    '''
    for col in range(dimensions):
        products.append(product(r[col] for r in sub_grid))
    '''
    get the product for the diagonals
    '''
    products.append(product(sub_grid[index][index] for index in range(dimensions)))
    products.append(product(sub_grid[index][(dimensions-1) - index] for index in range(dimensions)))

    return products

# # # #


if __name__ == '__main__':
    grd = '\
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08\n\
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00\n\
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65\n\
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91\n\
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80\n\
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50\n\
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70\n\
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21\n\
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72\n\
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95\n\
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92\n\
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57\n\
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58\n\
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40\n\
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66\n\
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69\n\
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36\n\
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16\n\
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54\n\
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'

    print main(grd)
