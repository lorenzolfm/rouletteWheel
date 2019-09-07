class Game:
	def __init__(self):
		#Select roulette type
		print("*****Welcome to Bash Cassino!*****\n\nLet's play a Roulette Game!\n")
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
		#Method for selecting roulette type
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
				print('You must select the Roulette by typing 1, 2 or 3\n')

	def selectNumberOfPlayers(self):
		while self.numberOfPlayers not in (str(i) for i in range(1,11)):
			self.numberOfPlayers = input('Enter the number of players in this game (1-10)\n')
		self.numberOfPlayers = int(self.numberOfPlayers)
		print('')
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
		for player in players.playersList:
			player.enterBetValue()
			player.chooseBetType()
		print('***All bets were made***')
		print('')

class Players:
	def __init__(self):
		self.playersList = []

	def addPlayer(self,name):
		self.playersList.append(Player(name))

class Player:
	def __init__(self,name):
		self.name = name
		self.pot = 100
		self.bet = 0

	def enterBetValue(self):
		while self.bet not in (str(i) for i in range(0,self.pot+1)):
			if self.pot > 0:
				self.bet = input(f"Player: {self.name}\nPot: {self.pot}\nHow much you wanna bet? (enter 0 to skip this round): ")
				print('')
				if self.bet not in (str(i) for i in range(0,self.pot+1)):
					print(f'***Please enter a valid input.***\n***You must choose a value between 0 and {self.pot}***')
					print('')
		self.bet = int(self.bet)
		if self.bet != 0:
			self.pot -=  self.bet
			print(f'Making a bet for {self.name}; Amount: ${self.bet}; You have ${self.pot} left')
			print('')
		else:
			print(f'{self.name} has chosen to skip this round')
			print('')

class Roulette:
	def __init__(self):
		self.board = [i for i in range(0,37)]

	def determineIfEven(self,id):
		if id % 2 == 0:
			return True
		return False

	def determineIfLessOrEqualThan18(self,id):
		if id <= 18:
			return True
		return False

	def determineIfRed(self,id):
		if id in [1,3,5,7,9,12,14,16,18,19,21,23,25,23,25,27,30,32,34,36]:
			return True
		return False

	def determineIfFirst12(self,id):
		if 1<=id<=12:
			return True
		return False

	def determineIfSecond12(self,id):
		if 13<=id<=24:
			return True
		return False

	def determineIfThird12(self,id):
		if 25<=id<=36:
			return True
		return False

	def determineIfFirstColumn(self,id):
		if id in range(1,37,3):
			return True
		return False

	def determineIfSecondColumn(self,id):
		if id in range(2,37,3):
			return True
		return False

	def determineIfThirdColumn(self,id):
		if id in range(3,37,3):
			return True
		return False

	# def buildRoulette(self):
	# 	for i in range(1,37):


class EuropeanRoulette(Roulette):
	def __init__(self):
		super().__init__()

class FrenchRoulette(Roulette):
	def __init__(self):
		super().__init__()

class AmericanRoulette(Roulette):
	def __init__(self):
		super().__init__()
		self.board.insert(0,'00')

players = Players()
game = Game()
