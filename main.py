import random

class Game:
	def __init__(self):
		self.run = True
		self.runGame()

	def runGame(self):
		self.displayIntro()
		settings.runSettingsRoutine()
		while self.run:
			self.getBets()
			if players.playersList == []:
				self.run = False
				print('All players have been eliminated')

	def displayIntro(self):
		print('\n------------------------------------------------')
		print("+-+-+- Welcome to Bash Terminal Cassino!-+-+-+\n+-+-+- Let's play a Roulette Game!-+-+-+\n")
		print("+- If you don't know how to play this game -+\n+- you can take a look at the readme.txt file -+\n+- for instructions and rules -+\n")
		print("+- You can press CTRL + D at any time to exit -+")
		print('------------------------------------------------\n')

	def instantiatePlayers(self):
		for playerNumber in range(1,self.numberOfPlayers + 1):
			name = input(f"+- Player {playerNumber}, enter your name: ")
			print('')
			if self.numberOfPlayers > 1:
				while name in [player.name for player in players.playersList]:
					name = input(f'+-+-+- Name already registered -+-+-+\nPlease enter a different name for player {playerNumber}: ')
					print('')
				else:
					players.addPlayer(name)
			else:
				players.addPlayer(name)
		print('\n-----------------------------------------------------------')
		print(f"+-+-+- Ok. Let's begin the {settings.rouletteType.name} game! -+-+-+")
		print('-----------------------------------------------------------\n')

	def getBets(self):
		for player in players.playersList:
			player.enterBetValue()
			player.chooseBet()

class GameSettings:
	def __init__(self):
		self.rouletteType = None
		self.numberOfPlayers = None

	def setRouletteType(self):
		selectedRoulette = None
		while selectedRoulette not in ['1','2','3']:
			print('\n------------------------------------------------')
			selectedRoulette = input('+- 1-American Roulette -+\n+- 2-European Roueltte -+\n+- 3-French Roulette -+\nSelect game style: ')
			print('------------------------------------------------\n')
			if selectedRoulette == '1':
				self.rouletteType = AmericanRoulette()
				print(f'\n+-+-+- Ok! Loading the {self.rouletteType.name} -+-+-+\n')
			elif selectedRoulette == '2':
				self.rouletteType = EuropeanRoulette()
				print(f'\n+-+-+- Ok! Loading the {self.rouletteType.name} -+-+-+\n')
			elif selectedRoulette == '3':
				self.rouletteType = FrenchRoulette()
				print(f'\n+-+-+- Ok! Loading the {self.rouletteType.name} -+-+-+\n')
			else:
				print('\n+- You must select the Roulette by typing 1, 2 or 3 -+\n')

	def setNumberOfPlayers(self):
		while self.numberOfPlayers not in (str(i) for i in range(1,11)):
			print('\n---------------------------------------------------')
			self.numberOfPlayers = input('+- Enter the number of players in this game (1-10): ')
			print('---------------------------------------------------\n')
		self.numberOfPlayers = int(self.numberOfPlayers)
		print('')

	def instantiatePlayers(self):
		for playerNumber in range(1,self.numberOfPlayers + 1):
			name = input(f"+- Player {playerNumber}, enter your name: ")
			print('')
			if self.numberOfPlayers > 1:
				while name in [player.name for player in players.playersList]:
					name = input(f'+-+-+- Name already registered -+-+-+\nPlease enter a different name for player {playerNumber}: ')
					print('')
				else:
					players.addPlayer(name)
			else:
				players.addPlayer(name)
		print('\n-----------------------------------------------------------')
		print(f"+-+-+- Ok. Let's begin the {settings.rouletteType.name} game! -+-+-+")
		print('-----------------------------------------------------------\n')

	def getGameSettings(self):
		print('\n------------------------------------------------')
		print(f'Setting {self.rouletteType.name} game for {self.numberOfPlayers} player(s)!')
		print('------------------------------------------------\n')

	def runSettingsRoutine(self):
		self.setRouletteType()
		self.setNumberOfPlayers()
		self.getGameSettings()
		self.instantiatePlayers()

class Players:
	def __init__(self):
		self.playersList = []

	def addPlayer(self,name):
		self.playersList.append(Player(name))

class Player:
	def __init__(self,name):
		self.name = name
		self.roundSkipedStreak = 0
		self.pot = 100
		self.betAmmount = 0
		self.betId = None
		self.outsideBetCategory = None

	def enterBetValue(self):
		while self.betAmmount not in (str(i) for i in range(0,self.pot+1)):
			if self.pot > 0:
				print('\n--------------------------------------------------------')
				self.betAmmount = input(f"Player: {self.name}\nPot: {self.pot}\nHow much you wanna bet? (enter 0 to skip this round): ")
				print('--------------------------------------------------------\n')
				if self.betAmmount not in (str(i) for i in range(0,self.pot+1)):
					print(f'+-+-+- Please enter a valid input. -+-+-+\n+-+-+- You must choose a value between 0 and {self.pot} (integers only) -+-+-+\n')
		self.betAmmount = int(self.betAmmount)
		if self.betAmmount != 0:
			self.pot -=  self.betAmmount
			if self.roundSkipedStreak != 0:
				self.roundSkipedStreak = 0
			print('\n------------------------------------------------------------------')
			print(f'+-+-+- Making a bet for {self.name}; Amount: ${self.betAmmount}; You have ${self.pot} left -+-+-+')
			print('------------------------------------------------------------------\n')
		else:
			self.roundSkipedStreak += 1
			if self.roundSkipedStreak >= 3:
				players.playersList.remove(self)
				print('\n------------------------------------------------------------------')
				print(f"+-+-+- {self.name}, You're out! Skiped 3 rounds in a row! -+-+-+")
				print('------------------------------------------------------------------\n')
			else:
				print(f'+- {self.name} has chosen to skip this round -+\n+- Skips Left before removal: {3-self.roundSkipedStreak} -+\n')

	def chooseBet(self):
		betTypeChoice = None
		if self.roundSkipedStreak == 0:
			print('\n------------------------------------------------------------------')
			print(f'{self.name}, Choose your bet type')
			while betTypeChoice not in ['1','2']:
				betTypeChoice = input('Enter 1 to make an INNER Bet - Enter 2 to make an OUTSIDE bet: ')
			if betTypeChoice == '1':
				self.betId = None
				while self.betId not in (str(i) for i in range(0,37)):
					self.betId = input('\nSelect a number between 0 and 36: ')
					print('------------------------------------------------------------------\n')
				self.betId = int(self.betId)
			else:
				while self.outsideBetCategory not in (str(i) for i in range(1,13)):
					self.outsideBetCategory = input("\n1-Red\n2-Black\n3-Even\n4-Odd\n5-One to Eighteen\n6-Eighteen to Thirty-Six\n7-First 12\n8-Second 12\n9-Third 12\n10-Column 1\n11-Column 2\n12-Column 3\nSelect bet category: ")
					print('------------------------------------------------------------------\n')

class Roulette:
	def __init__(self):
		self.result = None
		self.bank = 1000

class EuropeanRoulette(Roulette):
	def __init__(self):
		super().__init__()
		self.name = 'European Roulette'

class FrenchRoulette(Roulette):
	def __init__(self):
		super().__init__()
		self.name = 'French Roulette'

class AmericanRoulette(Roulette):
	def __init__(self):
		super().__init__()
		self.name = 'American Roulette'
		# self.board.insert(0,{id : '00'})

players = Players()
settings = GameSettings()
game = Game()