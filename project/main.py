from game_logic.sudoku_logic import solveSudoku

arr = [
    [4, '*', '*', '*', 1, 3, 5, '*', '*'],
    [6, 8, '*', 2, '*', 4, 1, 9, '*'],
    ['*', '*', '*', '*', '*', 7, '*', '*', 2],
    [3, 4, 9, '*', '*', '*', '*', '*', '*'],
    ['*', 7, 1, '*', '*', 5, '*', 2, 6],
    ['*', 5, '*', 8, 9, '*', '*', 7, 3],
    ['*', '*', 2, '*', 7, '*', 6, '*', 5],
    ['*', '*', 4, '*', 3, '*', 2, 1, '*'],
    [5, 9, '*', '*', 6, 2, '*', '*', 4],
]

newArr = solveSudoku(arr)
for i in range(0,9):
    print(newArr[i])
