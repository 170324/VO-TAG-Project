import msvcrt
import math
import random

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
							# also need to add a "total" counter showing if they are over 5000 or not

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

	pmax = 5000		# max pounds they can carry
	amount = 0		# current amount of pounds
	current = 0		# 0 for spare, 1 for meds, 2 for food
	objects = ["spare parts", "medical products", "food"]
	listamount = [0, 0, 0] # first item is spare, 2nd is meds, 3rd is food

	while (current < 3):
		if (amount <= 5000):
			print("Please enter the number of {} that you would like to bring.".format(objects[current]))
			while True:
				item = input()
				try:
					val = int(item)
					if val < 0:
						print("You need to insert a positive integer.")
						continue
					break
				except ValueError:
					print("You need to enter a valid amount.")
					continue
			if (current == 0 and ((val * 200) <= pmax)):			# spare parts
				new_amount = val * 200
				listamount[0] += val
			elif (current == 1 and ((val * 100) <= pmax)):			# medical products
				new_amount = val * 100
				listamount[1] += val
			elif (current == 2 and ((val * 1.5) <= pmax)):			# food
				new_amount = val * 1.5
				listamount[2] += val
			elif (current == 0):
				new_amount = pmax - amount
				listamount[0] += math.floor(new_amount / 200)
				amount += new_amount
				break
			elif (current == 1):
				new_amount = pmax - amount
				listamount[1] += math.floor(new_amount / 100)
				amount += new_amount
				break
			elif (current == 2):
				new_amount = pmax - amount
				listamount[2] += math.floor(new_amount / 1.5)
				amount += new_amount
				break
			amount += new_amount
			current += 1

	print("You have decided to bring {} spare parts, {} medical products, and {} packs of food. This adds up to {}/5000 pounds. Is this correct? [Y/N]"
		  .format(listamount[0], listamount[1], listamount[2], amount))

	while True:
		confirm = input()
		if (confirm.lower() == "y" or confirm.lower() == "n"):
			break
		else:
			print("Please enter a valid answer [Y/N]")
			continue

	if (confirm.lower() == "y"):
		if (listamount[0] != 0):		# check if any spare parts need to be added
			Inventory.add_item(S_parts)
			Inventory.counter["Spare Parts"] += (listamount[0] - 1)

		if (listamount[1] != 0):		# check if any medical parts need to be added
			Inventory.add_item(Meds)
			Inventory.counter["Medical Products"] += (listamount[1] - 1)

		if (listamount[2] != 0):		# check if any food needs to be added
			Inventory.add_item(Food)
			Inventory.counter["Food"] += (listamount[2] - 1)
	elif (confirm.lower() == "n"):
		print("Please enter the amount of the items you want again.")
		msvcrt.getch()
		get_items()

def percentage(part, whole):
	""" percentage: turn a regular number into a percentage """

	return 100 * float(part)/float(whole)

def sick_damage():
	""" sick_damage: deal damage to whoever is sick at the moment """
	
	global sicklist
	for key in sicklist:
#		key.health -= val.dpt
		print(key.name)
		print(key.health)
	
def daily():
	""" daily: generates what happens during the day """

	day = 0						# number day it is, 26 turns in total
	days_since_problem = 0				# there will be a minimum of 3 - 5 days before something can happen
	global sicklist
	
	while (day <= 26):
		if (days_since_problem == 0):
			problem = random.randint(1, 5)		# 1 is sick, 2 is spaceship problems
							# 3 is meteor shower, 4-5 are nothing atm

			if (problem == 1):		# get someone sick
				victim = players[random.randint(0, 2)]
				disease = diseases[random.randint(0, 4)]
				sicklist[victim] = disease
				print(victim.name + "has got sick with " + disease.altname)
				msvcrt.getch()
				sick_damage()
				


# global and class definitions
Flu = Problem("Flu", "the flu", 20, 40)
S_virus = Problem("Stomach Virus", "a stomach virus", 45, 80)
Smallpox = Problem("Smallpox", "smallpox", 15, 20)
Sprain = Problem("Sprain", "a sprain", 1, 85)
B_arm = Problem("Broken Arm", "a broken arm", 7, 50)
Food = Item("Food", 1.5)
Meds = Item("Medical Products", 100, True)
S_parts = Item("Spare Parts", 200)
Inventory = Inventory()

print("Hello, welcome to A Journey To Mars. [Press any key to continue]")
msvcrt.getch()
print("Give me the names of you and the other two members of your crew:")
names = get_names()
print("For the preparation of this journey, you must gather supplies.")
msvcrt.getch()
print("The supplies you may bring are food, medical products, and spare parts.")
msvcrt.getch()
print("Your spaceship has a maximum cargo of 5000 pounds. If you exceed the limit, the rocket will not launch due to safety precuations.")
msvcrt.getch()
print("Spare parts weigh 200 lb per unit. You can use these to repair the spaceship if it breaks.")
msvcrt.getch()
print("Medical products weigh 100 lb per unit. These will help you heal diseases.")
msvcrt.getch()
print("Food weighs 1.5 lb per pack. This will make sure you do not starve on the journey.")
msvcrt.getch()
get_items()

Player1 = Player(names[0])
Player2 = Player(names[1])
Player3 = Player(names[2])
players = [Player1, Player2, Player3]
diseases = [Flu, S_virus, Smallpox, Sprain, B_arm]
sicklist = {}
