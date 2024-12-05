# File: pa3.py
# Author: Marissa Esteban and Gabriel Krishnadasan
# Date: 4/14/23
# Description: Returns centeralized coordinates and the maximum number of stones in a given a distance


def solve(filename):
    """
    Solves pa3.  Input to problem is in the file named filename.
    Output should be printed to standard output (using print statement).

    to convert from i, j to c, r:

    c = (i + j) / 2
    r = (j - i) / 2
    """

    cases = read_data(filename)
    answers = []

    #Does this for every case in the test
    for i in range(len(cases)):
        ijStones = convertStones(cases[i][1])

        #number of columns and rows in case i
        cols = cases[i][0][0]
        rows = cases[i][0][1]

        #Creates variables for i, j grid
        minCol = 1 - rows
        maxCol = cols - 1
        minRow = 2
        maxRow = cols + rows

        countMatrix = createCountMatrix(minCol, maxCol, minRow, maxRow, ijStones)

        answers.append(calculateStones(cases[i], countMatrix, minCol, minRow, cols, rows))

    # printing each query for each case
    for i in range(len(answers)):
        print("Case " + str(i + 1) + ":")
        for j in range(len(answers[i])):
            c = str(answers[i][j][1][0])
            r = str(answers[i][j][1][1])
            print(str(answers[i][j][0]) + " (" + c + "," + r + ")")

def convertStones(locations):
    """
    Converts the locations of stones from c,r to i,j

    locations: list of c,r coordinates

    returns:
        newLocations: list of i,j coordinates

    """
    newLocations = []
    for item in locations:
        i = int(item[0]) - int(item[1])
        j = int(item[0]) + int(item[1])
        newLocations.append((i, j))
    return newLocations

def createCountMatrix(minCol, maxCol, minRow, maxRow, stoneLocations):
    """
    Creating the count matrix populated by the number of stones from bottom left corner to i,j

    minCol, maxCol, minRow, maxRow : int values of min/max of each axis
    stoneLocations: list of i,j coordnates of each stone

    returns:
        countMatrix: 2d array populated with number of stones from bottom left corner to i,j
        
    """
    stoneLocationMatrix = []
    for j in range(minCol, maxCol + 1):
       
       # priming matrix with values of 0
       temp = []
       for k in range(minRow, maxRow + 1):
           temp.append(0)
       stoneLocationMatrix.append(temp)
        
    # if there is a stone, making the value equal to 1
    for j in range(len(stoneLocations)):
        col = stoneLocations[j][0]
        row = stoneLocations[j][1]
        stoneLocationMatrix[col + abs(minCol)][row - minRow] = 1
        
    #Creating the count matrix, the number of stones between minCol, minRow and j, k
    countMatrix = []
    for m in range(len(stoneLocationMatrix)):
        temp = []
        count = 0

        for k in range(len(stoneLocationMatrix[m])):
            if m == 0 and k == 0:
                temp.append(stoneLocationMatrix[m][k])
            elif m == 0:
                temp.append(stoneLocationMatrix[m][k] + count)

            elif k == 0:
                temp.append(countMatrix[m - 1][k] + stoneLocationMatrix[m][k])
            else:
                temp.append(countMatrix[m - 1][k] + stoneLocationMatrix[m][k] + count)
            
            if stoneLocationMatrix[m][k] == 1:
                count += 1
        countMatrix.append(temp)

    return countMatrix

def calculateStones(cases, countMatrix, minCol, minRow, cols, rows):
    """
    Calculates the number of stones in a given distance

    countMatrix: 2d array populated with number of stones from bottom left corner to m,k
    minCol, minRow: int min values in i,j coordinate form
    cols, rows: int number of cols and rows in c,r

    returns:
        caseAnswers: a list of (maxStones, maxCoords) for each query in case
        
    """

    caseAnswers = []

    # iterate through every query in the case
    for q in range(len(cases[2])):
        queryNum = cases[2][q]
        maxStones = 0
        maxCoords = ()

        # calculate number of stones in query distance for each coord in c,r
        for c in range(1, cols + 1):
            for r in range(1, rows + 1):

                # convert c,r to i,j, to m,k
                cToi = c - r
                rToj = c + r

                cToi += abs(minCol)
                rToj -= minRow

                # corners of surrounding squares
                xPlusQuery = cToi + queryNum
                yPlusQuery = rToj + queryNum
                xMinusQuery = cToi - queryNum - 1
                yMinusQuery = rToj - queryNum - 1

                if xPlusQuery >= len(countMatrix):
                    xPlusQuery = len(countMatrix) - 1
                if yPlusQuery >= len(countMatrix):
                    yPlusQuery = len(countMatrix) - 1

                # number of stones in framing rectangles and subtracting them
                if xMinusQuery < 0 and yMinusQuery < 0:
                    stones = countMatrix[xPlusQuery][yPlusQuery]
                elif xMinusQuery < 0:
                    stones = countMatrix[xPlusQuery][yPlusQuery] - countMatrix[xPlusQuery][yMinusQuery]
                elif yMinusQuery < 0:
                    stones = countMatrix[xPlusQuery][yPlusQuery] - countMatrix[xMinusQuery][yPlusQuery]
                else:
                    stones = countMatrix[xPlusQuery][yPlusQuery] - countMatrix[xMinusQuery][yPlusQuery] - countMatrix[xPlusQuery][yMinusQuery] + countMatrix[xMinusQuery][yMinusQuery]


                # updating maxStones and maxCoords
                if stones > maxStones or maxCoords == ():
                    maxStones = stones
                    maxCoords = (c, r)
                elif stones == maxStones:
                    if r < maxCoords[1]:
                        maxCoords = (c, r)

        caseAnswers.append((maxStones, maxCoords))
    return caseAnswers

def read_data(filename):
    """
    Reads data from file, returns three lists

    Case info:
        caseInfo: tuple
        caseInfo: num columns, num rows, num stones, num queries
    
    Stone Location:
        stoneLocation: list of tuples of the coordinates
    
    Query Number:
        queryNumbers: 2D list
        queryNumbers[a][0-n]: a = case number
                              0-n = query number
    """


    cases = []
    
    # reading file data
    file = open(filename)

    line = file.readline()

    while True:
        stoneLocation = []
        queryNumbers = []

        line = line.split()

        if all([v == "0" for v in line]):
            return cases

        caseInfo = (int(line[0]), int(line[1]), int(line[2]), int(line[3]))

        for i in range(caseInfo[2]):
            location = file.readline().split()
            stoneLocation.append(location)
        
        for i in range(caseInfo[3]):
            query = file.readline()
            queryNumbers.append(int(query))

        cases.append((caseInfo, stoneLocation, queryNumbers))
        
        line = file.readline()



if __name__ == "__main__":
    solve("test3.in")

