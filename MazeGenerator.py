import random, copy, turtle, numpy
from heapq import *

#pip install numpy

#http://www.roguebasin.com/index.php?title=Dungeon-Building_Algorithm
#https://www.dropbox.com/s/75ehmjklm118g05/dungeonGenerator.py?dl=0


def drawTurtle(maze):
    tortle = turtle.Turtle()
    scrn = turtle.Screen()
    tortle.hideturtle()
    tortle.speed(0)
    scrn.setworldcoordinates(0,0,len(maze)*5,len(maze[0])*5)
    tortle.pensize(1)
    scrn.tracer(9999)
    tortle.color('Green')
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            tortle.penup()
            tortle.goto(i*5,j*5)
            if maze[i][j] == 0:
                tortle.color('black')
            elif maze[i][j] == 5:
                tortle.color('green')
            elif maze[i][j] == 1:
                tortle.color('brown')
            elif maze[i][j] == 6:
                tortle.color('yellow')
            elif maze[i][j] == 7:
                tortle.color('pink')
            else:
                tortle.color('brown')
            tortle.pendown()
            tortle.begin_fill()
            tortle.seth(0)
            tortle.fd(5)
            tortle.seth(90)
            tortle.fd(5)
            tortle.seth(180)
            tortle.fd(5)
            tortle.seth(270)
            tortle.fd(5)
            tortle.end_fill()
    scrn.exitonclick()

def rectangle(maxRectSize, mapDimen):
    '''
    Randomly generates a location and size for a rectangle
    args:       maxRectSize     -   (int)Maximum length for the sides of the rectangle
                mapDimen        -   (int)Dimensions of the map
    return:     returns coordinates and side lengths for a generated rectangle
    '''
    xLen = random.randrange(5,(maxRectSize+1))
    yLen = random.randrange(5,(maxRectSize+1))
    bottomLeftXCord = random.randrange(0,(mapDimen-xLen))
    bottomLeftYCord = random.randrange(0,(mapDimen-yLen))
    return ([xLen, yLen, bottomLeftXCord, bottomLeftYCord])

def printMaze (maze):
    '''
    Prints a maze
    args:       maze     -   (2DArray/list/matrix)Maze to be printed
    return:
    '''
    for i in range (len(maze)):
        for j in range (len(maze[i])):
            print(str(maze[i][j]), end='')
        print()

def createBlankMaze(dimensions):
    '''
    Generates and returns a blank maze of size dimensions
    args:       dimensions     -   (int)Number for the dimensions of the map
    return:     returns a blank map/maze of size dimensions
    '''
    maz = [['█' for i in range(dimensions)] for j in range(dimensions)]
    return maz

def rectInsertHollow (maze, rect):
    '''
    Takes a maze and randomly generated rectangle and inserts the rectangle into the maze
    args:       maze        -   (array/list)Maze for the rectangle to be inserted
                rect        -   (rectangle data)data that describes the rectangle
    return:     returns a new maze with the rectangle inserted
    '''
    xLen, yLen, bottomLeftXCord, bottomLeftYCord = rect
    newMaze = copy.deepcopy(maze)
    for i in range (yLen):
        for j in range (xLen):
            newMaze[bottomLeftYCord+i][bottomLeftXCord] = '#' #Left Column
            newMaze[bottomLeftYCord][bottomLeftXCord+j] = '#' #Top Row
            newMaze[bottomLeftYCord+i][bottomLeftXCord+xLen-1] = '#' #Right Column
            newMaze[bottomLeftYCord+yLen-1][bottomLeftXCord+j] = '#' #Bottom Row
    return newMaze

def rectInsert (maze, rect):
    '''
    Takes a maze and randomly generated rectangle and inserts the rectangle into the maze
    args:       maze        -   (array/list)Maze for the rectangle to be inserted
                rect        -   (rectangle data)data that describes the rectangle
    return:     returns a new maze with the rectangle inserted
    '''
    xLen, yLen, bottomLeftXCord, bottomLeftYCord = rect
    newMaze = copy.deepcopy(maze)
    for i in range (yLen):
        for j in range (xLen):
            if newMaze[bottomLeftYCord+i][bottomLeftXCord+j] == '█':
                newMaze[bottomLeftYCord+i][bottomLeftXCord+j] = '@'
            else:
                return (maze, False)
    newMaze = rectInsertHollow (newMaze, rect)
    return (newMaze, True)

def insertLoop (numRects, maze, rectSize):
    '''
    Inserts a rectangle into the maze numRects times
    args:       numRects    -   (int)Number of rectangles to be put into the maze
                maze        -   (array/list)Maze to be altered
                rectSize    -   (int)Maximum size for the sides of the rectangles
    return:     returns a maze with numRects rectangles in it
    '''
    newMaze = maze[:]
    rectangles = []
    for i in range (numRects):
        recta = rectangle(rectSize, len(maze))
        (newMaze, check) = rectInsert(newMaze, recta)
        if check:
            rectangles.append(recta)
    return (newMaze, rectangles)

