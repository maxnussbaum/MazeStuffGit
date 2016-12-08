import MazeGenerator, pygame, sys, copy, npc, settingsscreen, highScores
pygame.init()
loading = pygame.image.load('loading600x600.png').convert_alpha()


msize = 100
numrect = 9
rectsize = 15

lvl = 0  #global variable to hold the floor level
mobsKilled = 0  #global variable to hold the number of monsters killed
facing = 'right'  #global variable to hold the direction that the player is facing, left or right

class Camera(object):
    """
    Class used to offset the maze so that the player is centered and gives a zoomed in like functionality
    """
    def __init__(self, camera_func, width, height):
        """
        Called when creating an instance of Camera
        args:       camera_func     -   (function)camera function to be used to calculate the display offset
                    width           -   (int)Total width of the maze
                    height          -   (int)Total height of the maze
        return:
        """
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, target):
        """
        Applies the offset to each sprite so that the player remains centered
        args:       target      -   (pygame sprite)The sprite that is being offset
        return:     Returns the offset sprite
        """
        return target.rect.move(self.state.topleft)

    def update(self, target):
        """
        Takes in a target sprite and uses that sprite as the center point for offsetting the rest of the sprites
        args:       target      -   (pygame sprite)Sprite being used as the focal point for the offset
        return:
        """
        self.state = self.camera_func(self.state, target.rect)


def startEndPoints(mazz):
    """
    Runs through the maze array and finds the pre-generated entry and exit points
    args:       mazz      -   (array)The maze being used
    return:     Returns coordinates for the entry point and the exit point
    """
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
    """
    Generates the sprites for the area around the player to later be displayed
    args:       screen      -   (pygame surface object)The screen where everything is being displayed
                arr         -   (array)The maze being used
                x           -   (x-coord)The x-coordinate of the player
                y           -   (y-coord)The y-coordinate of the player
                mobList     -   (list)The list of mobs in this generated maze
                walls       -   (sprite group)The sprite group for the walls of the maze
                monstors    -   (sprite group)The sprite group for the monsters of the maze
                exit        -   (sprite group)The sprite group for the exit point of the maze
                floors      -   (sprite group)The sprite group for the floors of the maze
                entry       -   (sprite group)The sprite group for the entry point of the maze
    return:
    """
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
    #X and Y lower and upper are the bounds for the sprites being generated. This generates only the sprites that get displayed, so its more efficient
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
    """
    Generates monster objects and sprites
    args:       mobList     -   (list)List of monster objects to be created
                monstors    -   (sprite group)The sprite group for the monsters in the maze
    return:     Fills the monstors sprite group
    """
    for i in mobList:
        if i is None:
            continue
        else:
            monstar = Monsters(i.startY,i.startX,i)
            monstar.add(monstors)

class Monsters (pygame.sprite.Sprite):
    """
    Monster class used to generate monster objects and sprites
    """
    monsterColor = (255,0,0,)
    def __init__(self, i, j, monsterObj):
        """
        Generates a monster sprite
        args:       i           -   (coordinate)X-coordinate for the monster sprite
                    j           -   (coordinate)Y-coordinate for the monster sprite
                    monsterObj  -   (monster attributes)Object to give the sprite npc attributes
        return:
        """
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
        """
        Updates the position of the monster sprite
        args:       pos     -   (coordinates)Coordinates to be used to update the sprites position
        return:
        """
        self.rect.topleft = (pos)

