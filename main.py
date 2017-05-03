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
		self.heal = heal 			# will be True if it can get rid of sickness

class Problem:
	""" Problem: will consist of all of the diseases, spaceship problems, and 'space madness' values """

	def __init__(self, name, altname, dpt, recovery):
		self.name = name							# name of problem
		self.altname = altname							# used in a string
		self.dpt = dpt								# damage per turn
		self.recovery = percentage(recovery, 100)				# chance to get rid of it

class Inventory:
	""" Inventory: will maintain the current state of the player's items """

	def __init__(self):
		self.items = {}		# this contains actual item stats
		self.counter = {}	# this contains the amount they have in inventory

	def __str__(self):
		message = "\t".join(["Name", "Pounds", "Quantity"])
		for item in self.items.values():
			message += "\n" + "\t".join([str(x) for x in [item.name, item.pounds, self.counter[item.name]]])
		return message		# need to fix the alignment of output

	def add_item(self, item):
		""" add_item: adds an item class member to inventory's dictionary """

		self.items[item.name] = item

		if item.name in self.counter.keys():
			self.counter[item.name] += 1
		else:
			self.counter[item.name] = 1

	def remove_item(self, item):
		""" remove_item: removes item from both items and counter dictionaries """

		if item.name in self.counter.keys():
			self.counter[item.name] -= 1

		if self.counter[item.name] == 0:
			del self.counter[item.name]
			del self.items[item.name]

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

def get_items():
	""" get_items: gets the initial items the player wants and stores them in inventory """
	
	pass
			
def percentage(part, whole):
	""" percentage: turn a regular number into a percentage """

	return 100 * float(part)/float(whole)

print("Hello, welcome to A Journey To Mars. [Press any key to continue]")
msvcrt.getch()
print("Give me the names of you and the other two members of your crew:")
names = get_names()
print("For the preparation of this journey, you must gather supplies.")
msvcrt.getch()
get_items()

# next is to figure out how to get the amount they want and store it in the inventory

# global and class definitions
day = 0			# number day it is, 26 turns in total
Player1 = Player(names[0])
Player2 = Player(names[1])
Player3 = Player(names[2])
Flu = Problem("Flu", "the flu", 20, 40)
S_virus = Problem("Stomach Virus", "a stomach virus", 45, 80)
Smallpox = Problem("Smallpox", "smallpox", 15, 20)
Sprain = Problem("Sprain", "a sprain", 1, 85)
B_arm = Problem("Broken Arm", "a broken arm", 7, 50)
Food = Item("Food", 1.5)
Meds = Item("Medicine", 100, True)
S_parts = Item("Spare Parts", 200)
Inventory = Inventory()
