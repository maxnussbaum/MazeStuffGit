import MazeGenerator, pygame, sys, copy, npc, settingsscreen, highScores
pygame.init()
loading = pygame.image.load('loading600x600.png').convert_alpha()


msize = 100
numrect = 9
rectsize = 15

lvl = 0
mobsKilled = 0
facing = 'right'

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


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


def pygameMazeDraw (screen, arr, x, y, mobList, walls, monstors, exit, floors, entry):
    xLower = x-11
    yLower = y-11
    xUpper = x+11
    yUpper = y+11
    if xLower <= 0:
        xLower = 0
        xUpper = 21
    if yLower <= 0:
        yLower = 0
        yUpper = 21
    if xUpper >= len(arr):
        xUpper = len(arr)
        xLower = len(arr)-21
    if yUpper >= len(arr[0]):
        yUpper = len(arr[0])
        yLower = len(arr[0])-21
    for i in range((yLower), (yUpper), 1):
        for j in range((xLower), (xUpper), 1):
            if arr[i][j] == 9:
                florBlock = Flor(i,j)
                florBlock.add(floors)
            elif arr[i][j] == 5:
                wallBlock = Wal(i,j)
                wallBlock.add(walls)
            elif arr[i][j] == 1:
                florBlock = Flor(i,j)
                florBlock.add(floors)
            elif arr[i][j] == 6:
                entryBlock = Entry(i,j)
                entryBlock.add(entry)
            elif arr[i][j] == 7:
                exitBlock = Exit(i,j)
                exitBlock.add(exit)

    mobDraw(mobList, monstors)

def mobDraw(mobList, monstors):
    for i in mobList:
        if i is None:
            continue
        else:
            monstar = Monsters(i.startY,i.startX,i)
            monstar.add(monstors)

class Monsters (pygame.sprite.Sprite):
    monsterColor = (255,0,0,)
    def __init__(self, i, j, monsterObj):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface([30,30])
        self.image = pygame.image.load('mob.png').convert_alpha()
        #self.image.fill(self.monsterColor)
        self.pos = (i*30,j*30,)
        self.rect = self.image.get_rect()
        self.monst = monsterObj
        self.rect.topleft = self.pos
        self._layer = 3
    def update (self, pos):
        self.rect.topleft = (pos)

class Entry (pygame.sprite.Sprite):
    entryColor = (255,255,0,)
    def __init__(self, i, j):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30,30])
        self.image.fill(self.entryColor)
        self.pos = (i*30,j*30,)
        self.rect = pygame.Rect(i*30,j*30,30,30)
        self._layer = 4

class Dagger (pygame.sprite.Sprite):
    daggerColor = (100,200,100,)
    def __init__(self, i, j, direction):
        pygame.sprite.Sprite.__init__(self)
        global facing
        if direction == 'left':
            self.image = pygame.image.load('sordLeft.png').convert_alpha()
            self.pos = (i*30,j*30,)
            self.rect = pygame.Rect(i*30,j*30,60,30)
            facing = 'left'
        elif direction == 'right':
            self.image = pygame.image.load('sordRight.png').convert_alpha()
            self.pos = ((i-1)*30,j*30,)
            self.rect = pygame.Rect((i-1)*30,j*30,60,30)
            facing = 'right'

        elif direction == 'up' and facing == 'right':
            self.image = pygame.image.load('sordUpRight.png').convert_alpha()
            self.pos = (i*30,j*30,)
            self.rect = pygame.Rect(i*30,j*30,30,60)
        elif direction == 'up' and facing == 'left':
            self.image = pygame.image.load('sordUpLeft.png').convert_alpha()
            self.pos = (i*30,j*30,)
            self.rect = pygame.Rect(i*30,j*30,30,60)
        elif direction == 'down' and facing == 'left':
            self.image = pygame.image.load('sordDownLeft.png').convert_alpha()
            self.pos = (i*30,(j-1)*30,)
            self.rect = pygame.Rect(i*30,(j-1)*30,30,60)
        elif direction == 'down' and facing == 'right':
            self.image = pygame.image.load('sordDownRight.png').convert_alpha()
            self.pos = (i*30,(j-1)*30,)
            self.rect = pygame.Rect(i*30,(j-1)*30,30,60)
        #self.image = pygame.Surface([30,30])
        #self.image.fill(self.daggerColor)
        #self.pos = (i*30,j*30,)
        #self.rect = pygame.Rect(i*30,j*30,30,30)
        self._layer = 9
    def update(self, pos):
        self.rect.topleft = (pos)

