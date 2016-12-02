import MazeGenerator, pygame, sys, copy
pygame.init()
loading = pygame.image.load('loading.png')
dirt = pygame.image.load('dirt.bmp')
dirt25 = pygame.image.load('dirt25.bmp')
wall = pygame.image.load('wall.bmp')
playerGif = pygame.image.load('playerGif.gif')
playerimg = pygame.image.load('playerimg.png')


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


def pygameMazeDraw (screen, arr, y, x, walls):
    #newArr = [[]]
    newArr = [[0 for i in range(20)] for j in range (20)]
    xLower = x-10
    yLower = y-10
    xUpper = x+10
    yUpper = y+10
    if xLower <= 0:
        xLower = 0
        xUpper = xLower + 20
    if yLower <= 0:
        yLower = 0
        yUpper = yLower + 20
    if xUpper >= len(arr)-1:
        xUpper = len(arr)-1
        xLower = xUpper - 20
    if yUpper >= len(arr[0])-1:
        yUpper = len(arr[0])-1
        yLower = yUpper-20
    #p = 0
    #q = 0
    for i in range(20):
        for j in range(20):
            newArr[i][j] = arr[xLower+i][yLower+j]
    # for i in range((yLower), (yUpper), 1):
    #     for j in range((xLower), (xUpper), 1):
    #         newArr[p][q] = (arr[i][j])
    #         q += 1
    #     p += 1
    #     q = 0
    for i in range(20):
        for j in range(20):
            if newArr[i][j] == 0:
                pygame.draw.rect(screen, (0,0,0), pygame.Rect(i*25, j*25, 25, 25))
            elif newArr[i][j] == 5:
                #pygame.draw.rect(screen, (0,204,0), pygame.Rect(i*25, j*25, 25, 25))
                wallBlock = Wal(i,j)
                wallBlock.add(walls)
                #screen.blit(wall, (i*5,j*5,))
            elif newArr[i][j] == 1:
                pygame.draw.rect(screen, (102,51,0), pygame.Rect(i*25, j*25, 25, 25))
                #screen.blit(dirt25, (i*25,j*25,))
            elif newArr[i][j] == 6:
                pygame.draw.rect(screen, (255,255,0), pygame.Rect(i*25, j*25, 25, 25))
            elif newArr[i][j] == 7:
                pygame.draw.rect(screen, (255,51,255), pygame.Rect(i*25, j*25, 25, 25))
            else:
                pygame.draw.rect(screen, (102,51,0), pygame.Rect(i*25, j*25, 25, 25))
                #screen.blit(dirt25, (i*25,j*25,))
    # for i in range((yLower), (yUpper), 1):
    #     for j in range((xLower), (xUpper), 1):
    #         if arr[i][j] == 0:
    #             pygame.draw.rect(screen, (0,0,0), pygame.Rect(i*5, j*5, 5, 5))
    #         welif arr[i][j] == 5:
    #             pygame.draw.rect(screen, (0,204,0), pygame.Rect(i*5, j*5, 5, 5))
    #             #screen.blit(wall, (i*5,j*5,))
    #         elif arr[i][j] == 1:
    #             #pygame.draw.rect(screen, (102,51,0), pygame.Rect(i*5, j*5, 5, 5))
    #             screen.blit(dirt, (i*5,j*5,))
    #         elif arr[i][j] == 6:
    #             pygame.draw.rect(screen, (255,255,0), pygame.Rect(i*5, j*5, 5, 5))
    #         elif arr[i][j] == 7:
    #             pygame.draw.rect(screen, (255,51,255), pygame.Rect(i*5, j*5, 5, 5))
    #         else:
    #             #pygame.draw.rect(screen, (102,51,0), pygame.Rect(i*5, j*5, 5, 5))
    #             screen.blit(dirt, (i*5,j*5,))

class Wal (pygame.sprite.Sprite):
    wallColor = (0,204,0,)
    def __init__(self, i, j):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([25,25])
        self.image.fill(self.wallColor)
        self.pos = (i*5,j*5,)
        self.rect = pygame.Rect(i*25,j*25,25,25)

class Player (pygame.sprite.Sprite):
    playerColor = (51,255,255,)
    def __init__(self, i, j):
        pygame.sprite.Sprite.__init__(self)
        self.image = playerimg.convert_alpha()
        #self.image.fill(self.playerColor)
        self.pos = (i*5,j*5,)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
    def update(self, xCent, yCent):
        self.rect.topleft = (xCent*5,yCent*5,)



