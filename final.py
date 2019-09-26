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
            player.setInOrOutBet()

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
        self.betTypeChoice = None
        self.outsideBetId = None
        self.insideBetCategory = None
        self.insideBetChoice = None

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

    def setInOrOutBet(self):
        self.betTypeChoice = None
        if self.roundSkipStreak == 0:
            print('\n------------------------------------------------------------------')
            print(f'{self.name}, Choose your bet type')
        while self.betTypeChoice not in (str(i) for i in range(1,3)):
            self.betTypeChoice = input('Enter 1 to make an INSIDE Bet - Enter 2 to make an OUTSIDE bet: ')
        if self.betTypeChoice == '1':
            self.setInsideBetType()
        else:
            self.setOutsideBet()

    def setInsideBetType(self):
        self.insideBetCategory = None
        #Inner bet will depend on roullete type
        if isinstance(game.roulette, AmericanRoulette):
            while self.insideBetCategory not in (str(i) for i in range(1,8)):
                self.insideBetCategory = input('\n1 - Straight/Line\n2 - Split\n3 - Street\n4 - Corner/Square\n5 - Six Line/Double Street\n6 - Trio\n7 - Basket\nWhat type of inside bet you want to make? ')
                if self.insideBetCategory not in (str(i) for i in range(1,8)):
                    print('\nYou need to select your bet category by typing a interger (1-7)')
            #Straight/Single
            if self.insideBetCategory == '1':
                #Display options
                # x = [number['id'] for number in game.roulette.board]
                # print(x)
                pass
                #Make choice
            #Split
            elif self.insideBetCategory == '2':
                #Display Options
                insideBetChoices.displayOptions(insideBetChoices.splits)
                choice = input('Choose your bet: ')
                #Make Choice
            #Street
            elif self.insideBetCategory == '3':
                insideBetChoices.displayOptions(insideBetChoices.streets)
            #Corner/Square
            elif self.insideBetCategory == '4':
                insideBetChoices.displayOptions(insideBetChoices.squares)
            #Six Line/Double Street
            elif self.insideBetCategory == '5':
                insideBetChoices.displayOptions(insideBetChoices.doubleStreets)
                choice = input('Choose your bet: ')
            #Trio (american)
            elif self.insideBetCategory == '6':
                pass
            #Baskets
            else:
                pass
        elif isinstance(game.roulette, EuropeanRoulette):
            while self.insideBetCategory not in (str(i) for i in range(1,8)):
                self.insideBetCategory = input('\n1 - Straight/Line\n2 - Split\n3 - Street\n4 - Corner/Square\n5 - Six Line/Double Street\n6 - Trio\n7 - First Four\nWhat type of inside bet you want to make? ')
                if self.insideBetCategory not in (str(i) for i in range(1,8)):
                    print('\nYou need to select your bet category by typing a interger (1-7)')
            #Straight/Single
            if self.insideBetCategory == '1':
                pass
            #Split
            elif self.insideBetCategory == '2':
                insideBetChoices.displayOptions(insideBetChoices.splits)

            #Street
            elif self.insideBetCategory == '3':
                insideBetChoices.displayOptions(insideBetChoices.streets)
            #Corner/Square
            elif self.insideBetCategory == '4':
                insideBetChoices.displayOptions(insideBetChoices.squares)
            #Six Line/Double Street
            elif self.insideBetCategory == '5':
                insideBetChoices.displayOptions(insideBetChoices.doubleStreets)
            #Trio (american)
            elif self.insideBetCategory == '6':
                pass
            #First Four
            else:
                pass
        else:
            while self.insideBetCategory not in (str(i) for i in range(1,8)):
                self.insideBetCategory = input('\n1 - Straight/Line\n2 - Split\n3 - Street\n4 - Corner/Square\n5 - Six Line/Double Street\n6 - Trio\n7 - First Four\nWhat type of inside bet you want to make? ')
                if self.insideBetCategory not in (str(i) for i in range(1,8)):
                    print('\nYou need to select your bet category by typing a interger (1-7)')
            #Straight/Single
            if self.insideBetCategory == '1':
                pass
            #Split
            elif self.insideBetCategory == '2':
                insideBetChoices.displayOptions(insideBetChoices.splits)
            #Street
            elif self.insideBetCategory == '3':
                insideBetChoices.displayOptions(insideBetChoices.streets)
            #Corner/Square
            elif self.insideBetCategory == '4':
                insideBetChoices.displayOptions(insideBetChoices.squares)
            #Six Line/Double Street
            elif self.insideBetCategory == '5':
                insideBetChoices.displayOptions(insideBetChoices.doubleStreets)
            #Trio (american)
            elif self.insideBetCategory == '6':
                pass
            #First Four
            else:
                pass


    def setOutsideBet(self):
        self.outsideBetId = None
        while self.outsideBetId not in (str(i) for i in range(1,13)):
            print('\n------------------------------------------------------------------')
            self.outsideBetId = input("\n1-Red\n2-Black\n3-Even\n4-Odd\n5-One to Eighteen\n6-Eighteen to Thirty-Six\n7-First 12\n8-Second 12\n9-Third 12\n10-Column 1\n11-Column 2\n12-Column 3\n+-+-+- Select bet category: ")

