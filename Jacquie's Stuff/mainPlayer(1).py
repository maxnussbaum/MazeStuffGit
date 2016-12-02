import random

class mainPlayer:
	def __init__(self, named, level=1, attack=1, defense=1, experience=0):
		if(level<1 or attack<0 or defense<0 or experience<0):
			print("Invalid Input")
			self.valid = False
		else:
			self.valid = True
			self.named = named
			self.level = level
			self.attack = attack
			self.defense = defense
			self.experience = experience

	def displayStats(self):
		# print("Your level is:\t\t" + str(self.level))
		# print("Your EXP is:\t\t" + str(self.experience))
		# print("Your attack level is:\t" + str(self.attack))
		# print("Your defense level is:\t" + str(self.defense))
		if(self.valid == True):
			print("Name\tLevel\tEXP\tAttack\tDefense")
			print(str(self.named) + "\t" + str(self.level) + "\t" + str(self.experience) + "\t" + str(self.attack) + "\t" + str(self.defense))
		else:
			print("This Player doesn't exist")

	def attackNPC(self, badguy):
		if (badguy.attack-self.attack>=3):
			self.grimReaper()
		elif(self.attack-badguy.attack>=3):
			self.experience += (badguy.level)*10
			print("You killed the ", badguy.mobType)
		else:
			randVal = random.randrange(1)
			if(randVal==0):
				self.experience += (badguy.level)*10
				print("You killed the", badguy.mobType)
			else:
				self.attack = 0
				self.defense = 0
				self.grimReaper()

	def grimReaper(self):
		self.attack = 0
		self.defense = 0
		print("You died, you scrub")

	def levelUp(self):
		if (self.experience == 100):
			self.level +=1
			self.exp = 0

def main():

	displayStats()
