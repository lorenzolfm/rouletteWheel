import random

class Game:
	def __init__(self):
		print('\n------------------------------------------------')
		print("+-+-+- Welcome to Bash Terminal Cassino!-+-+-+\n+-+-+- Let's play a Roulette Game!-+-+-+\n")
		print("+- If you don't know how to play this game -+\n+- you can take a look at the readme.txt file -+\n+- for instructions and rules -+\n")
		print("+- You can press CTRL + D at any time to exit -+")
		print('------------------------------------------------\n')
		self.roulette = None
		self.numberOfPlayers = 0
		#Faz sentido executar o jogo inteiro dentro do método construtor? Acho que nao
		self.selectRouletteType()
		self.selectNumberOfPlayers()
		self.showGameSettings()
		self.instantiatePlayers()
		self.runGame()

	def selectRouletteType(self):
		selectedRoulette = None
		while selectedRoulette not in ['1','2','3']:
			print('\n------------------------------------------------')
			selectedRoulette = input('+- 1-American Roulette -+\n+- 2-European Roueltte -+\n+- 3-French Roulette -+\nSelect game style: ')
			print('------------------------------------------------\n')
			if selectedRoulette == '1':
				self.roulette = AmericanRoulette()
				print(f'\n+-+-+- Ok! Loading the {self.roulette.name} -+-+-+\n')
			elif selectedRoulette == '2':
				self.roulette = EuropeanRoulette()
				print(f'\n+-+-+- Ok! Loading the {self.roulette.name} -+-+-+\n')
			elif selectedRoulette == '3':
				self.roulette = FrenchRoulette()
				print(f'\n+-+-+- Ok! Loading the {self.roulette.name} -+-+-+\n')
			else:
				print('\n+- You must select the Roulette by typing 1, 2 or 3 -+\n')

	def selectNumberOfPlayers(self):
		while self.numberOfPlayers not in (str(i) for i in range(1,11)):
			print('\n---------------------------------------------------')
			self.numberOfPlayers = input('+- Enter the number of players in this game (1-10): ')
			print('---------------------------------------------------\n')
		self.numberOfPlayers = int(self.numberOfPlayers)
		print('')

	def showGameSettings(self):
		print('\n------------------------------------------------')
		print(f'Setting {self.roulette.name} game for {self.numberOfPlayers} player(s)!')
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
		print('\n------------------------------------------------------')
		print(f"+-+-+- Ok! Let's begin the {self.roulette.name} -+-+-+")
		print('------------------------------------------------------\n')

	def runGame(self):
		gameOver = False
		while not gameOver:
			luckyNumber = self.roulette.spinRoulette()
			print(f'House Money: {self.roulette.bank}')
			for player in players.playersList:
				player.enterBetValue()
				player.chooseBetType()
			print('***All bets were made***\n')
			for player in players.playersList:
				if player.betTypeChoice == '1':
					if player.betId == luckyNumber['id']:
						print(f'{player.name} got a bullseye\n')
						#Verificar se bank tem essa quantia
						if 35*player.betAmmount <= self.roulette.bank:
							self.roulette.bank -= 35*player.betAmmount
							player.pot += 35*player.betAmmount
						else:
							print(f'Game Over! {player.name} broke the bank!')
							gameOver = True
							quit()
					else:
						print(f'No luck for {player.name} :(\n')
						self.roulette.bank += player.betAmmount
						player.betAmmount = 0

				else:
					pass
					#checaCategoria(numeroCategoriaSelecionada,booleanoDoNumero)
					 # if player.outsideBetCategory == '1':
						#  if luckyNumber['red'] == True:
	 					# 	 print(f'{player.name} got a bullseye\n')
	 					# else:
	 					# 	 print(f'No luck for {player.name} :(\n')
					 # elif player.outsideBetCategory == '2':
						#  if luckyNumber['red'] == False:
						# 	 print(f'No luck for {player.name} :(\n')



			#Sortear numero
			#Determinar se vencedor
			#Distribuir dinheiro

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
		self.skiped = False
		self.betTypeChoice = None
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

	def chooseBetType(self):
		if self.roundSkipedStreak == 0:
			print('\n------------------------------------------------------------------')
			print(f'{self.name}, Choose your bet type')
			while self.betTypeChoice not in ['1','2']:
				self.betTypeChoice = input('Enter 1 to make an INNER Bet - Enter 2 to make an OUTSIDE bet: ')
			if self.betTypeChoice == '1':
				self.betId = None
				while self.betId not in (str(i) for i in range(0,37)):
					self.betId = input('Select a number between 0 and 36: ')
					print('------------------------------------------------------------------\n')
				self.betId = int(self.betId)
			else:
				while self.outsideBetCategory not in (str(i) for i in range(1,13)):
					self.outsideBetCategory = input("Select bet category:\n1-Red\n2-Black\n3-Even\n4-Odd\n5-One to Eighteen\n6-Eighteen to Thirty-Six\n7-First 12\n8-Second 12\n9-Third 12\n10-Column 1\n11-Column 2\n12-Column 3\n")
					print('------------------------------------------------------------------\n')
class Roulette:
	def __init__(self):
		self.result = None
		self.bank = 1000

	def spinRoulette(self):
		self.result = random.randrange(0,37)
		if self.result == 0:
			dict = {'id': 0}
		else:
			dict = {
				'id': self.result,
				'even': self.determineIfEven(self.result),
				'red': self.determineIfRed(self.result),
				'lessOrEqual18': self.determineIfLessOrEqualThan18(self.result),
				'firstTwelve': self.determineIfFirst12(self.result),
				'secondTwelve': self.determineIfSecond12(self.result),
				'thirdTwelve': self.determineIfThird12(self.result),
				'firstColumn': self.determineIfFirstColumn(self.result),
				'secondColumn': self.determineIfSecondColumn(self.result),
				'thirdColumn': self.determineIfThirdColumn(self.result),
			}
		print(dict)
		return dict

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

	# def createBoard(self):
	# 	for number in [i for i in range(0,37)]:
	# 		if number == 0:
	# 			self.board.append({'id':number})
	# 		else:
	# 			dict = {
	# 				'id': number,
	# 			    'even': self.determineIfEven(number),
	# 			    'red': self.determineIfRed(number),
	# 			    'lessOrEqual18': self.determineIfLessOrEqualThan18(number),
	# 			    'firstTwelve': self.determineIfFirst12(number),
	# 			    'secondTwelve': self.determineIfSecond12(number),
	# 			    'thirdTwelve': self.determineIfThird12(number),
	# 			    'firstColumn': self.determineIfFirstColumn(number),
	# 			    'secondColumn': self.determineIfSecondColumn(number),
	# 			    'thirdColumn': self.determineIfThirdColumn(number),
	# 			}
	# 			self.board.append(dict)

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
		# self.board.insert(0,'00')

players = Players()
game = Game()
