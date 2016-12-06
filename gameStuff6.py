import MazeGenerator, pygame, sys, copy, npc, settingsscreen
pygame.init()
loading = pygame.image.load('loading600x600.png')
#loading = pygame.transform.scale(loading, (600, 600))
# dirt = pygame.image.load('dungeon_floor.png')
# playerHead = pygame.image.load('player.png')
# mobster = pygame.image.load('mob.png')

msize = 100
numrect = 9
rectsize = 15

lvl = 0

#startx, starty, endx, endy = 0, 0, 0, 0

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
    xLower = x-10
    yLower = y-10
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
    # for i in range(100):
    #     for j in range(100):
            if arr[i][j] == 9:
                # pygame.draw.rect(screen, (0,0,0), pygame.Rect(i*30, j*30, 30, 30))
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
            # else:
            #     florBlock = Flor(i,j)
            #     florBlock.add(floors)
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
    def __init__(self, i, j):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30,30])
        self.image.fill(self.daggerColor)
        self.pos = (i*30,j*30,)
        self.rect = pygame.Rect(i*30,j*30,30,30)
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
    def __init__(self, i, j):
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface([30,30])
        #self.image.fill(self.playerColor)
        self.image = pygame.image.load('player.png').convert_alpha()
        self.pos = (i*30,j*30,)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self._layer = 7
    def update(self, pos):
        #self.rect.topleft = (xCent*30,yCent*30,)
        self.rect.topleft = (pos)

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
    xDimen = int(msize*6)
    yDimen = int(msize*6)
    startx, starty, endx, endy = 0, 0, 0, 0
    startx, starty, endx, endy = startEndPoints(mazze)
    #screen = pygame.display.set_mode((xDimen, yDimen,))
    screen = pygame.display.set_mode((600,600,))
    # all_entities = pygame.sprite.Group()
    # walls = pygame.sprite.Group()
    # players = pygame.sprite.GroupSingle()
    # monstors = pygame.sprite.Group()
    # exit = pygame.sprite.GroupSingle()
    # floors = pygame.sprite.Group()
    # entry = pygame.sprite.GroupSingle()
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
        i.displayStats()

    clock = pygame.time.Clock()

    x = copy.deepcopy(startx)
    y = copy.deepcopy(starty)

    total_level_width = 3000
    total_level_height = 3000
    camera = Camera(complex_camera, total_level_width, total_level_height)
    playerOne = Player(x, y)
    playerOne.add(players)
    while not done:
            for event in pygame.event.get():
                    pressed = pygame.key.get_pressed()
                    if event.type == pygame.QUIT:
                        done = True
                    # if event.type == pygame.KEYDOWN:
            # playerOne = Player(x, y)
            # playerOne.add(players)
            pygameMazeDraw(screen, mazze, y, x, mobList, walls, monstors, exit, floors, entry)
            pressed = pygame.key.get_pressed()
#<<<<<<< HEAD
            if pressed[pygame.K_w] or pressed[pygame.K_s] or pressed[pygame.K_a] or pressed[pygame.K_d]:
                if pressed[pygame.K_w]:
                    testSprite = Player(x,(y-1))
                    if pygame.sprite.spritecollideany(testSprite, walls) is not None:
                        print('wcollide')
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
                        players.update(testSprite.pos)
                elif pressed[pygame.K_s]:
                    testSprite = Player(x,(y+1))
                    if pygame.sprite.spritecollideany(testSprite, walls) is not None:
                        print('scollide')
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
                        players.update(testSprite.pos)
                elif pressed[pygame.K_a]:
                    testSprite = Player((x-1),y)
                    if pygame.sprite.spritecollideany(testSprite, walls) is not None:
                        print('acollide')
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
                        players.update(testSprite.pos)
                elif pressed[pygame.K_d]:
                    testSprite = Player((x+1),y)
                    if pygame.sprite.spritecollideany(testSprite, walls) is not None:
                        print('dcollide')
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
                        players.update(testSprite.pos)
            (players.sprite).add(daggers)
            if pressed[pygame.K_UP] or pressed[pygame.K_DOWN] or pressed[pygame.K_LEFT] or pressed[pygame.K_RIGHT] or pressed[pygame.K_RSHIFT]:
                if pressed[pygame.K_UP] or pressed[pygame.K_RSHIFT]:
                    dagger = Dagger(x, y-1)
                    dagger.add(daggers)
                    pygame.sprite.groupcollide(daggers, walls, True, False)
                    #pygame.sprite.groupcollide(daggers, monstors, True, True)
                    if len(daggers.sprites()) > 0:
                        coll = pygame.sprite.spritecollideany(daggers.sprite, monstors)
                        if coll is not None:
                            mobList[coll.monst.listPos] = None
                        pygame.sprite.groupcollide(daggers, monstors, True, True)
                    # pygame.sprite.groupcollide(daggers, walls, True, False)
                    # pygame.sprite.groupcollide(daggers, monstors, True, True)
                elif pressed[pygame.K_DOWN]:
                    dagger = Dagger(x, y+1)
                    dagger.add(daggers)
                    pygame.sprite.groupcollide(daggers, walls, True, False)
                    #pygame.sprite.groupcollide(daggers, monstors, True, True)
                    if len(daggers.sprites()) > 0:
                        coll = pygame.sprite.spritecollideany(daggers.sprite, monstors)
                        if coll is not None:
                            mobList[coll.monst.listPos] = None
                        pygame.sprite.groupcollide(daggers, monstors, True, True)
                    # pygame.sprite.groupcollide(daggers, walls, True, False)
                    # pygame.sprite.groupcollide(daggers, monstors, True, True)
                elif pressed[pygame.K_LEFT]:
                    dagger = Dagger(x-1, y)
                    dagger.add(daggers)
                    pygame.sprite.groupcollide(daggers, walls, True, False)
                    #pygame.sprite.groupcollide(daggers, monstors, True, True)
                    if len(daggers.sprites()) > 0:
                        coll = pygame.sprite.spritecollideany(daggers.sprite, monstors)
                        if coll is not None:
                            mobList[coll.monst.listPos] = None
                        pygame.sprite.groupcollide(daggers, monstors, True, True)
                    # pygame.sprite.groupcollide(daggers, walls, True, False)
                    # pygame.sprite.groupcollide(daggers, monstors, True, True)
                elif pressed[pygame.K_RIGHT]:
                    dagger = Dagger(x+1, y)
                    dagger.add(daggers)
                    pygame.sprite.groupcollide(daggers, walls, True, False)
                    if len(daggers.sprites()) > 0:
                        coll = pygame.sprite.spritecollideany(daggers.sprite, monstors)
                        if coll is not None:
                            mobList[coll.monst.listPos] = None
                        pygame.sprite.groupcollide(daggers, monstors, True, True)
                    # pygame.sprite.groupcollide(daggers, walls, True, False)
                    # pygame.sprite.groupcollide(daggers, monstors, True, True)

