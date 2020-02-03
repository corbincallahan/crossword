import random

def printGrid(grid):
    for row in grid:
        print(row)
    print()

def getRow(grid, num):
    return grid[num]

def getCol(grid, num):
    col = []
    for i in range(5):
        col.append(grid[i][num])
    return col

def writeRow(grid, num, word):
    for i in range(5):
        grid[num][i] = word[i]

def writeCol(grid, num, word):
    for i in range(5):
        grid[i][num] = word[i]

def testWriteRow(grid, num, word):
    grid = list(grid)
    for i in range(5):
        grid[num][i] = word[i]
    return grid

def testWriteCol(grid, num, word):
    grid = list(grid)
    for i in range(5):
        grid[i][num] = word[i]
    return grid

def testWrite(grid, num, word):
    if(num < 5):
        return testWriteRow(grid, num, word)
    else:
        return testWriteCol(grid, num - 5, word)

def fittingWords(present, words):
    words = list(words)
    for i in range(5):
        if(present[i] != ' '):
            for j in range(len(words) - 1, -1, -1):
                if(words[j][i] != present[i]):
                    words.pop(j)
    return words

def getNumPossible(grid, words):
    numPossible = []
    for i in range(5):
        numPossible.append(len(fittingWords(getRow(grid, i), words)))
    for i in range(5):
        numPossible.append(len(fittingWords(getCol(grid, i), words)))
    return numPossible

def getOptimalWord(grid, position, words):
    max = -1
    maxIndex = -1
    for i in range(len(words)):
        result = testWrite(grid, position, words[i])
        min = getMin(getNumPossible(result, words))
        if(min > max):
            maxIndex = i
            max = min
    return words[maxIndex]

def getMin(list):
    min = 4267
    for item in list:
        if(item < min):
            min = item
    return min

dictionary = open('5dict.txt', 'r')
words = []
for word in dictionary:
    words.append(word[:-1])

grid = [[' ' for i in range(5)] for j in range(5)]

# Add starting words here
# writeRow(grid, 2, 'happy')

printGrid(grid)

filled = []
for i in range(5):
    if ' ' in getRow(grid, i):
        filled.append(False)
    else:
        filled.append(True)
for i in range(5):
    if ' ' in getCol(grid, i):
        filled.append(False)
    else:
        filled.append(True)

while(False in filled):
    numPossible = getNumPossible(grid, words)
    minIndex = -1
    min = 4267
    for i in range(len(numPossible)):
        if(numPossible[i] < min and not filled[i]):
            minIndex = i
            min = numPossible[i]

    if(minIndex < 5):
        writeRow(grid, minIndex, getOptimalWord(grid, minIndex, fittingWords(getRow(grid, minIndex), words)))
    else:
        writeCol(grid, minIndex - 5, getOptimalWord(grid, minIndex, fittingWords(getCol(grid, minIndex - 5), words)))
    filled[minIndex] = True

    printGrid(grid)

    if 0 in getNumPossible(grid, words):
        print("NO SOLUTIONS REMAINING")
        exit()