class Entry (pygame.sprite.Sprite):
    """
    Sprite class used to generate the entry point sprite
    """
    entryColor = (255,255,0,)
    def __init__(self, i, j):
        """
        Generates the entry point sprite
        args:       i       -   (coordinate)X-coordinate for the sprite
                    j       -   (coordinate)Y-coordinate for the sprite
        return:
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30,30])
        self.image.fill(self.entryColor)
        self.pos = (i*30,j*30,)
        self.rect = pygame.Rect(i*30,j*30,30,30)
        self._layer = 4

class Dagger (pygame.sprite.Sprite):
    """
    Class used to generate the attack sprites
    """
    daggerColor = (100,200,100,)
    def __init__(self, i, j, direction):
        """
        Generates the attack sprite if and when an attack is initiated
        args:       i           -   (coordinate)X-coordinate for the sprite
                    j           -   (coordinate)Y-coordinate for the sprite
                    direction   -   (right or left)Direction the player is facing, used to decide what image to use for the sprite
        return:
        """
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
        """
        Updates the position of the dagger sprite
        args:       pos     -   (coordinates)Coordinates to be used to update the sprites position
        return:
        """
        self.rect.topleft = (pos)

class Exit (pygame.sprite.Sprite):
    """
    Class used to generate the exit sprite
    """
    exitColor = (255,51,255,)
    def __init__(self, i, j):
        """
        Generates the exit point sprite
        args:       i       -   (coordinate)X-coordinate for the sprite
                    j       -   (coordinate)Y-coordinate for the sprite
        return:
        """
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30,30])
        self.image.fill(self.exitColor)
        self.pos = (i*30,j*30,)
        self.rect = pygame.Rect(i*30,j*30,30,30)
        self._layer = 4

class Flor (pygame.sprite.Sprite):
    """
    Class used to generate the floor sprites
    """
    floorColor = (102,51,0,)
    def __init__(self, i, j):
        """
        Generates a floor sprite
        args:       i       -   (coordinate)X-coordinate for the floor sprite
                    j       -   (coordinate)Y-coordinate for the floor sprite
        return:
        """
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface([30,30])
        #self.image.fill(self.floorColor)
        self.image = pygame.image.load('dungeon_floor.png').convert_alpha()
        self.pos = (i*30,j*30,)
        self.rect = pygame.Rect(i*30, j*30, 30, 30)
        self._layer = 2

class Wal (pygame.sprite.Sprite):
    """
    Class used to generate the wall sprites
    """
    wallColor = (0,204,0,)
    def __init__(self, i, j):
        """
        Generates a wall sprite
        args:       i       -   (coordinate)X-coordinate for the wall sprite
                    j       -   (coordinate)Y-coordinate for the wall sprite
        return:
        """
        pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.Surface([30,30])
        #self.image.fill(self.wallColor)
        self.image = pygame.image.load('stone_wall.png').convert_alpha()
        self.pos = (i*30,j*30,)
        self.rect = pygame.Rect(i*30,j*30,30,30)
        self._layer = 2

class Player (pygame.sprite.Sprite):
    """
    Class used to generate the player sprite
    """
    playerColor = (51,255,255,)
    def __init__(self, i, j, direction):
        """
        Generates the player sprite
        args:       i           -   (coordinate)X-coordinate for the player sprite
                    j           -   (coordinate)Y-coordinate for the player sprite
                    direction   -   (right or left)Direction to be used to determine what way the sprite image faces
        return:
        """
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
        """
        Updates the position of the player sprite
        args:       pos         -   (coordinates)Coordinates to be used to update the sprites position
                    direction   -   (right or left)Direction to be used to determine what way the sprite image faces
        return:
        """
        #self.rect.topleft = (xCent*30,yCent*30,)
        self.rect.topleft = (pos)
        if direction == 'left':
            self.image = pygame.image.load('mainplayerleft.png').convert_alpha()
            facing = 'left'
        elif direction == 'right':
            self.image = pygame.image.load('mainplayerright.png').convert_alpha()
            facing = 'right'

def simple_camera(camera, target_rect):
    """
    Method to offset the image
    args:       camera          -   (camera object)Object that utilizes the camera class
                target_rect     -   (rect)Target rect to apply the offset to
    return:     Returns the new offset rect
    """
    l, t, _, _ = target_rect
    _, _, w, h = camera
    return pygame.Rect(-l+300, -t+300, w, h)

def complex_camera(camera, target_rect):
    """
    Method to offset the image, but more complex so that the player doesn't stay centered near edges
    args:       camera          -   (camera object)Object that utilizes the camera class
                target_rect     -   (rect)Target rect to apply the offset to
    return:     Returns the new offset rect
    """
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l+300, -t+300, w, h

    l = min(0, l)
    l = max(-(camera.width-600), l)
    t = max(-(camera.height-600), t)
    t = min(0, t)

    return pygame.Rect(l, t, w, h)

def runMaze(mazze, rectangles):
    """
    Main method that runs the majority of the game display logic, contains the pygame while loop
    args:       mazze          -   (array)Maze to be used to draw and display
                rectangles     -   (rectangle list)List of rectangles in the maze
    return:     Displays the maze, various sprites, player scores, etc.
    """
    global lvl
    global mobsKilled
    startx, starty, endx, endy = 0, 0, 0, 0
    startx, starty, endx, endy = startEndPoints(mazze)
    screen = pygame.display.set_mode((600,600,)) #pygame display object
    all_entities = pygame.sprite.LayeredUpdates() #sprite group of all sprites
    walls = pygame.sprite.LayeredUpdates() #sprite group for the walls
    players = pygame.sprite.GroupSingle() #sprite group for the player
    monstors = pygame.sprite.LayeredUpdates() #sprite group for the monsters
    exit = pygame.sprite.GroupSingle() #sprite group for the exit point
    floors = pygame.sprite.LayeredUpdates() #sprite group for the floors
    entry = pygame.sprite.GroupSingle() #sprite group for the entry point
    daggers = pygame.sprite.GroupSingle() #sprite group for the attacks
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
    camera = Camera(complex_camera, total_level_width, total_level_height) #camera object used to generate the offsets
    playerOne = Player(x, y, facing) #player object and sprite
    playerOne.add(players)
    while not done:
            for event in pygame.event.get():
                    pressed = pygame.key.get_pressed()
                    if event.type == pygame.QUIT:
                        done = True
                        print("You Killed " + str(mobsKilled) + " Monsters.")
                        highScores.setHighScore( lvl-1, mobsKilled)
            pygameMazeDraw(screen, mazze, y, x, mobList, walls, monstors, exit, floors, entry) #generates the necessary sprites and objects to later be displayed
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
                            pygame.display.set_caption("Dungeon Crawlers" + "               " + "Monsters Killed:   " + str(mobsKilled) + "         Current Floor:   " + str(lvl))
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
                            pygame.display.set_caption("Dungeon Crawlers" + "               " + "Monsters Killed:   " + str(mobsKilled) + "         Current Floor:   " + str(lvl))
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
                            pygame.display.set_caption("Dungeon Crawlers" + "               " + "Monsters Killed:   " + str(mobsKilled) + "         Current Floor:   " + str(lvl))
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
                            pygame.display.set_caption("Dungeon Crawlers" + "               " + "Monsters Killed:   " + str(mobsKilled) + "         Current Floor:   " + str(lvl))
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
                screen.blit(e.image, camera.apply(e)) #Applies the offsets to the sprites and draws them to the screen

            screen.convert_alpha()
            pygame.display.flip() #updates the screen to show the changes
            all_entities.empty()
            walls.empty()
            floors.empty()


            clock.tick(100)
            screen.fill((0,0,0,))
        #I don't know where to put this that it would work
    # print("You Killed " + str(mobsKilled) + " Monsters.")
    # highScores.setHighScore( lvl-1, mobsKilled)

def main():
    """
    Main callable method to be used if this file is called by another class or file
    args:
    return:
    """
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
    pygame.display.set_caption("Dungeon Crawlers" + "               " + "Monsters Killed:   " + str(mobsKilled) + "         Current Floor:   " + str(lvl))
    runMaze(maze, rectangles)
