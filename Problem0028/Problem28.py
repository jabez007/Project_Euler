"""
Starting with the number 1 and moving to the right in a clockwise 
direction a 5 by 5 spiral is formed as follows:

    21 22 23 24 25
    20  7  8  9 10
    19  6  1  2 11
    18  5  4  3 12
    17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
formed in the same way?

Answer:
	669171001
Completed on Sun, 9 Oct 2016, 14:34
"""


def main(n=1001):
    grid = spiral_grid(n)
    return sum_diagonals(grid)


def sum_diagonals(grid):
    dim = len(grid)
    x = y = dim/2
    
    return sum_down_diagonal(grid) + sum_up_diagonal(grid) - grid[y][x]    


def sum_down_diagonal(grid):
    terms = list()
    for i in range(len(grid)):
        terms.append(grid[i][i])
        
    return sum(terms)
    

def sum_up_diagonal(grid):
    flipped_grid = list()
    for row in grid:
        flipped_grid.append(row[::-1])
        
    return sum_down_diagonal(flipped_grid)


def spiral_grid(n=5):
    """
    yes, to solve just this problem all I need to know are the diagonals.
    So the simple solution would be to just find the pattern for the
    numbers on the diagonals, but wheres the fun in that?
    This, I think, is a bit more interesting and makes this solution
    perhaps more useful outside of this problem.
    """
    # even dimensions dont apply to this problem.
    if n%2 == 0:
        return list()
    
    grid = list()
    for r in range(n):
        grid.append([0]*n)
    
    x_start = y_start = x = y = n/2
    grid[y_start][x_start] = 1
    
    for dim in range(1, n+1, 2):
        left_column = x_start - (dim/2)
        top_row = y_start - (dim/2)
        bottom_row = y_start + (dim/2)
        right_column = x_start + (dim/2)
        
        in_right_column = False
        in_bottom_row = False
        in_left_column = False
        in_top_row = False
        
        for i in range(((dim-2)**2)+1, (dim**2)+1):            
            # clockwise rotation
            
            # start
            if not any(place for place in [in_right_column, in_bottom_row, in_left_column, in_top_row]):
                if x+1 == right_column:
                    in_right_column = True
                    x += 1
                    grid[y][x] = i
                    continue
                
            if in_right_column:
                if y+1 == bottom_row:
                    in_bottom_row = True
                    in_right_column = False
                
                if y+1 <= bottom_row:
                    y += 1
                
                grid[y][x] = i
                continue
                 
            if in_bottom_row:
                if x-1 == left_column:
                    in_left_column = True
                    in_bottom_row = False
                    
                if x-1 >= left_column:
                    x -= 1
                
                grid[y][x] = i
                continue
            
            if in_left_column:
                if y-1 == top_row:
                    in_top_row = True
                    in_left_column = False
                    
                if y-1 >= top_row:
                    y -= 1
                    
                grid[y][x] = i
                continue
                    
            if in_top_row:
                if x+1 == right_column:
                    in_right_column = True
                    in_top_row = False
                    
                if x+1 <= right_column:
                    x += 1
                    
                grid[y][x] = i
                continue
    
    return grid
    
# # # #


if __name__ == "__main__":
    print main()
