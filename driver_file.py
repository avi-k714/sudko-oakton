# Let's put all our code here

'''
CSC 255 OC1 - Group Assignment
Sudoku Solver
'''

'''
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
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


def printPuzzle()               #Thuy

def checkifPuzzleComplete()     #Thuy

def checkEmptyCells()           #Sebastian

def solveBacktracking()         #Sebastian

def candidateNumbers()          #Sebastian

def generateStartingBoard()      #Avi



'''