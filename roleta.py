#Nome dos players

class Game:
	def __init__(self):
		#Select roulette type
		print("*****Welcome to Bash Cassino!*****\n\nLet's play a Roulette Game!\n")
		self.rouletteDict = {'1': 'American Roulette', '2': 'European Roulette', '3': 'French Roulette' }
		self.selectedRoulette = None
		self.numberOfPlayers = 0

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
		for player in range(1,self.numberOfPlayers + 1):
			name = input(f"Player {player}, enter your name: ")
			players.addPlayer(name)
		print('')
		print(f"Ok! Let's begin the {self.rouletteDict[self.selectedRoulette]}")
		print('')
		print('')

	def runGame(self):
		for player in players.playersList:
			player.makeBet()


class Roulette:
	def __init__(self):
		self.board = [str(i) for i in range(0,37)]


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

	def makeBet(self):
		validBet = False
		while not validBet:
			if self.pot > 0:
				self.bet = int(input(f"Player: {self.name}\nPot: {self.pot}\nHow much you wanna bet?: "))
				if self.bet > self.pot:
					print(f"Not enough money!, You only have ${self.pot} left")
				else:
					self.pot -= self.bet
					print(self.pot)
		#Aqui tem que ter os tipos de apostas diferentes

class AmericanRoulette(Roulette):
	def __init__(self):
		super().__init__()
		self.board.insert(0,'00')


class EuropeanRoulette(Roulette):
	def __init__(self):
		super().__init__()

class FrenchRoulette(Roulette):
	def __init__(self):
		super().__init__()

players = Players()
game = Game()
# for player in players.playersList:
# 	print(player.name)
# 	print(player.bank)
# 	print('')
