#Max
import random, MazeGenerator, gameStuff6, pygame


class Mob:
    """
    Class that defines a generic mob and gives it predefined or customized attributes
    """
    def __init__(self, mobType, level=0, attack=0, defense=0, startX=0, startY=0):
        """
        Generates the attributes for the monster
        args:       mobType     -   (str)Type of monster
                    level       -   (int)Level for the monster
                    attack      -   (int)Attack level for the monster
                    defense     -   (int)Defense level for the monster
                    startX      -   (int)Starting x-coordinate for the monster
                    startY      -   (int)Starting y-coordinate for the monster
        return:     Returns a created monster
        """
        self.level = level
        self.mobType = mobType
        self.attack = attack
        self.defense = defense
        self.startX = startX
        self.startY = startY
        self.listPos = 0

    def displayStats(self):
        """
        Prints the Stats for the monster
        args:
        return:
        """
        print("The mobs level is:\t\t" + str(self.level))
        print("The mobs type is:\t\t" + str(self.mobType))
        print("The mobs attack level is:\t" + str(self.attack))
        print("The mobs defense level is:\t" + str(self.defense))
        print("The mobs startX point is:\t" + str(self.startX))
        print("The mobs startY point is:\t" + str(self.startY))
        print("The List Pos is:\t\t" + str(self.listPos))
    def setListPos(self, val):
        self.listPos = val


def generateMobs(rect, lvl):
    """
    Randomly generates a monster in the given rectangle
    args:       rect    -   (rectangle information)Rectangle information to be used to generate a monster within
                lvl     -   (int)Level to be used to generate the monsters stats
    return:     Returns either a monster object or 0 if a monster is not going to be generated in the given rect
    """
    randVal = random.randrange(3)
    if randVal == 0:
        xLen, yLen, bottomLeftXCord, bottomLeftYCord = rect
        xLen = xLen-2
        yLen = yLen-2
        bottomLeftXCord = bottomLeftXCord + 1
        bottomLeftYCord = bottomLeftYCord + 1
        rectPoints = []
        for i in range (yLen):
            for j in range (xLen):
                rectPoints.append((bottomLeftYCord+i,bottomLeftXCord+j,))
        rectPoints = list(set(rectPoints))
        newPoints = rectPoints[:]
        val = len(newPoints)
        randPoint = random.choice(newPoints)

        return(Mob("Zombie", lvl, lvl*2, lvl*3, randPoint[1],randPoint[0]))
    else:
        return 0

def main(rectangles, lvl):
    """
    Main callable to be used to generate monsters in a maze
    args:       rectangles      -   (array)List of rectangles and their respective data in the maze
                lvl             -   (int)Level to be used when generating the monster
    return:     Returns a list of generated monsters
    """
    mobList = []
    for i in rectangles:
        thing = generateMobs(i, lvl)
        if thing == 0:
            continue
        else:
            mobList.append(thing)
    return mobList
