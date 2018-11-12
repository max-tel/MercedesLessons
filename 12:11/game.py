import sys

class Character:
	def __init__(self):
		self.health = 10
		self.attack = 1
		self.defense = 1
		self.name = 'No Name'

	def setStats(self, health, attack, defense, name):
		self.health = health
		self.attack = attack
		self.defense = defense
		self.name = 'No Name'

	def setHealth(self, health):
		self.health = health

	def setName(self, name):
		self.name = name

	def setAttack(self, attack):
		self.attack = attack

	def setDefense(self, defense):
		self.defense = defense

	def getHealth(self):
		return self.health

	def getAttack(self):
		return self.attack

	def getDefense(self):
		return self.defense

	def getName(self):
		return self.name

def attack(attacker, defender):
	defender.setHealth(defender.getHealth() - attacker.getAttack())
	print (defender.name + " Has "+ str(defender.health) + " Health")

def round(character1, character2):
	attack(character1, character2)
	attack(character2, character1)


def encounter(character1, character2):
	while(character1.getHealth() > 0 and character2.getHealth() > 0):
		round(character1, character2)


#Create 2 characters

player = Character()
name = input("Give your player a name: ")
player.setName(name)
enemy = Character()
enemy.setName("Goblin")
enemy.setHealth(5)
print "You run into a goblin, start the fight"
encounter(player, enemy)