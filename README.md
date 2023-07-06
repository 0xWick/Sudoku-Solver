# Sudoku-Solver
Sudoku Puzzle game solver in python.
Currently you have to hard-code the puzzle values but the answer will be outputted automatically once you run the function.

# Explained!


Introduction:

I am writing this article for record in future and also for keeping a note of my journey in Programming. I will try to write one blog every week about fun projects of Programming. My focus will be mostly about Python and Machine Learning or AI in general. I might also do some introductory ones on Blockchain and Cryptography. Let’s see how it turns out!

Inspiration:

I had the idea of making a Python Sudoku Solver for a while now. While I was watching Computerphile videos on YouTube I came across a video about a Python Sudoku Solver. But it was very much on-point and not so much self-explanatory.
So, I decided to break each step down and explain at a beginner level.

If you are familiar with the rules of Sudoku Puzzle, you can skip the next Paragraph.

Sudoku:

Image Credit: ”https://www.freepik.com/photos/puzzle" Puzzle photo created by freepik — www.freepik.com


It’s a 9 X 9 grid of boxes

Basically, its a game with 3 main rules. You have to put a number (or integer in programming terms) in all boxes. But
Numbers mustn't repeat in the same

Row
Column
Box (3X3)
Note: There can be more than 1 solution to a Sudoku Puzzle.

With that out of the way, let’s get technical now!

Main Concepts:

I have listed some main concepts that will be used in this tutorial. Although, I have tried to explain it but you can use Youtube or Google too to get a better understanding.

2d Lists (or Arrays) - optional
Numpy (Matrix only) - optional
Recursion (It’s roughly like inception movie). This video can help (https://www.youtube.com/watch?v=Mv9NEXX1VHc&ab_channel=Computerphile)
BackTracking (Trial & Error)
A little Math
Let’s get started:

First, assign the rows as lists into a single list. (You will find out why its important.)

Code:
import numpy as np
grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]
print("-------Unsolved------")
print(np.matrix(grid))
Output:
-------Unsolved------
[[5 3 0 0 7 0 0 0 0]
 [6 0 0 1 9 5 0 0 0]
 [0 9 8 0 0 0 0 6 0]
 [8 0 0 0 6 0 0 0 3]
 [4 0 0 8 0 3 0 0 1]
 [7 0 0 0 2 0 0 0 6]
 [0 6 0 0 0 0 2 8 0]
 [0 0 0 4 1 9 0 0 5]
 [0 0 0 0 8 0 0 7 9]]
Process finished with exit code 0
We will do it in three sections.

Checking the number in row
Checking the number in column
Checking the number in the box
We will define a function for checking row and then add column check to it. We will do a different function for the box(it’s a little more complicated)

-Checking the number in the row:

Let’s start with checking if the number we want is in the same row or not. We can use a simple for loop that will check every number in the row we give as argument in the function.

# x for rows
# y for columns
# i for iterations. duh!!
def possible(y, x, n):
    global grid
    # Checking Rows
    for i in range(0, 9):
        if grid[x][i] == n:
            return False
This function will return False if the number (n) is already in the row we defined.

-Checking the number in the column:

Now let’s add the column check into this function…

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
This function return False if the number (n) is either in the same column or row.

-Checking the number in the box(3X3):

For checking the box you need to know a mathematical term known as Floor Division (Google or Youtube pls).

# Checking the Box (3X3)
x0 = x//3 * 3
y0 = y//3 * 3
for i in range(0, 3):
    for j in range(0, 3):
        if grid[x0+i][y0+j] == n:
            return False
First two lines are the math. In simple words, it resets the grid to a specific number for a bunch of numbers. We use this to get the start of the box for any number in any box. Like,
the start will be 0 if x = 0 or 1 or 2
similarly, start is 3 if x = 3 or 4 or 5
and 6 while x = 6 or 7 or 8.
See, how this resets the any number in a block to the starting point of that block.

Moving on, we use nested for loop with range 3. To check 3x3 boxes of the Box.
Also, we add the i and j into x0 and j0 respectively to checking the next block and the next block so on to the last block in the box.
With this we can loop (i and j) and check all 9 blocks 1-by-1 to see if number (n) is already in the box or not.

First Section wind up:

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
So far, we have made a checker to see if its possible to put a number at a specific position in the puzzle. But as Programming our laziness urge us to automate the whole process. Instead of checking every box manually.

Also, the second section isn’t only for automation but it gives another important function to our program i.e. Trial and Error. Because possible() only tell us if a number can be placed in a specific position but there can be many possibilities for a specific position. Our choice now can prove to be wrong later. That’s why we need Trial and Error (Backtracking and Recursion).

Second Section:

We loop through all numbers 0–8 in rows and columns to check the position with possible(). But first we check if the position is empty i.e. 0. Then use possible() and a loop to check which of the number we can put there currently (we might be wrong and won’t put the same number again and again hence I use able to put currently)

def solver():
    global grid
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
Now we are going to use the most important and complicated method to solve this puzzle.

Recursion:
Try to understand recursion using this meme:


Look how you got the answer at 5th recursion. That’s when you get out of the recursion. Use the computerphile with this meme to understand it properly!

Simply put in this method, we keep finding the answer and putting it in the empty spot until we can’t find the answer for the next empty position. In which case, we return. But we returned from a recursed function not the main or most outer function. Re-watch the recursion video if you feel lost.

BackTracking:


So, if we fail to find all answers with a number we simply change it to zero and try the next number. Google: Backtracking. To understand how we use Trial and Error to solve this.

This process of recursion and backtracking will keep going on until we find the answers to all empty spaces that satisfy our conditions in possible().

That’s when we return from our main function or the most outer layer of our function.

Finally,

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
# Don't break your keyboard because you haven't called the function XD
If you feel lost at any point regarding Backtracking or Recursion just Google or Find Computerphile's tutorial on YouTube about it.

Also watch this video for a overview of this puzzle: https://www.youtube.com/watch?v=G_UYXzGuqvM&ab_channel=Computerphile

Well, that was my first article and I hope to get better at writing and my Knowledge.
Stay tuned for further Python Fun Projects and Computer Science (Especially ML, AI, Crypto and Tech) related Blogs.

JazakAllah for reading and your feedback means a lot for me.

This Blog is also a bookmark for my future self to compare if I am better today when I was at the time of writing this!

Process finished with exit code 0

# To-Do

-> Make GUI for taking input of the game values from user
-> Output the answer in the same GUI back to the user

