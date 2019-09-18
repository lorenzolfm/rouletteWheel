import random

class Game:
    def __init__(self):
        self.roulette = settings.setRoulette()
        self.players = settings.setPlayers()

    def runGame(self):
        self.setBets()

    def setBets(self):
        while True:
            for player in self.players:
                player.setBetAmmount()
                player.setBetType()

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
        return self.instantiatePlayers()

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
            while not name.strip():
                print('\n You must enter a name! \n')
                name = input(f"+- Player {player}, enter your name: ")
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
        self.roundSkipStreak = 0
        self.pot = 100
        self.betAmmount = 0

    def __repr__(self):
        return f'{self.name}'

    def setBetAmmount(self):
        self.betAmmount = None
        while self.betAmmount not in (str(i) for i in range(0,self.pot+1)):
            print('\n--------------------------------------------------------')
            self.betAmmount = input(f"Player: {self.name}\nPot: {self.pot}\nHow much you wanna bet? (enter 0 to skip this round): ")
            print('--------------------------------------------------------\n')
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
            self.pot -=  self.betAmmount
            if self.roundSkipStreak != 0:
                self.roundSkipStreak = 0

    def setBetType(self):
        self.betTypeChoice = None
        if self.roundSkipStreak == 0:
            print('\n------------------------------------------------------------------')
            print(f'{self.name}, Choose your bet type')
        while self.betTypeChoice not in ['1','2']:
            self.betTypeChoice = input('Enter 1 to make an INNER Bet - Enter 2 to make an OUTSIDE bet: ')
        if self.betTypeChoice == '1':
            self.setInnerBet()

    def setInnerBet(self):
        self.betId = None
        #Aqui tem que ter a condicao do tabuleiro americano com 00
        #HSelect on how many numbers you're gonna bet on
            #Based on previous choice, display options
            #Choose
        while self.betId not in (str(i) for i in range(0,37)):
            self.betId = input('\nSelect a number between 0 and 36: ')
            print('------------------------------------------------------------------\n')


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
game.runGame()