class Exit (pygame.sprite.Sprite):
    exitColor = (255,51,255,)
    def __init__(self, i, j):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30,30])
        self.image.fill(self.exitColor)
        self.pos = (i*30,j*30,)
        self.rect = pygame.Rect(i*30,j*30,30,30)
        self._layer = 4

class Flor (pygame.sprite.Sprite):
    floorColor = (102,51,0,)
    def __init__(self, i, j):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface([30,30])
        #self.image.fill(self.floorColor)
        self.image = pygame.image.load('dungeon_floor.png').convert_alpha()
        self.pos = (i*30,j*30,)
        self.rect = pygame.Rect(i*30, j*30, 30, 30)
        self._layer = 2

class Wal (pygame.sprite.Sprite):
    wallColor = (0,204,0,)
    def __init__(self, i, j):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface([30,30])
        #self.image.fill(self.wallColor)
        self.image = pygame.image.load('stone_wall.png').convert_alpha()
        self.pos = (i*30,j*30,)
        self.rect = pygame.Rect(i*30,j*30,30,30)
        self._layer = 2

class Player (pygame.sprite.Sprite):
    playerColor = (51,255,255,)
    def __init__(self, i, j, direction):
        pygame.sprite.Sprite.__init__(self)
        global facing
        #self.image = pygame.Surface([30,30])
        #self.image.fill(self.playerColor)
        if direction == 'left':
            self.image = pygame.image.load('mainplayerleft.png').convert_alpha()
            facing = 'left'
        elif direction == 'right':
            self.image = pygame.image.load('mainplayerright.png').convert_alpha()
            facing = 'right'
        self.pos = (i*30,j*30,)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self._layer = 7
    def update(self, pos, direction):
        #self.rect.topleft = (xCent*30,yCent*30,)
        self.rect.topleft = (pos)
        if direction == 'left':
            self.image = pygame.image.load('mainplayerleft.png').convert_alpha()
            facing = 'left'
        elif direction == 'right':
            self.image = pygame.image.load('mainplayerright.png').convert_alpha()
            facing = 'right'

def simple_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    return pygame.Rect(-l+300, -t+300, w, h)

def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l+300, -t+300, w, h

    l = min(0, l)
    l = max(-(camera.width-600), l)
    t = max(-(camera.height-600), t)
    t = min(0, t)

    return pygame.Rect(l, t, w, h)

