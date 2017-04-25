import msvcrt

class Player:
	
	health = 100
	
	def __init__(self, name):
		self.name = name
		
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
	
print("Hello, welcome to A Journey To Mars. [Press enter to continue]")
msvcrt.getch()
print("Give me the names of you and the other two members of your crew:")
names = get_names()
print("The next step in the journey is that you must gather supplies.")
msvcrt.getch()

Player1 = Player(names[0])
Player2 = Player(names[1])
Player3 = Player(names[2])