# #=======
#             if pressed[pygame.K_w]:
#                 if screen.get_at((x*6,(y-1)*6,)) == (0,204,0):
#                     continue
#                 elif screen.get_at((x*6,(y-1)*6,)) == (255,51,255):
#                     screen.blit(loading, (0,0,))
#                     pygame.display.flip()
#                     return main()
#                 else:
#                     y -= 1
#             elif pressed[pygame.K_s]:
#                 if screen.get_at((x*6,(y+1)*6,)) == (0,204,0):
#                     continue
#                 elif screen.get_at((x*6,(y+1)*6,)) == (255,51,255):
#                     screen.blit(loading, (0,0,))
#                     pygame.display.flip()
#                     return main()
#                 else:
#                     y += 1
#             elif pressed[pygame.K_a]:
#                 if screen.get_at(((x-1)*6,y*6,)) == (0,204,0):
#                     continue
#                 elif screen.get_at(((x-1)*6,y*6,)) == (255,51,255):
#                     screen.blit(loading, (0,0,))
#                     pygame.display.flip()
#                     return main()
#                 else:
#                     x -= 1
#             elif pressed[pygame.K_d]:
#                 if screen.get_at(((x+1)*6,y*6,)) == (0,204,0):
#                     continue
#                 elif screen.get_at(((x+1)*6,y*6,)) == (255,51,255):
#                     screen.blit(loading, (0,0,))
#                     pygame.display.flip()
#                     return main()
#                 else:
#                     x += 1
            #opens up the settings screen but need a way to clear it
            if pressed[pygame.K_o]:
                settingsscreen.main()
#
#             pygame.draw.rect(screen,(255,70,255,),pygame.Rect(600,0,200,600))
#             pygameMazeDraw(screen, mazze, y, x, mobList)
#             #pygame.draw.rect(screen, (51, 255,255), pygame.Rect(x*6, y*6, 6, 6))
#             screen.blit(playerHead, (x*6,y*6,))
# >>>>>>> 086ff51dc81ab8af833d9828461fc3ce1c44e303

            #pygame.draw.rect(screen,(255,70,255,),pygame.Rect(600,0,200,600))
            # pygame.sprite.LayeredUpdates.move_to_front(sprite=players.sprite)
            # pygame.sprite.LayeredUpdates.move_to_front(sprite=entry.sprite)
            # pygame.sprite.LayeredUpdates.move_to_front(sprite=exit.sprite)
            # pygame.sprite.groupcollide(daggers, walls, True, False)
            # #pygame.sprite.groupcollide(daggers, monstors, True, True)
            # if pygame.sprite.spritecollideany(daggers.sprite, monstors) is not None:
            #     monstors.remove(pygame.sprite.spritecollideany(daggers.sprite, monstors))
                # all_entities.remove(pygame.sprite.spritecollideany(daggers.sprite, monstors))
            all_entities.add(walls)
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

            #pygameMazeDraw(screen, mazze, y, x, mobList)
            #pygame.draw.rect(screen, (51, 255,255), pygame.Rect(x*6, y*6, 6, 6))
            #screen.blit(playerHead, (x*6,y*6,))
            # rectss = all_entities.draw(screen)
            # pygame.display.update(rectss)
            screen.convert_alpha()
            pygame.display.flip()
            all_entities.empty()
            walls.empty()
            floors.empty()
            entry.empty()
            exit.empty()
            daggers.empty()


            clock.tick(30)
            screen.fill((0,0,0,))

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
