import random

class Game:
    def __init__(self):
        self.roulette = settings.setRoulette()
        self.players = settings.setPlayers()

    def runGame(self):
        settings.instantiateRoulette()

class Settings:
    def __init__(self):
        self.selectedRoulette = 0
        self.numberOfPlayers = 0

    def setRoulette(self):
        self.setRouletteType()
        self.instantiateRoulette()

    def setRouletteType(self):
        while self.selectedRoulette not in ['1','2','3']:
            print('\n------------------------------------------------')
            self.selectedRoulette = input('+- 1-American Roulette -+\n+- 2-European Roueltte -+\n+- 3-French Roulette -+\nSelect game style: ')
            print('------------------------------------------------\n')
            if self.selectedRoulette not in ['1','2','3']:
                print('\n+- You must select the Roulette by typing 1, 2 or 3 -+\n')

    def instantiateRoulette(self):
        if self.selectedRoulette == '1':
            print(f'\n+-+-+- Ok! Loading the American Roulette -+-+-+\n')
            return AmericanRoulette()
        elif self.selectedRoulette == '2':
            print(f'\n+-+-+- Ok! Loading the European Roulette -+-+-+\n')
            return EuropeanRoulette()
        elif self.selectedRoulette == '3':
            print(f'\n+-+-+- Ok! Loading the French Roulette -+-+-+\n')
            return FrenchRoulette()

    def setPlayers(self):
        self.setNumberOfPlayers()
        self.instantiatePlayers()

    def setNumberOfPlayers(self):
        while self.numberOfPlayers not in (str(i) for i in range(1,11)):
            print('\n---------------------------------------------------')
            self.numberOfPlayers = input('+- Enter the number of players in this game (1-10): ')
            print('---------------------------------------------------\n')
            if self.numberOfPlayers not in (str(i) for i in range(1,11)):
                print('\nYou must select a number between 1 and 10\n')

    def instantiatePlayers(self):
        self.numberOfPlayers = int(self.numberOfPlayers)
        players = []
        for player in range(1,self.numberOfPlayers+1):
            name = input(f"+- Player {player}, enter your name: ")
            print('\n')
            if self.numberOfPlayers > 1:
                while name in [player.name for player in players]:
                    name = input(f'+-+-+- Name already registered -+-+-+\nPlease enter a different name for player {player}: ')
                    print('\n')
                players.append(Player(name))
            else:
                players.append(Player(name))
        return players

class Player:
    def __init__(self,name):
        self.name = name
        self.roundSkipedStreak = 0
        self.pot = 100
        self.betAmmount = 0

    def __repr__(self):
        return f'{self.name}'

class Roulette:
    def __init__(self):
        pass

class EuropeanRoulette(Roulette):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f'\n+-+-+- Ok! Loading the European Roulette -+-+-+\n'

class AmericanRoulette(Roulette):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f'\n+-+-+- Ok! Loading the American Roulette -+-+-+\n'

class FrenchRoulette(Roulette):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return f'\n+-+-+- Ok! Loading the French Roulette -+-+-+\n'

settings = Settings()
game = Game()
