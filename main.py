import msvcrt

class Player:
	""" Player: defines the base stats of the player """

	health = 100

	def __init__(self, name):
		self.name = name

class Item:
	""" Will be a template for making items such as medicine or food """

	def __init__(self):
		pass	# will require information about what item it is

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

# may turn below into one fuction to start game

print("Hello, welcome to A Journey To Mars. [Press enter to continue]")
msvcrt.getch()
print("Give me the names of you and the other two members of your crew:")
names = get_names()
print("The next step in the journey is that you must gather supplies.")
msvcrt.getch()

Player1 = Player(names[0])
Player2 = Player(names[1])
Player3 = Player(names[2])
