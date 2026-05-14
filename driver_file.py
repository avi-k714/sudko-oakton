# Let's put all our code here

'''
CSC 255 OC1 - Group Assignment
Sudoku Solver
'''

import random

puzzle = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]


def checkValidMove(puzzle, row, col, value):        #Avi
    #Function: Return True if value can be placed in that box
    #Approach: Check Row and Column and the 3 by 3 box to ensure that the 
        #value is not already present in either of these

    if value in puzzle[row]:
        return False

    for r in range(9):
        if puzzle[r][col] == value:
            return False

    box_r = 3 * (row // 3)
    box_c = 3 * (col // 3)

    for r in range(box_r, box_r + 3):
        for c in range(box_c, box_c + 3):
            if puzzle[r][c] == value:
                return False

    return True


#def printPuzzle()               #Thuy


#def checkifPuzzleComplete()     #Thuy

def checkEmptyCells(puzzle):           #Avi
    """Return (row, col) of the first empty cell, or None if full."""
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                return (r, c)
    return None

#def solveBacktracking()         #Sebastian

#def candidateNumbers()          #Sebastian

def fillBoard(puzzle):
    empty = checkEmptyCells(puzzle)
    if not empty:
        return True
    row, col = empty
    nums = list(range(1, 10))
    random.shuffle(nums)
    for value in nums:
        if checkValidMove(puzzle, row, col, value):
            puzzle[row][col] = value
            if fillBoard(puzzle):
                return True
            puzzle[row][col] = 0
    return False
    
def removeCells(puzzle, holes=40):
    removed = 0
    while removed < holes:
        r = random.randint(0, 8)
        c = random.randint(0, 8)
        if puzzle[r][c] != 0:
            puzzle[r][c] = 0
            removed += 1

def generateStartingBoard(puzzle):
    fillBoard(puzzle)
    removeCells(puzzle, holes=45)
    return puzzle


start_puzzle = generateStartingBoard(puzzle)