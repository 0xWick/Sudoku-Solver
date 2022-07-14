import numpy as np


grid = [[0, 5, 8, 0, 0, 3, 1, 0, 0],
        [3, 9, 0, 1, 6, 0, 7, 0, 2],
        [0, 1, 0, 0, 0, 0, 4, 0, 3],
        [0, 0, 2, 7, 3, 0, 6, 1, 0],
        [1, 0, 0, 0, 0, 0, 9, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 4, 0, 9, 6],
        [8, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 9, 0, 1, 0, 0, 0]]

print("-------Unsolved------")
print(np.matrix(grid))


def possible(y, x, n):
    global grid
    # Checking Rows
    for i in range(0, 9):
        if grid[x][i] == n:
            return False
    # Checking Columns
    for i in range(0, 9):
        if grid[i][y] == n:
            return False
        # Checking the Box (3X3)
    x0 = x//3 * 3
    y0 = y//3 * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[x0+i][y0+j] == n:
                return False
    return True


def solver():
    global grid
    # Checking Rows (Lists in the grid(main list) )
    for x in range(9):
        # Checking Columns (Each number in the current list)
        for y in range(9):
            # Checking for empty position
            if grid[x][y] == 0:
                # Looping through 1-9 numbers to see
                # what num to we can put here currently
                for n in range(1, 10):
                    if possible(y, x, n):
                        # if it's possible, lets put the
                        # number in that position
                        grid[x][y] = n
                        # Recall Recursion at this
                        # point from the video.
                        # This is complicated
                        # but you can handle it.
                        solver()
                        # If the function fails to find the
                        # answer for the next empty it will
                        # return and we will know we were wrong.
                        # And set the value back to zero
                        # and try a new number (Backtracking).
                        # Imp Note: One number is being checked
                        # for the whole puzzle in Recursion.
                        grid[x][y] = 0

                # This return will be used in the above
                # called function when we want to
                # get out of the recursion(or inception)
                return
    print("-------Solved------")
    print(np.matrix(grid))


solver()

