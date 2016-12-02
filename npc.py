import random, MazeGenerator, gameStuff6, pygame


class Mob:
    def __init__(self, mobType, level=0, attack=0, defense=0, startX=0, startY=0):
        self.level = level
        self.mobType = mobType
        self.attack = attack
        self.defense = defense
        self.startX = startX
        self.startY = startY

    def displayStats(self):
        print("The mobs level is:\t\t" + str(self.level))
        print("The mobs type is:\t\t" + str(self.mobType))
        print("The mobs attack level is:\t" + str(self.attack))
        print("The mobs defense level is:\t" + str(self.defense))
        print("The mobs startX point is:\t" + str(self.startX))
        print("The mobs startY point is:\t" + str(self.startY))


def generateMobs(rect, lvl):
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
    mobList = []
    for i in rectangles:
        thing = generateMobs(i, lvl)
        if thing == 0:
            continue
        else:
            mobList.append(thing)
    return mobList
