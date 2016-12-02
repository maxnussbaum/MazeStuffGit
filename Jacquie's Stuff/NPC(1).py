class NPC:
	def __init__(self, mobType, level=1, attack=1, defense=1, startX=0, startY=0):
		if(level<1 or attack<0 or defense<0):
			print("Invalid Input")
			self.valid = False
		else:
			self.valid = True
			self.level = level
			self.mobType = mobType
			self.attack = attack
			self.defense = defense
			self.startX = startX
			self.startY = startY

	def displayStats(self):
		# print("The mob's level is:\t\t" + str(self.level))
		# print("The mob's type is:\t\t" + str(self.mobType))
		# print("The mob's attack level is:\t" + str(self.attack))
		# print("The mob's defense level is:\t" + str(self.defense))
		# print("The mob's startX point is:\t" + str(self.startX))
		# print("The mob's startY point is:\t" + str(self.startY))
		if(self.valid==True):
			print("Mob\tLevel\tX,Y\tAttack\tDefense")
			print(str(self.mobType) + "\t" + str(self.level) + "\t" + str(self.startX)+str(self.startY) + "\t" + str(self.attack) + "\t" + str(self.defense))
		else:
			print("This mob is invalid")



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