class Roulette:
    def __init__(self):
        self.sortedNumber = None
        self.bank = 1000
        self.board = self.setBoard()


    def setBoard(self):
        self.board = []
        for number in range(1,37):
            self.board.append(
                {
                    'id': str(number),
                    'even': self.determineIfEven(number),
                    'red': self.determineIfRed(number),
                    'lessOrEqual18': self.determineIfLessOrEqualThan18(number),
                    'firstTwelve':  self.determineIfFirst12(number),
                    'secondTwelve': self.determineIfSecond12(number),
                    'thirdTwelve': self.determineIfThird12(number),
                    'firstColumn': self.determineIfFirstColumn(number),
                    'secondColumn': self.determineIfSecondColumn(number),
                    'thirdColumn': self.determineIfThirdColumn(number)
                }
            )
        self.board.insert(0,
            {
                'id': '0',
                'even': False,
                'red': False,
                'lessOrEqual18': False,
                'firstTwelve':  False,
                'secondTwelve': False,
                'thirdTwelve': False,
                'firstColumn': False,
                'secondColumn': False,
                'thirdColumn': False
            }
        )
        return self.board

    def determineIfEven(self,number):
        if number % 2 == 0:
            return True
        return False

    def determineIfRed(self,number):
        if number in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]:
            return True
        return False

    def determineIfLessOrEqualThan18(self,number):
        if number <= 18:
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
        if 25<=number:
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

class AmericanRoulette(Roulette):
    def __init__(self):
        super().__init__()
        self.board.insert(0,
            {
                'id': '00',
                'even': False,
                'red': False,
                'lessOrEqual18': False,
                'firstTwelve':  False,
                'secondTwelve': False,
                'thirdTwelve': False,
                'firstColumn': False,
                'secondColumn': False,
                'thirdColumn': False
            }
        )

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

class InsideBetChoices:
    def __init__(self):
        self.splits = [[1,2],[2,3],[4,5],[5,6],[7,8],[8,9],[10,11],[11,12],[13,14],[14,15],[16,17],[17,18],[19,20],[20,21],[22,23],[23,24],[25,26],[26,27],[28,29],[29,30],[31,32],[32,33],[34,35],[35,36],[1,4],[4,7],[7,10],[10,13],[13,16],[19,22],[22,25],[25,28],[28,31],[31,34],[2,5],[5,8],[8,11],[11,14],[14,17],[17,20],[20,23],[23,26],[26,29],[29,32],[32,35],[3,6],[6,9],[9,12],[12,15],[15,18],[18,21],[21,24],[24,27],[27,30],[30,33],[33,36]]
        self.streets = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,20,21],[22,23,24],[25,26,27],[28,29,30],[31,32,33],[34,35,36]]
        self.squares = [[1,2,4,5],[2,3,5,6],[4,7,5,8],[5,6,7,9],[7,8,10,11],[8,9,11,12],[10,11,13,14],[11,12,14,15],[13,14,16,17],[14,15,17,18],[16,17,19,20],[17,18,20,21],[19,20,22,23],[20,21,23,24],[22,23,25,26],[23,24,26,27],[25,26,28,29],[26,27,29,30],[28,29,31,31],[29,30,32,33],[31,32,34,35],[32,33,35,36]]
        self.doubleStreets = [[1,2,3,4,5,6],[4,5,6,7,8,9],[7,8,9,10,11,12],[10,11,12,13,14,15],[13,14,15,16,17,18],[16,17,18,19,20,21],[19,20,21,22,23,24],[22,23,24,25,26,27],[25,26,27,28,29,30],[28,29,30,31,32,33],[31,32,33,34,35,36]]

    def displayOptions(self,list):
        i = 0
        print('\nThis are your options\n')
        for group in list:
            print(f'{i}: {group}')
            i+=1


insideBetChoices = InsideBetChoices()

game = Game()
game.runGame()