def generateMaze (mazeSize, numberOfRectangles, rectangleSize):
    '''
    Generates and returns a maze filled with rectangles
    args:
    return:     returns a maze filled with rectangles
    '''
    maze = createBlankMaze(mazeSize)
    (newestMaze, rectangles) = insertLoop (numberOfRectangles, maze, rectangleSize)
    if (len(rectangles)%2 == 0):
        return (newestMaze, rectangles)
    else:
        return (generateMaze(mazeSize, numberOfRectangles, rectangleSize))

# def testPointGenerator2 (i, pointList):
#     xLen, yLen, bottomLeftXCord, bottomLeftYCord = i
#     rectPerim = []
#     for i in range (yLen):
#         for j in range (xLen):
#             rectPerim.append((bottomLeftYCord+i,bottomLeftXCord,)) #Left Column
#             rectPerim.append((bottomLeftYCord,bottomLeftXCord+j,)) #Top Row
#             rectPerim.append((bottomLeftYCord+i,bottomLeftXCord+xLen-1,)) #Right Column
#             rectPerim.append((bottomLeftYCord+yLen-1,bottomLeftXCord+j,)) #Bottom Row
#     rectPerim = list(set(rectPerim))
#     newPerim = rectPerim[:]
#     cord1 = ((bottomLeftYCord, bottomLeftXCord,))
#     cord2 = ((bottomLeftYCord+yLen-1, bottomLeftXCord,))
#     cord3 = ((bottomLeftYCord, bottomLeftXCord+xLen-1,))
#     cord4 = ((bottomLeftYCord+yLen-1, bottomLeftXCord+xLen-1,))
#     newPerim.remove(cord1)
#     newPerim.remove(cord2)
#     newPerim.remove(cord3)
#     newPerim.remove(cord4)
#     val = len(newPerim)
#     randVal = random.randrange(val)
#     pointList.append(newPerim[randVal])
#     return pointList

def testPointGenerator (i, pointList):
    xLen, yLen, bottomLeftXCord, bottomLeftYCord = i
    xLen = xLen-2
    yLen = yLen-2
    bottomLeftXCord = bottomLeftXCord + 1
    bottomLeftYCord = bottomLeftYCord + 1
    rectPerim = []
    for i in range (yLen):
        for j in range (xLen):
            rectPerim.append((bottomLeftYCord+i,bottomLeftXCord,)) #Left Column
            rectPerim.append((bottomLeftYCord,bottomLeftXCord+j,)) #Top Row
            rectPerim.append((bottomLeftYCord+i,bottomLeftXCord+xLen-1,)) #Right Column
            rectPerim.append((bottomLeftYCord+yLen-1,bottomLeftXCord+j,)) #Bottom Row
    rectPerim = list(set(rectPerim))
    newPerim = rectPerim[:]
    # cord1 = ((bottomLeftYCord, bottomLeftXCord,))
    # cord2 = ((bottomLeftYCord+yLen-1, bottomLeftXCord,))
    # cord3 = ((bottomLeftYCord, bottomLeftXCord+xLen-1,))
    # cord4 = ((bottomLeftYCord+yLen-1, bottomLeftXCord+xLen-1,))
    # newPerim.remove(cord1)
    # newPerim.remove(cord2)
    # newPerim.remove(cord3)
    # newPerim.remove(cord4)
    val = len(newPerim)
    randVal = random.randrange(val)
    pointList.append(newPerim[randVal])
    return pointList

def genNodes(rectangles):
#    xLen, yLen, bottomLeftXCord, bottomLeftYCord = rect
    rectList = rectangles
    pointList = []
    for i in rectList:
        pointList = testPointGenerator(i, pointList)
    return (pointList)

def heuristic(a, b):
    #return (b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2
    ax, ay, bx, by = a[0], a[1], b[0], b[1]
    # if ax == 5:
    #     ax = 100000
    # if ay == 5:
    #     ay = 100000
    # if bx == 5:
    #     bx = 100000
    # if by == 5:
    #     by = 100000
    return 10 * (abs(ax-bx) + abs(ay-by))

def astar(array, start, goal):

    neighbors = [(0,1),(0,-1),(1,0),(-1,0)]

    close_set = set()
    came_from = {}
    gscore = {start:0}
    fscore = {start:heuristic(start, goal)}
    oheap = []

    heappush(oheap, (fscore[start], start))

    while oheap:

        current = heappop(oheap)[1]

        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = gscore[current] + heuristic(current, neighbor)
            if 0 <= neighbor[0] < array.shape[0]:
                if 0 <= neighbor[1] < array.shape[1]:
                    if array[neighbor[0]][neighbor[1]] == 3:
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue

            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue

            if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heappush(oheap, (fscore[neighbor], neighbor))

    return False

def astartest(array, start, goal):

    neighbors = [(0,1),(0,-1),(1,0),(-1,0)]

    close_set = set()
    came_from = {}
    gscore = {start:0}
    fscore = {start:heuristic(start, goal)}
    oheap = []

    heappush(oheap, (fscore[start], start))

    while oheap:

        current = heappop(oheap)[1]

        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = gscore[current] + heuristic(current, neighbor)
            if 0 <= neighbor[0] < array.shape[0]:
                if 0 <= neighbor[1] < array.shape[1]:
                    if array[neighbor[0]][neighbor[1]] == 5:
                        continue
                else:
                    # array bound y walls
                    continue
            else:
                # array bound x walls
                continue

            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue

            if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1]for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heappush(oheap, (fscore[neighbor], neighbor))

    return False


