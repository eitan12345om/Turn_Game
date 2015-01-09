import random
import time

def attacking(attack, health):
	for hitpoints in range(attack):
		if health > 0:
			health -= 1
	return health

def healing(heal, health):
	for hitpoints in range(heal):
		if health < 100:
			health += 1
	return health

def Display_Menu(items):
	for n in range(len(items)):
		print(str(n+1) + '. ' + items[n])

menu = ["Moderate Attack (18-25). Will unlock Summon Gods after 3 consecutive turns",
	"Heavy Attack (10-35) with (0-5) recoil",
	"Heal (18-25)",
	"Poison Blade: Will add an extra 5 damage every turn"
]

menu1 = ["Moderate Attack (18-25). Will unlock Summon Gods after 3 consecutive turns",
	"Heavy Attack (10-35) with (0-5) recoil",
	"Heal (18-25)",
	"Poison Blade: Will add an extra 5 damage every turn",
	"Summon Gods: 50/50 chance of depleting Computer of half its health or losing 25 health"
]

menu2 = ["Moderate Attack (18-25). Will unlock Summon Gods after 3 consecutive turns",
	"Heavy Attack (10-35) with (0-5) recoil",
	"Heal (18-25)",
	"Summon Gods: 50/50 chance of depleting Computer of half its health or losing 25 health"
]

menu3 = ["Moderate Attack (18-25). Will unlock Summon Gods after 3 consecutive turns",
	"Heavy Attack (10-35) with (0-5) recoil",
	"Heal (18-25)"
]


Human_Health = 100
Computer_Health = 100
moves = ['moderate', 'heal']
moves2 = ['moderate', 'moderate', 'heal', 'heal', 'heal', 'heal', 'heal', 'heal', 'heal', 'heal']
Blade_poisoned = False
Gods = 0
menu_displayed = 0


print('Your health:', str(Human_Health) + '     ' + 'Computer health:', str(Computer_Health))
while Human_Health > 0 and Computer_Health > 0:

	Move = False
	while Move == False:
		print('\n' + 'Moves available:')
		if Gods < 3:
			if Blade_poisoned == False:
				Display_Menu(menu)
				menu_displayed = 0
			else:
				Display_Menu(menu3)
				menu_displayed = 3
		else:
			if Blade_poisoned == False:
				Display_Menu(menu1)
				menu_displayed = 1
			else:
				Display_Menu(menu2)
				menu_displayed = 2

		print('\n')
		Selection = input("Select your move: ")
		print('\n')
		if not Selection.isnumeric():
			print("Please type in a number corresponding to a menu option!")
			print('Your health:', str(Human_Health) + '     ' + 'Computer health:', str(Computer_Health) + '\n')
		else:
			Selection = int(Selection)
			Move = True
			if Selection == 1:
				Gods += 1
				attack = random.randrange(18, 26)
				Computer_Health = attacking(attack, Computer_Health)
				if Blade_poisoned == True:
					Computer_Health = attacking(5, Computer_Health)
					print("You've dealt", str(attack), "damage (+5 poison damage), a total damage of:", str(attack +5))
				else:
					print("You've dealt", str(attack), "damage")
			else:
				Gods = 0
				if Selection == 2:
					attack = random.randrange(10, 36)
					recoil = random.randrange(0, 6)
					Human_Health = attacking(recoil, Human_Health)
					Computer_Health = attacking(attack, Computer_Health)
					if Blade_poisoned == True:
						Computer_Health = attacking(5, Computer_Health)
						print("You've dealt", str(attack), "damage (+5 poison damage), a total damage of:", str(attack +5))
					else:
						print("You've dealt", str(attack), "damage")
					print("Your weapon recoils and hits you for:", str(recoil), "lifepoint(s)")
				elif Selection == 3:
					heal = random.randrange(18, 26)
					Human_Health = healing(heal, Human_Health)
					print("You've been healed", str(heal), 'life points!')
				elif Blade_poisoned == False and Selection == 4:
					Blade_poisoned = True
					print("You've poisoned your blade!")
				else:
					if Gods == 3:
						if Selection == 5 and Blade_poisoned == False:
						Gods = 0
						Who_is_hit = random.randrange(2)
						if Who_is_hit = 0:
							attack = Computer_Health // 2
							Computer_Health = attacking(attack, Computer_Health)
							print("You depleted half the Computer's health!")
						else:
							attack = 25
							Human_Health = attacking(attack, Computer_Health)
							print("Your attack rebounded and damaged you for 25 health!")
					else:
						Move = False
						print("Please type in a number corresponding to a menu option!")
						print('Your health:', str(Human_Health) + '     ' + 'Computer health:', str(Computer_Health) + '\n')

	if Computer_Health > 0 and Human_Health > 0:			
		print('Your health:', str(Human_Health) + '     ' + 'Computer health:', str(Computer_Health) + '\n')			
	time.sleep(1)

	if Computer_Health > 0:
		if Computer_Health > 60 or Human_Health < 30:
			Computer_move = 'moderate'
		elif Computer_Health < 25:
			Computer_move = 'heal'
		elif Computer_Health < 30:
			Computer_move = random.choice(moves2)
		else:
			Computer_move = random.choice(moves)
		if Computer_move == 'heal':
			heal = random.randrange(18, 26)
			Computer_Health = healing(heal, Computer_Health)
			print("The Computer healed", str(heal), 'life points!')
		else:
			if Computer_move == 'moderate':
				attack = random.randrange(18, 26)
			else:
				attack = random.randrange(10, 31)
			Human_Health = attacking(attack, Human_Health)
			print("You've been dealt a blow of", str(attack))

	print('Your health:', str(Human_Health) + '     ' + 'Computer health:', str(Computer_Health))
	time.sleep(2)

if Computer_Health == Human_Health:
	print('You both died! Awwzies!')
elif Computer_Health == 0:
	print('You Win! Yayzies!')
else:
	print('You Lose! Oopszies :(')