import MazeGenerator, pygame, sys, copy, npc
pygame.init()
loading = pygame.image.load('loadingTeach.png')
loading = pygame.transform.scale(loading, (600, 600))
dirt = pygame.image.load('dirt.bmp')
playerHead = pygame.image.load('playerhead.png')

msize = 100
numrect = 9
rectsize = 15

lvl = 0

#startx, starty, endx, endy = 0, 0, 0, 0

def startEndPoints(mazz):
    for i in range (len(mazz)):
        for j in range (len(mazz[i])):
            if mazz[i][j] == 6:
                startx = i
                starty = j
            elif mazz[i][j] == 7:
                endx = i
                endy = j
    return startx, starty, endx, endy


def pygameMazeDraw (screen, arr, x, y, mobList):
    xLower = x-10
    yLower = y-10
    xUpper = x+11
    yUpper = y+11
    if xLower <= 0:
        xLower = 0
    if yLower <= 0:
        yLower = 0
    if xUpper >= len(arr):
        xUpper = len(arr)
    if yUpper >= len(arr[0]):
        yUpper = len(arr[0])
    for i in range((yLower), (yUpper), 1):
        for j in range((xLower), (xUpper), 1):
            if arr[i][j] == 0:
                pygame.draw.rect(screen, (0,0,0), pygame.Rect(i*6, j*6, 6, 6))
            elif arr[i][j] == 5:
                pygame.draw.rect(screen, (0,204,0), pygame.Rect(i*6, j*6, 6, 6))
            elif arr[i][j] == 1:
                pygame.draw.rect(screen, (102,51,0), pygame.Rect(i*6, j*6, 6, 6))
                #screen.blit(dirt, (i*6,j*6,))
            elif arr[i][j] == 6:
                pygame.draw.rect(screen, (255,255,0), pygame.Rect(i*6, j*6, 6, 6))
            elif arr[i][j] == 7:
                pygame.draw.rect(screen, (255,51,255), pygame.Rect(i*6, j*6, 6, 6))
            else:
                pygame.draw.rect(screen, (102,51,0), pygame.Rect(i*6, j*6, 6, 6))
                #screen.blit(dirt, (i*6,j*6,))
    mobDraw(screen, mobList, xLower, xUpper, yLower, yUpper)

def mobDraw(screen, mobList, xLower, xUpper, yLower, yUpper):
    for i in mobList:
        if (i.startX >= xLower and i.startX < xUpper) and (i.startY >= yLower and i.startY < yUpper):
            pygame.draw.rect(screen, (255,0,0,), pygame.Rect(i.startY*6,i.startX*6,6,6))

def runMaze(mazze, rectangles):
    global lvl
    xDimen = int(msize*6)
    yDimen = int(msize*6)
    startx, starty, endx, endy = 0, 0, 0, 0
    startx, starty, endx, endy = startEndPoints(mazze)
    #screen = pygame.display.set_mode((xDimen, yDimen,))
    screen = pygame.display.set_mode((800,600,))
    done = False

    mobList = npc.main(rectangles, lvl)
    for i in mobList:
        i.displayStats()

    clock = pygame.time.Clock()

    x = copy.deepcopy(startx)
    y = copy.deepcopy(starty)
    while not done:
            for event in pygame.event.get():
                    pressed = pygame.key.get_pressed()
                    if event.type == pygame.QUIT:
                        done = True
                    # if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_w]:
                if screen.get_at((x*6,(y-1)*6,)) == (0,204,0):
                    continue
                elif screen.get_at((x*6,(y-1)*6,)) == (255,51,255):
                    screen.blit(loading, (0,0,))
                    pygame.display.flip()
                    return main()
                else:
                    y -= 1
            elif pressed[pygame.K_s]:
                if screen.get_at((x*6,(y+1)*6,)) == (0,204,0):
                    continue
                elif screen.get_at((x*6,(y+1)*6,)) == (255,51,255):
                    screen.blit(loading, (0,0,))
                    pygame.display.flip()
                    return main()
                else:
                    y += 1
            elif pressed[pygame.K_a]:
                if screen.get_at(((x-1)*6,y*6,)) == (0,204,0):
                    continue
                elif screen.get_at(((x-1)*6,y*6,)) == (255,51,255):
                    screen.blit(loading, (0,0,))
                    pygame.display.flip()
                    return main()
                else:
                    x -= 1
            elif pressed[pygame.K_d]:
                if screen.get_at(((x+1)*6,y*6,)) == (0,204,0):
                    continue
                elif screen.get_at(((x+1)*6,y*6,)) == (255,51,255):
                    screen.blit(loading, (0,0,))
                    pygame.display.flip()
                    return main()
                else:
                    x += 1

            pygame.draw.rect(screen,(255,70,255,),pygame.Rect(600,0,200,600))
            pygameMazeDraw(screen, mazze, y, x, mobList)
            #pygame.draw.rect(screen, (51, 255,255), pygame.Rect(x*6, y*6, 6, 6))
            screen.blit(playerHead, (x*6,y*6,))

            pygame.display.flip()
            clock.tick(20)

def main():
    global numrect
    global rectsize
    rectsize += 4
    numrect += 5
    print("rectsize:\t" + str(rectsize))
    print("numrect:\t" + str(numrect))
    maze, rectangles = MazeGenerator.main(msize, numrect, rectsize)
    global lvl
    print(str(lvl))
    lvl += 1
    runMaze(maze, rectangles)
