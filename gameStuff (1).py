import MazeGenerator, pygame, sys, copy
pygame.init()
loading = pygame.image.load('loading.png')
dirt = pygame.image.load('dirt.bmp')

msize = 100
numrect = msize
rectsize = 30



startx, starty, endx, endy = 0, 0, 0, 0

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

def pygameMiniMazeDraw (screen, arr, x, y):
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
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 0:
                pygame.draw.rect(screen, (0,0,0), pygame.Rect(i, j, 1, 1))
            elif arr[i][j] == 5:
                pygame.draw.rect(screen, (0,204,0), pygame.Rect(i, j, 1, 1))
            elif arr[i][j] == 1:
                pygame.draw.rect(screen, (102,51,0), pygame.Rect(i, j, 1, 1))
                #screen.blit(dirt, (i*5,j*5,))
            elif arr[i][j] == 6:
                pygame.draw.rect(screen, (255,255,0), pygame.Rect(i, j, 1, 1))
            elif arr[i][j] == 7:
                pygame.draw.rect(screen, (255,51,255), pygame.Rect(i, j, 1, 1))
            else:
                pygame.draw.rect(screen, (102,51,0), pygame.Rect(i, j, 1, 1))
                #screen.blit(dirt, (i*5,j*5,))


def pygameMazeDraw (screen, arr, x, y):
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
                pygame.draw.rect(screen, (0,0,0), pygame.Rect(i*5, j*5, 5, 5))
            elif arr[i][j] == 5:
                pygame.draw.rect(screen, (0,204,0), pygame.Rect(i*5, j*5, 5, 5))
            elif arr[i][j] == 1:
                #pygame.draw.rect(screen, (102,51,0), pygame.Rect(i*5, j*5, 5, 5))
                screen.blit(dirt, (i*5,j*5,))
            elif arr[i][j] == 6:
                pygame.draw.rect(screen, (255,255,0), pygame.Rect(i*5, j*5, 5, 5))
            elif arr[i][j] == 7:
                pygame.draw.rect(screen, (255,51,255), pygame.Rect(i*5, j*5, 5, 5))
            else:
                #pygame.draw.rect(screen, (102,51,0), pygame.Rect(i*5, j*5, 5, 5))
                screen.blit(dirt, (i*5,j*5,))

def runMaze(mazze):
    xDimen = int(msize*5)
    yDimen = int(msize*5)
    startx, starty, endx, endy = 0, 0, 0, 0
    startx, starty, endx, endy = startEndPoints(mazze)
    #screen = pygame.display.set_mode((xDimen, yDimen,))
    screen = pygame.display.set_mode((800,600,))
    done = False

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
                if screen.get_at((x*5,(y-1)*5,)) == (0,204,0):
                    continue
                elif screen.get_at((x*5,(y-1)*5,)) == (255,51,255):
                    screen.blit(loading, (0,0,))
                    pygame.display.flip()
                    return runMaze(MazeGenerator.main(msize, numrect, rectsize))
                else:
                    y -= 1
            elif pressed[pygame.K_s]:
                if screen.get_at((x*5,(y+1)*5,)) == (0,204,0):
                    continue
                elif screen.get_at((x*5,(y+1)*5,)) == (255,51,255):
                    screen.blit(loading, (0,0,))
                    pygame.display.flip()
                    return runMaze(MazeGenerator.main(msize, numrect, rectsize))
                else:
                    y += 1
            elif pressed[pygame.K_a]:
                if screen.get_at(((x-1)*5,y*5,)) == (0,204,0):
                    continue
                elif screen.get_at(((x-1)*5,y*5,)) == (255,51,255):
                    screen.blit(loading, (0,0,))
                    pygame.display.flip()
                    return runMaze(MazeGenerator.main(msize, numrect, rectsize))
                else:
                    x -= 1
            elif pressed[pygame.K_d]:
                if screen.get_at(((x+1)*5,y*5,)) == (0,204,0):
                    continue
                elif screen.get_at(((x+1)*5,y*5,)) == (255,51,255):
                    screen.blit(loading, (0,0,))
                    pygame.display.flip()
                    return runMaze(MazeGenerator.main(msize, numrect, rectsize))
                else:
                    x += 1

            pygame.draw.rect(screen,(255,255,255,),pygame.Rect(0,500,800,100))
            pygame.draw.rect(screen,(255,255,255,),pygame.Rect(500,0,300,600))
            pygameMazeDraw(screen, mazze, y, x)
            pygame.draw.rect(screen, (51, 255,255), pygame.Rect(x*5, y*5, 5, 5))

            pygame.display.flip()
            clock.tick(20)

def main():
    runMaze(MazeGenerator.main(msize, numrect, rectsize))
