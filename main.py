import msvcrt

class Player:
	""" Player: defines the base stats of the player """

	health = 100
	sick = False
	morale = "standard"				# three types of morale, [low, standard, and high]
							# it matters when a problem occurs, if a player has
							# low morale than it is harder to fix something,
							# the opposite as if he had high morale

	def __init__(self, name):
		self.name = name

class Item:
	""" Item: will be a template for making items such as medicine or food """

	def __init__(self, name, pounds, heal=False):
		self.name = name
		self.pounds = pounds
		self.heal = heal # will be True if it can get rid of sickness

class Problem:
	""" Problem: will consist of all of the diseases, spaceship problems, and 'space madness' values """
	
	def __init__(self, name, altname, death_timer, recovery):
		self.name = name							# name of problem
		self.death_timer = death_timer						# turns it takes to die with it
		self.recovery = percentage(recovery, 100)				# chance to get rid of it

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

def percentage(part, whole):
	""" percentage: turn a regular number into a percentage """
	
	return 100 * float(part)/float(whole)

day = 0			# number day it is, 26 turns in total

print("Hello, welcome to A Journey To Mars. [Press enter to continue]")
msvcrt.getch()
print("Give me the names of you and the other two members of your crew:")
names = get_names()
print("The next step in the journey is that you must gather supplies.")
msvcrt.getch()

# definitions after inventory, will probably move into seperate file

Player1 = Player(names[0])
Player2 = Player(names[1])
Player3 = Player(names[2])
Flu = Problem("Flu", "the flu", 4, 30)
S_virus = Problem("Stomach Virus", "a stomach virus", 2, 80)
Smallpox = Problem("Smallpox", "smallpox", 6, 6)
Sprain = Problem("Sprain", "a sprain", 15, 90)
B_arm = Problem("Broken Arm", "a broken arm", 0, 50)
Food = Item("Food", 40)
Meds = Item("Medicine", 50, True)
S_parts = Item("Spare Parts", 400)
