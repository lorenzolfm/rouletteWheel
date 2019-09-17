import random

class Game:
	def __init__(self):
		self.run = True
		self.roulette = None
		self.drawnNumber = None
		self.runGame()

	def runGame(self):
		self.displayIntro()
		settings.runSettingsRoutine()
		self.instantiateRoulette()
		while self.run:
			#Making bets
			self.spinRoulette()
			self.getBets()
			#Playing the round

			self.checkResult()

	def displayIntro(self):
		print('\n------------------------------------------------')
		print("+-+-+- Welcome to Bash Terminal Cassino!-+-+-+\n+-+-+- Let's play a Roulette Game!-+-+-+\n")
		print("+- If you don't know how to play this game -+\n+- you can take a look at the readme.txt file -+\n+- for instructions and rules -+\n")
		print("+- You can press CTRL + D at any time to exit -+")
		print('------------------------------------------------\n')

	def instantiateRoulette(self):
		if settings.selectedRoulette == '1':
			self.roulette = AmericanRoulette()
		elif settings.selectedRoulette == '2':
			self.roulette = EuropeanRoulette()
		else:
			self.roulette = FrenchRoulette()

	def getBets(self):
		for player in players.playersList:
			player.enterBetValue()
			player.chooseBet()

	def spinRoulette(self):
		self.drawnNumber = self.roulette.drawnNumber()
		print(self.drawnNumber)

	def checkResult(self):
		for player in players.playersList:
			if player.betAmmount != 0:
				if player.betTypeChoice == '1':
					if player.betId == self.drawnNumber['id']:
						print(f'{player.name} won!')
						#subtract player.betAmmount*multiplier from self.roulette.bank and ad it to player.pot (the multiplier value depends on rouletteType it can be an atributte of child class based on a conditional)
						player.pot += player.betAmmount*35 + player.betAmmount
						self.roulette.bank -= player.betAmmount*35
						print(f'{player.name} has won {player.betAmmount*35 + player.betAmmount} ')
						print(f'{player.betAmmount*35} subtracted from bank')
						print(f'{player.name} pot = {player.pot}')
						print(f'Bank = {self.roulette.bank}')
					else:
						print(f"\nPlayer {player.name} bet on {player.betId}, but the drawn number was {self.drawnNumber['id']}\n")
					    #add it to the bank
						self.roulette.bank += player.betAmmount
						print(f'Player pot = {player.pot}')
						print(f'Bank = {self.roulette.bank}')
				else:
					if not(self.drawnNumber['id'] == '00' or self.drawnNumber['id'] == '0'):
						#Call the function
						#If output is the same
							#Ditribute money
							pass
					else:
						self.roulette.bank += player.betAmmount
						print(f'Player pot = {player.pot}')
						print(f'Bank = {self.roulette.bank}')
					#if drawn number is not 0 or 00, call the respective function passing self.drawnNumber and compare it with mapping dictionary from player.betChoice
					#if output is the same, make the correct changes to player.pot and bank
					#else give betAmmount to bank
					pass

class GameSettings:
	def __init__(self):
		self.rouletteTypes = {'1': 'American Roulette', '2': 'European Roulette', '3': 'French Roulette'}
		self.selectedRoulette = None
		self.numberOfPlayers = None

	def setRouletteType(self):
		#Dar um jeito nisso
		while self.selectedRoulette not in ['1','2','3']:
			print('\n------------------------------------------------')
			self.selectedRoulette = input('+- 1-American Roulette -+\n+- 2-European Roueltte -+\n+- 3-French Roulette -+\nSelect game style: ')
			print('------------------------------------------------\n')
			if self.selectedRoulette == '1':
				print(f'\n+-+-+- Ok! Loading the {self.rouletteTypes[self.selectedRoulette]} -+-+-+\n')
			elif self.selectedRoulette == '2':
				print(f'\n+-+-+- Ok! Loading the {self.rouletteTypes[self.selectedRoulette]} -+-+-+\n')
			elif self.selectedRoulette == '3':
				print(f'\n+-+-+- Ok! Loading the {self.rouletteTypes[self.selectedRoulette]} -+-+-+\n')
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
		print(f"+-+-+- Ok. Let's begin the game! -+-+-+")
		print('-----------------------------------------------------------\n')

	def getGameSettings(self):
		print('\n------------------------------------------------')
		print(f'Setting {self.rouletteTypes[self.selectedRoulette]} game for {self.numberOfPlayers} player(s)!')
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
		self.betTypeChoice = None

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
		self.betTypeChoice = None
		if self.roundSkipedStreak == 0:
			print('\n------------------------------------------------------------------')
			print(f'{self.name}, Choose your bet type')
			while self.betTypeChoice not in ['1','2']:
				self.betTypeChoice = input('Enter 1 to make an INNER Bet - Enter 2 to make an OUTSIDE bet: ')
			if self.betTypeChoice == '1':
				self.betId = None
				#Aqui tem que ter a condicao do tabuleiro americano com 00
				while self.betId not in (str(i) for i in range(0,37)):
					self.betId = input('\nSelect a number between 0 and 36: ')
					print('------------------------------------------------------------------\n')
			else:
				while self.outsideBetCategory not in (str(i) for i in range(1,13)):
					self.outsideBetCategory = input("\n1-Red\n2-Black\n3-Even\n4-Odd\n5-One to Eighteen\n6-Eighteen to Thirty-Six\n7-First 12\n8-Second 12\n9-Third 12\n10-Column 1\n11-Column 2\n12-Column 3\nSelect bet category: ")
					print('------------------------------------------------------------------\n')

class Roulette:
	def __init__(self):
		self.result = None
		self.bank = 1000
		self.board = []
		self.createBoard()

	def createBoard(self):
		for number in range(1,37):
			self.board.append(
				{
					'id': str(number),
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
			)
		self.board.insert(0,
			{
				'id': '0',
				'even': False,
				'red': False,
				'lessOrEqual18': False,
				'firstTwelve': False,
				'secondTwelve': False,
				'thirdTwelve': False,
				'firstColumn': False,
				'secondColumn': False,
				'thirdColumn': False,
			}
		)

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

	def drawnNumber(self):
		return random.choice(self.board)

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
		self.add00()

	def add00(self):
		self.board.insert(0,
			{
				'id': '00',
				'even': False,
				'red': False,
				'lessOrEqual18': False,
				'firstTwelve': False,
				'secondTwelve': False,
				'thirdTwelve': False,
				'firstColumn': False,
				'secondColumn': False,
				'thirdColumn': False,
			}
		)


players = Players()
settings = GameSettings()
game = Game()


#Criar parceria com empresas e laboratorios da UFSC
#Unir pesquisa e iniciativa privada
#Terceirizar o processo de teste
#Fundos quantitativos
