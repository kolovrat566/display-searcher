def whatSquere(position):
    if ((position >= 0) & (position <= 2)):
        return 0
    if ((position >= 3) & (position <= 5)):
        return 1
    if ((position >= 6) & (position <= 8)):
        return 2

def getPossibleValues(arr, position): 
    possibleValues = list(range(1,10))
    squareX = whatSquere(position[0])
    squareY = whatSquere(position[1])
    square = []
    for i in range(3 * squareX, 3 * squareX + 3):
        for j in range(3 * squareY, 3 * squareY + 3):
            square.append(arr[i][j])

    for i in range(0,9):
        if ((arr[position[0]][i] != '*') & (arr[position[0]][i] in possibleValues)):
            possibleValues.remove(arr[position[0]][i])

        if ((arr[i][position[1]] != '*') & (arr[i][position[1]] in possibleValues)):
            possibleValues.remove(arr[i][position[1]])

        if ((square[i] != '*') & (square[i] in possibleValues)):
            possibleValues.remove(square[i])

    return possibleValues

def pasteValue(arr):
    newArr = arr
    for i in range(0, 9):
        for j in range(0, 9):
            if (arr[i][j] == '*'):
                if (len(getPossibleValues(arr, [i, j])) == 1):
                    newArr[i][j] = getPossibleValues(arr, [i, j])[0]
                else: 
                    newArr[i][j] = '*'
            else: newArr[i][j] = arr[i][j]

    return newArr

def haveStar(arr):
    for i in range(0,9):
        for j in range(0, 9):
            if (arr[i][j] == '*'): return True
    return False

def solveSudoku(arr):
    newArr = arr
    while(haveStar(newArr)):
        newArr = pasteValue(newArr)
    return newArr