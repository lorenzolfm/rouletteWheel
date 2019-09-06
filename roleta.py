#Nome dos players

class Game:
	def __init__(self):
		print("Welcome to Bash Cassino!\nLet's play a Roulette Game!")
		self.numberOfPlayers = input("Enter number of players: ")
		self.gameType = input('Select game style:\n1-American Roulette\n2-European Roueltte\n3-French Roulette')
		if self.gameType = '1':
			print(f'Ok! Loading the American Roulette')
	def createPlayers(self)


class Roulette:
	def __init__(self):
		self.board = [str(i) for i in range(0,37)]


class Players:
	def __init__(self):
		pass

class Player:
	def __init__(self):
		pass

class AmericanRoulette(Roulette):
	def __init__(self):
		super().__init__()


class EuropeanRoulette(Roulette):
	def __init__(self):
		super().__init__()
		
class FrenchRoulette(Roulette):
	def __init__(self):
		super().__init__()


game = Game()
print(game.board)
print(game.numberOfPlayers)