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
            self.setPlayers()
            while self.players != []:
                self.setBets()

                #check to see if remaining players still have any Money

    def displayIntro(self):
        print('\n------------------------------------------------')
        print("+-+-+- Welcome to Bash Terminal Cassino!-+-+-+\n+-+-+- Let's play a Roulette Game!-+-+-+\n")
        print("+- If you don't know how to play this game -+\n+- you can take a look at the readme.txt file -+\n+- for instructions and rules -+\n")
        print("+- You can press CTRL + D at any time to exit -+")
        print('------------------------------------------------\n')

    def setRoulette(self):
        self.settings.setRouletteType()
        self.instantiateRoulette()

    def setPlayers(self):
        self.settings.setNumberOfPlayers()
        self.instantiatePlayers()

    def setBets(self):
        for player in self.players:
            player.setBetAmmount()

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

    def instantiatePlayers(self):
        # self.players = []
        for player in range(1,self.settings.numberOfPlayers+1):
            name = input(f"+- Player {player}, enter your name: ")
            print('\n')
            while not name.strip():
                print(' \n+-+-+- You must enter a name! -+-+-+')
                name = input(f"+- Player {player}, enter your name: ")
            if self.settings.numberOfPlayers > 1:
                while name in (player.name for player in self.players):
                    name = ''
                    while not name.strip():
                        name = input(f'+-+-+- Name already registered -+-+-+\nPlease enter a different name for player {player}: ')
                        print('\n')
                self.players.append(Player(name))
            else:
                self.players.append(Player(name))


class Settings:
    #Settings class is used to define game settings (i.e.: Number of players and roullete type)
    def __init__(self):
        self.selectedRoulette = None
        self.numberOfPlayers = None

    def setRouletteType(self):
        while self.selectedRoulette not in (str(i) for i in range(1,4)):
            print('\n------------------------------------------------')
            self.selectedRoulette = input('+- 1-American Roulette -+\n+- 2-European Roueltte -+\n+- 3-French Roulette -+\nSelect game style: ')
            print('------------------------------------------------\n')
            if self.selectedRoulette not in ['1','2','3']:
                print('\n+- You must select the Roulette by typing 1, 2 or 3 -+\n')

    def setNumberOfPlayers(self):
        while self.numberOfPlayers not in (str(i) for i in range(1,11)):
            print('\n---------------------------------------------------')
            self.numberOfPlayers = input('+- Enter the number of players in this game (1-10): ')
            print('---------------------------------------------------\n')
            if self.numberOfPlayers not in (str(i) for i in range(1,11)):
                print('\nYou must select a number between 1 and 10\n')
        self.numberOfPlayers = int(self.numberOfPlayers)

class Player:
    #Player model
    def __init__(self,name):
        self.name = name
        self.roundSkipStreak = 0
        self.pot = 100
        self.betAmmount = None

    def  __repr__(self):
        return f'{self.name}'

    def setBetAmmount(self):
        self.betAmmount = None
        if self.pot <= 0:
            game.players.remove(self)
        while self.betAmmount not in (str(i) for i in range(0,self.pot+1)):
            print('\n--------------------------------------------------------')
            self.betAmmount = input(f"Player: {self.name}\nPot: {self.pot}\nHow much you wanna bet? (enter 0 to skip this round): ")
            if self.betAmmount not in (str(i) for i in range(0,self.pot+1)):
                print(f'+-+-+- Please enter a valid input. -+-+-+\n+-+-+- You must choose an integer between 0 and {self.pot} (integers only) -+-+-+\n')
        if self.betAmmount == '0':
            self.roundSkipStreak += 1
            if self.roundSkipStreak >= 3:
                game.players.remove(self)
                print('\n------------------------------------------------------------------')
                print(f"+-+-+- {self.name}, You're out! Skiped 3 rounds in a row! -+-+-+")
                print('------------------------------------------------------------------\n')
            else:
                print(f'+- {self.name} has chosen to skip this round -+\n+- Skips Left before removal: {3-self.roundSkipStreak} -+\n')
        else:
            self.betAmmount = int(self.betAmmount)
            self.pot -= self.betAmmount
            if self.roundSkipStreak != 0:
                self.roundSkipStreak = 0



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
