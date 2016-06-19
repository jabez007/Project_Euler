# -*- coding: utf-8 -*-
"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.
    example.jpg
How many such routes are there through a 20×20 grid?

Answer:
    137846528820
Completed on Sun, 19 Jun 2016, 15:33
"""


def main(n=20):
    """
    We can treat the n x n grid like an (n+1) x (n+1) graph
    Then we can use an adjacency matrix to calculate the number of paths from the upper left to lower right

    We can see that the length of each path from the upper left to the lower right is going to be 2n
    because we eventually have to move to the right n spaces and move down n spaces. Since we can't move in any other
    directions, we won't have any more spaces to cover than that. Also, there is no "physical" way to have any path
    shorter than that

    This means we can raise our adjacency matrix to the n*n power to find the number of paths of length n*n between any
    two nodes on the graph and look at the last element of the first row to find the number of paths from the upper left
    to lower right
    :param n: <int> size of our grid
    :return: answer
    """
    matrix = adjacency_matrix(n)
    paths = number_of_paths(matrix, 0, (n+1)*(n+1) - 1, 2*n)
    return paths


def adjacency_matrix(n):
    """
    Creates the adjacency matrix for an n x n grid as though it were an (n+1) x (n+1) directed graph
    :param n: <int> the size of your grid
    :return: <list> adjacency matrix for a directed graph (full of 0's and 1's)
    """
    matrix = list()
    nodes = range((n+1)**2)
    for row in nodes:
        r = list()
        for col in nodes:
            if col == row + 1:  # we can move to the right
                r.append(1)
            elif col == row + (n+1):  # or we can move down
                r.append(1)
            else:  # otherwise, this node isn't connected for our problem
                r.append(0)
        matrix.append(r)
    return matrix


def matrix_power(matrix, exponent):
    """
    raises the given matrix to the given power through matrix multiplication
    :param matrix: <list> of lists of integers. Should be a square matrix to allow self multiplication
    :param exponent: <int> the number of times we want to multiply the matrix by itself
    :return: <list> the overall result of the multiplications
    """
    matrix_a = matrix
    matrix_b = matrix
    while exponent > 1:
        matrix_a = multiply_matrices(matrix_a, matrix_b)
        exponent -= 1
    return matrix_a


def multiply_matrices(a, b):
    """
    multiplies two matrices together.
    Does NOT validate that the two matrices can be multiplied together, that is it does not compare the dimensions of
    the matrices to determine their compatibility
    :param a: <list> of lists of integers. The number of columns in a should match the number of rows in b
    :param b: <list> of lists in integers. The number of rows in b should match the number of columns in a
    :return: <list> the result of the multiplication
    """
    b_cols = len(b[0])

    matrix = list()

    for row in a:  # take each row of matrix A
        multiplied_row = list()
        for i in range(b_cols):  # and for each column in matrix B
            terms = list()
            for j, elm in enumerate(row):
                '''
                multiply each element of the row from A by the corresponding
                element in the current column from B
                '''
                terms.append(elm * b[j][i])
            '''
            then sum all of those products
            '''
            multiplied_row.append(sum(terms))
        matrix.append(multiplied_row)

    return matrix


def number_of_paths(adj_matrix, node_a, node_b, length):
    """
    uses the adjacency matrix of a graph to calculate the number of paths from node_a to node_b of given the length by
    multiplying the adjacency matrix by the column for node_b from the adjacency matrix length number of times.
    :param adj_matrix: <list> the adjacency matrix of our graph
    :param node_a: <int> the index for our starting node
    :param node_b: <int> the index for our ending node
    :param length: <int> the length of the paths between node_a and node_b
    :return: <int> the number of paths of the given length going from node_a to node_b
    """
    matrix_b = list()
    '''
    get the column for the adjacency to node b
    '''
    for row in adj_matrix:
        matrix_b.append([row[node_b]])

    '''
    multiply the adjacency matrix by the column for node b as though we are raising the adjacency matrix to the length
    power to find the number of paths to node_b of that length
    '''
    while length > 1:
        matrix_b = multiply_matrices(adj_matrix, matrix_b)
        length -= 1

    '''
    Then return the node_a row of the node_b column for the number of paths from node_a to node_b
    '''
    return matrix_b[node_a][0]

# # # #


if __name__ == '__main__':
    print main()