def runMaze(mazze, rectangles):
    global lvl
    global mobsKilled
    xDimen = int(msize*6)
    yDimen = int(msize*6)
    startx, starty, endx, endy = 0, 0, 0, 0
    startx, starty, endx, endy = startEndPoints(mazze)
    #screen = pygame.display.set_mode((xDimen, yDimen,))
    screen = pygame.display.set_mode((600,600,))
    all_entities = pygame.sprite.LayeredUpdates()
    walls = pygame.sprite.LayeredUpdates()
    players = pygame.sprite.GroupSingle()
    monstors = pygame.sprite.LayeredUpdates()
    exit = pygame.sprite.GroupSingle()
    floors = pygame.sprite.LayeredUpdates()
    entry = pygame.sprite.GroupSingle()
    daggers = pygame.sprite.GroupSingle()
    done = False

    mobList = npc.main(rectangles, lvl)
    mobCounter = 0
    for i in mobList:
        i.setListPos(mobCounter)
        mobCounter += 1
        # i.displayStats()

    clock = pygame.time.Clock()

    x = copy.deepcopy(startx)
    y = copy.deepcopy(starty)

    total_level_width = 3000
    total_level_height = 3000
    global facing
    camera = Camera(complex_camera, total_level_width, total_level_height)
    playerOne = Player(x, y, facing)
    playerOne.add(players)
    while not done:
            for event in pygame.event.get():
                    pressed = pygame.key.get_pressed()
                    if event.type == pygame.QUIT:
                        done = True
                        print("You Killed " + str(mobsKilled) + " Monsters.")
                        highScores.setHighScore( lvl-1, mobsKilled)
            pygameMazeDraw(screen, mazze, y, x, mobList, walls, monstors, exit, floors, entry)
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_w] or pressed[pygame.K_s] or pressed[pygame.K_a] or pressed[pygame.K_d]:
                if pressed[pygame.K_w]:
                    testSprite = Player(x,(y-1), facing)
                    if pygame.sprite.spritecollideany(testSprite, walls) is not None:
                        # print('wcollide')
                        continue
                    elif pygame.sprite.spritecollideany(testSprite, exit) is not None:
                        screen.blit(loading, (0,0,))
                        pygame.display.flip()
                        return main()
                    # elif len(pygame.sprite.spritecollide(testSprite, monstors, dokill=True)) > 0:
                    #     print('monstCollide')
                    #     y -= 1
                    #     #testSprite.add(players)
                    #     players.update(testSprite.pos)
                    else:
                        y -= 1
                        #testSprite.add(players)
                        players.update(testSprite.pos, facing)
                elif pressed[pygame.K_s]:
                    testSprite = Player(x,(y+1), facing)
                    if pygame.sprite.spritecollideany(testSprite, walls) is not None:
                        # print('scollide')
                        continue
                    elif pygame.sprite.spritecollideany(testSprite, exit) is not None:
                        screen.blit(loading, (0,0,))
                        pygame.display.flip()
                        return main()
                    # elif len(pygame.sprite.spritecollide(testSprite, monstors, dokill=True)) > 0:
                    #     print('monstCollide')
                    #     y += 1
                    #     #testSprite.add(players)
                    #     players.update(testSprite.pos)
                    else:
                        y += 1
                        #testSprite.add(players)
                        players.update(testSprite.pos, facing)
                elif pressed[pygame.K_a]:
                    testSprite = Player((x-1),y, 'left')
                    if pygame.sprite.spritecollideany(testSprite, walls) is not None:
                        # print('acollide')
                        continue
                    elif pygame.sprite.spritecollideany(testSprite, exit) is not None:
                        screen.blit(loading, (0,0,))
                        pygame.display.flip()
                        return main()
                    # elif len(pygame.sprite.spritecollide(testSprite, monstors, dokill=True)) > 0:
                    #     print('monstCollide')
                    #     x -= 1
                    #     #testSprite.add(players)
                    #     players.update(testSprite.pos)
                    else:
                        x -= 1
                        #testSprite.add(players)
                        players.update(testSprite.pos, 'left')
                elif pressed[pygame.K_d]:
                    testSprite = Player((x+1),y, 'right')
                    if pygame.sprite.spritecollideany(testSprite, walls) is not None:
                        # print('dcollide')
                        continue
                    elif pygame.sprite.spritecollideany(testSprite, exit) is not None:
                        screen.blit(loading, (0,0,))
                        pygame.display.flip()
                        return main()
                    # elif len(pygame.sprite.spritecollide(testSprite, monstors, dokill=True)) > 0:
                    #     print('monstCollide')
                    #     x += 1
                    #     #testSprite.add(players)
                    #     players.update(testSprite.pos)
                    else:
                        x += 1
                        #testSprite.add(players)
                        players.update(testSprite.pos, 'right')
            (players.sprite).add(daggers)
            if pressed[pygame.K_UP] or pressed[pygame.K_DOWN] or pressed[pygame.K_LEFT] or pressed[pygame.K_RIGHT] or pressed[pygame.K_RSHIFT]:
                if pressed[pygame.K_UP] or pressed[pygame.K_RSHIFT]:
                    dagger = Dagger(x, y-1, 'up')
                    dagger.add(daggers)
                    pygame.sprite.groupcollide(daggers, walls, True, False)
                    #pygame.sprite.groupcollide(daggers, monstors, True, True)
                    if len(daggers.sprites()) > 0:
                        coll = pygame.sprite.spritecollideany(daggers.sprite, monstors)
                        if coll is not None:
                            mobList[coll.monst.listPos] = None
                            mobsKilled += 1
                            pygame.display.set_caption("Dungeon Crawlers" + "         " + "Monsters Killed:   " + str(mobsKilled) + "         Current Floor:   " + str(lvl))
                        pygame.sprite.groupcollide(daggers, monstors, False, True)
                    # pygame.sprite.groupcollide(daggers, walls, True, False)
                    # pygame.sprite.groupcollide(daggers, monstors, True, True)
                elif pressed[pygame.K_DOWN]:
                    dagger = Dagger(x, y+1, 'down')
                    dagger.add(daggers)
                    pygame.sprite.groupcollide(daggers, walls, True, False)
                    #pygame.sprite.groupcollide(daggers, monstors, True, True)
                    if len(daggers.sprites()) > 0:
                        coll = pygame.sprite.spritecollideany(daggers.sprite, monstors)
                        if coll is not None:
                            mobList[coll.monst.listPos] = None
                            mobsKilled += 1
                            pygame.display.set_caption("Dungeon Crawlers" + "         " + "Monsters Killed:   " + str(mobsKilled) + "         Current Floor:   " + str(lvl))
                        pygame.sprite.groupcollide(daggers, monstors, False, True)
                    # pygame.sprite.groupcollide(daggers, walls, True, False)
                    # pygame.sprite.groupcollide(daggers, monstors, True, True)
                elif pressed[pygame.K_LEFT]:
                    dagger = Dagger(x-1, y, 'left')
                    dagger.add(daggers)
                    pygame.sprite.groupcollide(daggers, walls, True, False)
                    #pygame.sprite.groupcollide(daggers, monstors, True, True)
                    if len(daggers.sprites()) > 0:
                        coll = pygame.sprite.spritecollideany(daggers.sprite, monstors)
                        if coll is not None:
                            mobList[coll.monst.listPos] = None
                            mobsKilled += 1
                            pygame.display.set_caption("Dungeon Crawlers" + "         " + "Monsters Killed:   " + str(mobsKilled) + "         Current Floor:   " + str(lvl))
                        pygame.sprite.groupcollide(daggers, monstors, False, True)
                    # pygame.sprite.groupcollide(daggers, walls, True, False)
                    # pygame.sprite.groupcollide(daggers, monstors, True, True)
                elif pressed[pygame.K_RIGHT]:
                    dagger = Dagger(x+1, y, 'right')
                    dagger.add(daggers)
                    pygame.sprite.groupcollide(daggers, walls, True, False)
                    if len(daggers.sprites()) > 0:
                        coll = pygame.sprite.spritecollideany(daggers.sprite, monstors)
                        if coll is not None:
                            mobList[coll.monst.listPos] = None
                            mobsKilled += 1
                            pygame.display.set_caption("Dungeon Crawlers" + "         " + "Monsters Killed:   " + str(mobsKilled) + "         Current Floor:   " + str(lvl))
                        pygame.sprite.groupcollide(daggers, monstors, False, True)
                    # pygame.sprite.groupcollide(daggers, walls, True, False)
                    # pygame.sprite.groupcollide(daggers, monstors, True, True)

            #opens up the settings screen but need a way to clear it
            if pressed[pygame.K_o]:
                done = settingsscreen.main()
                # if done==True:
                #     print("You Killed " + str(mobsKilled) + " Monsters.")
                #     highScores.setHighScore( lvl-1, mobsKilled)

            all_entities.add(walls)
            if daggers.sprite is None:
                all_entities.add(players)
            all_entities.add(daggers)
            all_entities.add(monstors)
            all_entities.add(exit)
            all_entities.add(floors)
            all_entities.add(entry)
            camera.update(players.sprite)
            #all_entities.draw(screen)
            for e in all_entities:
                screen.blit(e.image, camera.apply(e))

            screen.convert_alpha()
            pygame.display.flip()
            all_entities.empty()
            walls.empty()
            floors.empty()


            clock.tick(100)
            screen.fill((0,0,0,))
        #I don't know where to put this that it would work
    # print("You Killed " + str(mobsKilled) + " Monsters.")
    # highScores.setHighScore( lvl-1, mobsKilled)

def main():
    global numrect
    global rectsize
    rectsize += 1
    numrect += 2
    # print("rectsize:\t" + str(rectsize))
    # print("numrect:\t" + str(numrect))
    maze, rectangles = MazeGenerator.main(msize, numrect, rectsize)
    global lvl
    # print(str(lvl))
    lvl += 1
    pygame.display.set_caption("Dungeon Crawlers" + "         " + "Monsters Killed:   " + str(mobsKilled) + "         Current Floor:   " + str(lvl))
    runMaze(maze, rectangles)
