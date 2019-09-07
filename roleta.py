import random

class Game:
	def __init__(self):
		#Select roulette type
		print("*****Welcome to Bash Terminal Cassino!*****\n\nLet's play a Roulette Game!\n")
		print("***If you don't know how to play this game, you can take a look at the readme.txt file for instructions and rules***")
		self.rouletteDict = {'1': 'American Roulette', '2': 'European Roulette', '3': 'French Roulette' }
		self.selectedRoulette = None
		self.numberOfPlayers = 0
		#Faz sentido executar o jogo inteiro dentro do método construtor? Acho que nao
		self.selectRouletteType()
		self.selectNumberOfPlayers()
		self.showGameSettings()
		self.instantiatePlayers()
		self.runGame()

	def selectRouletteType(self):
		while self.selectedRoulette not in ['1','2','3']:
			self.selectedRoulette = input('Select game style:\n\n1-American Roulette\n2-European Roueltte\n3-French Roulette\n')
			print('')
			print('')
			if self.selectedRoulette == '1':
				print(f'Ok! Loading the {self.rouletteDict[self.selectedRoulette]}\n')
				roulette = AmericanRoulette()
			elif self.selectedRoulette == '2':
				print(f'Ok! Loading the {self.rouletteDict[self.selectedRoulette]}\n')
				roulette = EuropeanRoulette()
			elif self.selectedRoulette == '3':
				print(f'Ok! Loading the {self.rouletteDict[self.selectedRoulette]}\n')
				roulette = FrenchRoulette()
			else:
				print('***You must select the Roulette by typing 1, 2 or 3***\n')

	def selectNumberOfPlayers(self):
		while self.numberOfPlayers not in (str(i) for i in range(1,11)):
			self.numberOfPlayers = input('Enter the number of players in this game (1-10)\n')
		self.numberOfPlayers = int(self.numberOfPlayers)
		print('')


	def showGameSettings(self):
		print(f'Setting {self.rouletteDict[self.selectedRoulette]} game for {self.numberOfPlayers} player(s)!\n')

	def instantiatePlayers(self):
		for playerNumber in range(1,self.numberOfPlayers + 1):
			name = input(f"Player {playerNumber}, enter your name: ")
			print('')
			if self.numberOfPlayers > 1:
				while name in [player.name for player in players.playersList]:
					name = input('***Name already registered***\nPlease enter a different name: ')
					print('')
				else:
					players.addPlayer(name)
			else:
				players.addPlayer(name)
		print('')
		print(f"***Ok! Let's begin the {self.rouletteDict[self.selectedRoulette]}***")
		print('')
		print('')

	def runGame(self):
		while True:
			for player in players.playersList:
				player.enterBetValue()
				player.chooseBetType()
			print('***All bets were made***\n')

class Players:
	def __init__(self):
		self.playersList = []

	def addPlayer(self,name):
		self.playersList.append(Player(name))

class Player:
	def __init__(self,name):
		self.name = name
		self.pot = 100
		self.betAmmount = 0
		self.roundSkipedStreak = 0
		self.bet = None

	def enterBetValue(self):
		while self.betAmmount not in (str(i) for i in range(0,self.pot+1)):
			if self.pot > 0:
				self.betAmmount = input(f"Player: {self.name}\nPot: {self.pot}\nHow much you wanna bet? (enter 0 to skip this round): ")
				print('')
				if self.betAmmount not in (str(i) for i in range(0,self.pot+1)):
					print(f'***Please enter a valid input.***\n***You must choose a value between 0 and {self.pot} (integers only)***\n')
		self.betAmmount = int(self.betAmmount)
		if self.betAmmount != 0:
			self.pot -=  self.betAmmount
			if self.roundSkipedStreak != 0:
				self.roundSkipedStreak = 0
			print(f'***Making a bet for {self.name}; Amount: ${self.betAmmount}; You have ${self.pot} left***\n')

		else:
			self.roundSkipedStreak += 1
			if self.roundSkipedStreak >= 3:
				players.playersList.remove(self)
				print(f"***{self.name}, You're out! Skiped 3 rounds in a row!***\n")

			else:
				print(f'***{self.name} has chosen to skip this round***\n***Skips Left before removal: {3-self.roundSkipedStreak}***\n')

	def chooseBetType(self):
		choice = 0
		print(f'{self.name}, Choose your bet type')
		while choice not in ['1','2']:
			choice = input('Enter 1 to make an INNER Bet - Enter 2 to make an OUTSIDE bet: ')
			print('')
		if choice == '1':
			print("You're making a inner bet")
		else:
			category = ''
			while category not in (str(i) for i in range(1,13)):
				category = input("Select bet category:\n1-Red\n2-Black\n3-Even\n4-Odd\n5-One to Eighteen\n6-Eighteen to Thirty-Six\n7-First 12\n8-Second 12\n9-Third 12\n10-Column 1\n11-Column 2\n12-Column 3\n")

class Roulette:
	def __init__(self):
		self.board = []
		self.result = None

	def determineIfEven(self,number):
		if number % 2 == 0:
			return True
		return False

	def determineIfLessOrEqualThan18(self,number):
		if number <= 18:
			return True
		return False

	def determineIfRed(self,number):
		if number in [1,3,5,7,9,12,14,16,18,19,21,23,25,23,25,27,30,32,34,36]:
			return True
		return False

	def determineIfFirst12(self,number):
		if 1<=number<=12:
			return True
		return False

	def determineIfSecond12(self,number):
		if 13<=number<=24:
			return True
		return False

	def determineIfThird12(self,number):
		if 25<=number<=36:
			return True
		return False

	def determineIfFirstColumn(self,number):
		if number in range(1,37,3):
			return True
		return False

	def determineIfSecondColumn(self,number):
		if number in range(2,37,3):
			return True
		return False

	def determineIfThirdColumn(self,number):
		if number in range(3,37,3):
			return True
		return False

	def createBoard(self):
		for number in [i for i in range(0,37)]:
			if number == 0:
				self.board.append({'id':number})
			else:
				dict = {
					'id': number,
				    'even': self.determineIfEven(number),
				    'red': self.determineIfRed(number),
				    'lessOrEqual18': self.determineIfLessOrEqualThan18(number),
				    'firstTwelve': self.determineIfFirst12(number),
				    'secondTwelve': self.determineIfSecond12(number),
				    'thirdTwelve': self.determineIfThird12(number),
				    'firstColumn': self.determineIfFirstColumn(number),
				    'secondColumn': self.determineIfSecondColumn(number),
				    'thirdColumn': self.determineIfThirdColumn(number),
				}
				self.board.append(dict)

	def spinRoulette(self):
		self.result = random.randrange(0,37)

class EuropeanRoulette(Roulette):
	def __init__(self):
		super().__init__()
		self.createBoard()

class FrenchRoulette(Roulette):
	def __init__(self):
		super().__init__()
		self.createBoard()

class AmericanRoulette(Roulette):
	def __init__(self):
		super().__init__()
		self.createBoard()
		# self.board.insert(0,'00')

players = Players()
game = Game()
