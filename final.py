import random

class Game:
    #Game is composed of player(s) and a Roulette child class (american,european,french)
    def __init__(self):
        self.settings = Settings()
        self.roulette = None
        self.players = []

    def runGame(self):
        run = True
        #While runGame
            #Define player number and instantiate player(s)
            #Sort number
            #For each player:
                #setBetAmmount
                #chooseBet
                #Check result
                #Transfer Money
        while run:
            self.displayIntro()
            self.setRoulette()
            # self.setPlayers()

    def displayIntro(self):
        print('\n------------------------------------------------')
        print("+-+-+- Welcome to Bash Terminal Cassino!-+-+-+\n+-+-+- Let's play a Roulette Game!-+-+-+\n")
        print("+- If you don't know how to play this game -+\n+- you can take a look at the readme.txt file -+\n+- for instructions and rules -+\n")
        print("+- You can press CTRL + D at any time to exit -+")
        print('------------------------------------------------\n')

    def setRoulette(self):
        self.settings.setRouletteType()
        self.instantiateRoulette()


    def instantiateRoulette(self):
        if self.settings.selectedRoulette == '1':
            print(f'\n+-+-+- Ok! Loading the American Roulette -+-+-+\n')
            self.roulette = AmericanRoulette()
        elif self.settings.selectedRoulette == '2':
            print(f'\n+-+-+- Ok! Loading the European Roulette -+-+-+\n')
            self.roulette = EuropeanRoulette()
        else:
            print(f'\n+-+-+- Ok! Loading the French Roulette -+-+-+\n')
            self.roulette = FrenchRoulette()

class Settings:
    #Settings class is used to define game settings (i.e.: Number of players and roullete type)
    def __init__(self):
        self.selectedRoulette = None
        self.numberOfPlayers = None

    def setRouletteType(self):
        while self.selectedRoulette not in ['1','2','3']:
            print('\n------------------------------------------------')
            self.selectedRoulette = input('+- 1-American Roulette -+\n+- 2-European Roueltte -+\n+- 3-French Roulette -+\nSelect game style: ')
            print('------------------------------------------------\n')
            if self.selectedRoulette not in ['1','2','3']:
                print('\n+- You must select the Roulette by typing 1, 2 or 3 -+\n')


class Player:
    #Player model
    def __init__(self):
        pass

class Roulette:
    def __init__(self):
        pass

class AmericanRoulette(Roulette):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return 'American Roulette'

class EuropeanRoulette(Roulette):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return 'European Roulette'

class FrenchRoulette(Roulette):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return 'French Roulette'

game = Game()
game.runGame()
