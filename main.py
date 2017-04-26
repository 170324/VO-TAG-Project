from random import randint
import msvcrt

class Player:
	""" Player: defines the base stats of the player """

	health = 100
	sick = 0
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
daycount = 0		#day count counts days since last problem.
			#Don't want problems more often than 5 turns, number can be adjusted
sicknesses = ["**healthy**", "a broken arm", "a sprain", "smallpox", "a stomach virus", "the flu"]

def turnChoice():
#gives players options to view conditions or continue
	what = 0
    
	what = input("What would you like to do?\n1. Continue\n2. View Inventory3. Check status")
	while what < 1 or what > 3:
		what = input("Please choose a valid option")

	if what == 2:
		print(inventory)
		print("[Press enter to coninue]")
		print("\n")
		msvcrt.getch()
		turnChoice()
	elif what == 3:
		print(player1.name)
		if player1.sick > 0:
			print(player1.name + " has " + sickness[player1.sick])
		else:
			print(player1.name + "is healthy")
		print(player1.hunger)
            
		print(player2.name)
		if player2.sick > 0:
			print(player2.name + " has " + sickness[player2.sick])
		else:
			print(player2.name + "is healthy")
		print(player2.hunger)
            
		print(player3.name)
		if player3.sick > 0:
			print(player3.name + " has " + sickness[player3.sick])
		else:
			print(player3.name + "is healthy")
		print(player3.hunger)
            
		print(player4.name)
		if player4.sick > 0:
			print(player4.name + " has " + sickness[player4.sick])
		else:
			print(player4.name + "is healthy")
		print(player4.hunger)
            
		print(player5.name)
		if player5.sick > 0:
			print(player5.name + " has " + sickness[player5.sick])
		else:
			print(player5.name + "is healthy")
		print(player5.hunger)
		print("[Press enter to coninue]")
		print("\n")
		msvcrt.getch()
		turnChoice()
#end of turnChoice function

def daily():
#creates problems and runs turnChoice function
	global daycount
	global sick
	global parts
	global sickness
	what = 1
	player = 0
	sick = 0

	if daycount < 0:
		p = randint(1, 5)
        	#1 is sick; 2 is techinical difficulties; 3 is meteor shower
       		#assuming each problem has a 20% chance
        
#get people sick
		if p == 1:
			player = randint(1, 5)
			sick = randint(1, 5)
		
			if player == 1:
				player1.sick = sick
				player = player1.name
			elif player == 2:
				player2.sick = sick
				player = player2.name
			elif player == 3:
				player3.sick = sick
				player = player3.name
			elif player == 4:
				player4.sick = sick
				player = player4.name
			elif player == 5:
				player5.sick = sick
				player = player5.name
			
			print(player + " has " + sickness[sick])
            
#break things
		elif p == 2:
			fix = " "
			rep = " "
			success = 0;
			
			fix = input("The ship is broken. Would you like to repair it? ")
			while fix != "y" and fix != "Y" and fix != "n" and fix != "N":
				fix = input("Plese enter \"y\" for Yes or \"n\" for No.")
			if fix == "y" or fix == "Y":
				success = randint(1, 3)
				if success == 1:
					print("You successfully repaired the ship!")
				else:
					rep = input("You were unable to repair the ship. Would you like to replace the broken part?")
					while fix != "y" and fix != "Y" and fix != "n" and fix != "N":
						fix = input("Plese enter \"y\" for Yes or \"n\" for No.")
					if parts > 0 and (rep == "y" or rep == "Y"):
					#!!!parts variable is currently undefined. It will be part of inventory class!!!
						print("You fixed the ship!")
					else:
						print("You were unable to fix the ship. You spiraled out of control and crashed into the sun.")
						#game ends

#flying rocks                      
		elif p == 2:
			lost = randint(1, 3)
			print("You flew into a meteor shower. Lose %s weeks." %(lost))
			#factor in lost time. No turns are used, but food is wasted
#end of problems
		daycount = 6
		#can't have another problem for 5 days. Set at 6, but each turn end by removing 1 from day count, 
		#so 6 will be 5 at the end of turn

#stats and option menu
	turnChoice()

	if daycount > 0:
		daycount -= 1   #lower days since last problem
#end of daily function

print("Hello, welcome to A Journey To Mars. [Press enter to continue]")
msvcrt.getch()
print("Give me the names of you and the other two members of your crew:")
names = get_names()
print("The next step in the journey is that you must gather supplies.")
msvcrt.getch()

player1 = Player(names[0])
player2 = Player(names[1])
player3 = Player(names[2])




while day <= 26:
	daily()
	day += 1
