import random

class Game:
    def __init__(self):
        self.roulette = settings.instantiateRoulette()
        self.players = settings.instantiatePlayers()

    def runGame(self):
        settings.instantiateRoulette()

class Settings:
    def __init__(self):
        pass

    def instantiateRoulette(self):
        selectedRoulette = 0
        while selectedRoulette not in ['1','2','3']:
            print('\n------------------------------------------------')
            selectedRoulette = input('+- 1-American Roulette -+\n+- 2-European Roueltte -+\n+- 3-French Roulette -+\nSelect game style: ')
            print('------------------------------------------------\n')
            if selectedRoulette == '1':
                print(f'\n+-+-+- Ok! Loading the American Roulette -+-+-+\n')
                return AmericanRoulette()
            elif selectedRoulette == '2':
                print(f'\n+-+-+- Ok! Loading the European Roulette -+-+-+\n')
                return EuropeanRoulette()
            elif selectedRoulette == '3':
                print(f'\n+-+-+- Ok! Loading the French Roulette -+-+-+\n')
                return FrenchRoulette()

    def instantiatePlayers(self):
        numberOfPlayers = 0
        while numberOfPlayers not in (i for i in range(1,11)):
            print('\n---------------------------------------------------')
            numberOfPlayers = input('+- Enter the number of players in this game (1-10): ')
            print('---------------------------------------------------\n')
            if numberOfPlayers in (str(i) for i in range(1,11)):
                numberOfPlayers = int(numberOfPlayers)
                players = []
                for player in range(1,numberOfPlayers+1):
                    name = input(f"+- Player {player}, enter your name: ")
                    print('\n')
                    if numberOfPlayers > 1:
                        while name in [player.name for player in players]:
                            name = input(f'+-+-+- Name already registered -+-+-+\nPlease enter a different name for player {player}: ')
                            print('\n')
                        players.append(Player(name))
                    else:
                        players.append(Player(name))
            else:
                print('\nYou must select a number between 1 and 10\n')
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