def genEntryExit(rectangles):
    #xLen, yLen, bottomLeftXCord, bottomLeftYCord = rect
    rectList = copy.deepcopy(rectangles)
    randOne = random.randrange(len(rectList))
    randListOne = range(0,randOne)
    randListTwo = range((randOne+1),len(rectList))
    randList = list(randListOne) + list(randListTwo)
    randTwo = random.choice(randList)
    rectOne = rectList[randOne]
    rectTwo = rectList[randTwo]
    xLenOne, yLenOne, bottomLeftXCordOne, bottomLeftYCordOne = rectOne
    xLenTwo, yLenTwo, bottomLeftXCordTwo, bottomLeftYCordTwo = rectTwo
    xLenOne = xLenOne-2
    yLenOne = yLenOne-2
    bottomLeftXCordOne = bottomLeftXCordOne + 1
    bottomLeftYCordOne = bottomLeftYCordOne + 1
    xLenTwo = xLenTwo-2
    yLenTwo = yLenTwo-2
    bottomLeftXCordTwo = bottomLeftXCordTwo + 1
    bottomLeftYCordTwo = bottomLeftYCordTwo + 1
    randPointOne = ((random.randrange(bottomLeftXCordOne,bottomLeftXCordOne+xLenOne+1)),(random.randrange(bottomLeftYCordOne,bottomLeftYCordOne+yLenOne+1)))
    randPointTwo = ((random.randrange(bottomLeftXCordTwo,bottomLeftXCordTwo+xLenTwo+1)),(random.randrange(bottomLeftYCordTwo,bottomLeftYCordTwo+yLenTwo+1)))
    return randPointOne,randPointTwo

def mainJunk(mazeSize, numberOfRectangles, rectangleSize):
    (newestMaze, rectangles) = generateMaze(mazeSize, numberOfRectangles, rectangleSize)
    points = genNodes(rectangles)
    enexpoints = genEntryExit(rectangles)
    # points.append(enexpoints[0])
    # points.append(enexpoints[1])

    for i in points:
        newestMaze[i[0]][i[1]] = '&'
    pathMaze = newestMaze[:]
    for i in range(len(pathMaze)):
        for j in range(len(pathMaze[0])):
            if pathMaze[i][j] == '█':
                pathMaze[i][j] = 0
            elif pathMaze[i][j] == '@':
                pathMaze[i][j] = 1
            elif pathMaze[i][j] == '=':
                pathMaze[i][j] = 3
            elif pathMaze[i][j] == '#':
                pathMaze[i][j] = 5
            elif pathMaze[i][j] == '&':
                pathMaze[i][j] = 9
    numparr = numpy.asarray(pathMaze)
    for i in range (0, len(points), 2):
        newlist = astar(numparr, points[i], points[i+1])
        for j in newlist:
            if numparr[j[0], j[1]] != 3 and numparr[j[0],j[1]] != 1:
                numparr[j[0], j[1]] = 9
    #numparr.tolist()
    for i in range(len(numparr)):
        for j in range(len(numparr[i])):
            numparr[i, j] = str(numparr[i, j])
    newparr = copy.deepcopy(numparr)
    newparr.tolist()
    for i in range (len(newparr)):
        for j in range (len(newparr[i])):
            checkPoints = [(0,1,),(0,-1,),(-1, 0,),(1,0,),(1,1,),(-1,-1,),(1,-1,),(-1,1)]
            if newparr[i][j] == 9:
                for k in checkPoints:
                    if newparr[i+k[0]][j+k[1]] == 0:
                        newparr[i+k[0]][j+k[1]] = 5
    checker = True
    while checker:
        enexpoints = genEntryExit(rectangles)
        x1,y1 = enexpoints[0]
        x2,y2 = enexpoints[1]
        if not(astartest(newparr, enexpoints[0], enexpoints[1])):
            checker = True
        else:
            checker = False
    if newparr[x1][y1] == 1:
        newparr[x1][y1]=6
    else:
        return mainJunk(mazeSize, numberOfRectangles, rectangleSize)
    if newparr[x2][y2] == 1:
        newparr[x2][y2]=7
    else:
        return mainJunk(mazeSize, numberOfRectangles, rectangleSize)
    #drawTurtle(newparr)
    return (newparr, rectangles)

def main(mazeSize, numberOfRectangles, rectangleSize):
    # mazeSize = int(input("Enter a number for the size of the maze:  "))
    # numberOfRectangles = int(input("Enter a number for the amount of rectangles to be in the maze:  "))
    # rectangleSize = int(input("Enter a number for the maximum size of the rectangles:   "))
    #mazeSize, numberOfRectangles, rectangleSize = 100, 100, 30
    return (mainJunk(mazeSize, numberOfRectangles, rectangleSize))
