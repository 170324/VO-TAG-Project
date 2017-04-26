import msvcrt

class Player:
	""" Player: defines the base stats of the player """

	health = 100
	sick = False
	morale = "standard"		# three types of morale, [low, standard, and high]
							# it matters when a problem occurs, if a player has
							# low morale than it is harder to fix something,
							# the opposite as if he had high morale

	def __init__(self, name):
		self.name = name

class Item:
	""" Will be a template for making items such as medicine or food """

	def __init__(self, name, pounds, heal=0):
		self.name = name
		self.pounds = pounds
		self.heal = heal

class Problem:
	""" Will consist of all of the diseases, spaceship problems, and 'space madness' values """
	
	def __init__(self, name, chance, death_timer, recovery):
		self.name = name					# name of problem
		self.chance = chance				# chance to get it
		self.death_timer = death_timer		# turns it takes to die with it
		self.recovery = recovery			# chance to get rid of it

class Inventory:
	""" Inventory: will maintain the current state of the player's items """

	def __init__(self):
		self.items = {}

	def __str__(self):
		pass	# will print your inventory to the player

	def add_item():
		pass	# will add an item to the player's invetory

def get_names():
	""" get_names: gets names of players and returns a list """

	i = 0
	names = []
	while (i < 3):
		name = input()
		if (name.isspace() or name == ""):
			print("A name has to have one letter minimum, enter again.")
			continue
		names.append(name)
		i += 1
	return names

day = 0			# number day it is, 26 turns in total

print("Hello, welcome to A Journey To Mars. [Press enter to continue]")
msvcrt.getch()
print("Give me the names of you and the other two members of your crew:")
names = get_names()
print("The next step in the journey is that you must gather supplies.")
msvcrt.getch()

Player1 = Player(names[0])
Player2 = Player(names[1])
Player3 = Player(names[2])