def runMaze(mazze):
    xDimen = int(msize*5)
    yDimen = int(msize*5)
    startx, starty, endx, endy = 0, 0, 0, 0
    startx, starty, endx, endy = startEndPoints(mazze)
    screen = pygame.display.set_mode((xDimen, yDimen,))
    walls = pygame.sprite.Group()
    players = pygame.sprite.Group()
    #screen.convert()
    #screen = pygame.display.set_mode((100,100,))
    done = False

    clock = pygame.time.Clock()

    x = copy.deepcopy(startx)
    y = copy.deepcopy(starty)
    #xCent = copy.deepcopy(x)
    #yCent = copy.deepcopy(y)
    yCent = 50
    xCent = 50
    playerOne = Player(xCent, yCent)
    playerOne.add(players)
    while not done:
            for event in pygame.event.get():
                    pressed = pygame.key.get_pressed()
                    if event.type == pygame.QUIT:
                        done = True
                    # if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_w]:
                if yCent-1 >=0:
                    if screen.get_at((xCent*5,(yCent-1)*5,)) == (0,204,0):
                        #continue
                        xCent = xCent
                        yCent = yCent
                    elif screen.get_at((xCent*5,(yCent-1)*5,)) == (255,51,255):
                        screen.blit(loading, (0,0,))
                        pygame.display.flip()
                        return runMaze(MazeGenerator.main(msize, numrect, rectsize))
                    else:
                        if (yCent - 1) <= 0:
                            yCent = 0
                            players.update(xCent,yCent)
                        else:
                            yCent -= 1
                            players.update(xCent,yCent)
                else:
                    continue
            elif pressed[pygame.K_s]:
                if yCent+1 <= 99:
                    if screen.get_at((xCent*5,(yCent+1)*5,)) == (0,204,0):
                        #continue
                        xCent = xCent
                        yCent = yCent
                    elif screen.get_at((xCent*5,(yCent+1)*5,)) == (255,51,255):
                        screen.blit(loading, (0,0,))
                        pygame.display.flip()
                        return runMaze(MazeGenerator.main(msize, numrect, rectsize))
                    else:
                        if (yCent + 1) >= 99:
                            yCent = 99
                            players.update(xCent,yCent)
                        else:
                            yCent += 1
                            players.update(xCent,yCent)
                else:
                    continue
            elif pressed[pygame.K_a]:
                if xCent-1 >= 0:
                    if screen.get_at(((xCent-1)*5,yCent*5,)) == (0,204,0):
                        #continue
                        xCent = xCent
                        yCent = yCent
                    elif screen.get_at(((xCent-1)*5,yCent*5,)) == (255,51,255):
                        screen.blit(loading, (0,0,))
                        pygame.display.flip()
                        return runMaze(MazeGenerator.main(msize, numrect, rectsize))
                    else:
                        if (xCent-1) <= 0:
                            xCent = 0
                            players.update(xCent,yCent)
                        else:
                            xCent -= 1
                            players.update(xCent,yCent)
                else:
                    continue
            elif pressed[pygame.K_d]:
                if xCent+1 <= 99:
                    if screen.get_at(((xCent+1)*5,yCent*5,)) == (0,204,0):
                        #continue
                        xCent = xCent
                        yCent = yCent
                    elif screen.get_at(((xCent+1)*5,yCent*5,)) == (255,51,255):
                        screen.blit(loading, (0,0,))
                        pygame.display.flip()
                        return runMaze(MazeGenerator.main(msize, numrect, rectsize))
                    else:
                        if (xCent +1) >= 99:
                            xCent = 99
                            players.update(xCent,yCent)
                        else:
                            xCent += 1
                            players.update(xCent,yCent)
                else:
                    continue


            #pygameMazeDraw(screen, mazze, yCent, xCent)
            pygameMazeDraw(screen, mazze, yCent, xCent, walls)
            walls.draw(screen)
            players.draw(screen)
            #pygame.draw.rect(screen, (51, 255,255), pygame.Rect(xCent*5, yCent*5, 25, 25))

            pygame.display.flip()
            #walls.clear(screen, (0,0,0,))
            walls.empty()
            players.empty()
            clock.tick(20)
runMaze(MazeGenerator.main(msize, numrect, rectsize))
