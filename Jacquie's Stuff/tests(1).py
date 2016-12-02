import mainPlayer
import NPC

def main():
	print("------Testing Player------")
	Joe = mainPlayer.mainPlayer("Joe")
	Joe.displayStats()
	Joe.levelUp()
	print()
	print("------Testing NPCs------")
	maleficent=NPC.NPC("Zombie")
	maleficent.displayStats()
	print()
	print("------Testing Invalid Input------")
	Anna = mainPlayer.mainPlayer("Max",0,-1,0,0)
	Jacquie = mainPlayer.mainPlayer("Max",0,0,-1,0)
	Isabel = mainPlayer.mainPlayer("Max",0,0,0,-1)
	Max = mainPlayer.mainPlayer("Max",-1,0,0,0)
	Max.displayStats()
	print()
	print("------Testing Attack Win------")
	Joe.attackNPC(maleficent)
	Joe.displayStats()
	print()
	print("------Testing Attack Loss------")
	hades=NPC.NPC("Vampire", 5, 5, 5)
	hades.displayStats()
	Joe.attackNPC(hades)
	Joe.displayStats()
	print()
	print("------Testing Attack Tie------")
	hades=NPC.NPC("Vampire", 2, 2, 2)
	hades.displayStats()
	Joe.displayStats()
	Joe.attackNPC(hades)
	Joe.displayStats()
main()