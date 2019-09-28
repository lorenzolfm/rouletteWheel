import random
#La partage and En prison only affects even bets
#La partage:  if sorted = 0 and no winner:
                #take half of the money of each player for the bank (if bet is even)
                #give back the other half to each player
#En prison:   if sorted = 0 and no winner:
                #If bet is even
                #Play again
                #If wins:
                    #Give back bet
                #else:
                    #take bet money
class Game:
    #Game is composed of player(s) and a Roulette child class (american,european,french)
    def __init__(self):
        self.settings = Settings()
        self.roulette = None
        self.players = []
        self.sortedNumber = None
        self.playersPlayingRound = []

    def runGame(self):
        run = True
        while run:
            self.displayIntro()
            self.setRoulette()
            self.setPlayers()
            while self.players != []:
                self.sortNumber()
                self.setBets()
                self.checkBets()
                self.displayResults()
                if self.roulette.bank <= 0 :
                    print("Oh no, your out of money. Thanks for playing")
                    self.players = []
                    run = False
                self.resetAttrs()


    def displayIntro(self):
        print('\n------------------------------------------------')
        print("+-+-+- Welcome to Bash Terminal Casino!-+-+-+\n+-+-+- Let's play a Roulette Game!-+-+-+\n")
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

    def sortNumber(self):
        self.sortedNumber = random.choice(self.roulette.board)
        print(self.sortedNumber)

    def checkBets(self):
        for player in self.playersPlayingRound:
            if player.isInsideBet:
                if self.sortedNumber['id'] in player.insideBet:
                    player.pot += player.betMultiplier*player.betAmmount + player.betAmmount
                    self.roulette.bank -= player.betMultiplier*player.betAmmount
                else:
                    self.roulette.bank += player.betAmmount
            else:
                pass
                if player.outsideBetId == '1':
                    if self.sortedNumber['red'] == True:
                        player.pot += player.betMultiplier*player.betAmmount + player.betAmmount
                        self.roulette.bank -= player.betMultiplier*player.betAmmount
                    else:
                        self.roulette.bank += player.betAmmount
                elif player.outsideBetId == '2':
                    if self.sortedNumber['red'] == False:
                        player.pot += player.betMultiplier*player.betAmmount + player.betAmmount
                        self.roulette.bank -= player.betMultiplier*player.betAmmount
                    else:
                        self.roulette.bank += player.betAmmount
                elif player.outsideBetId == '3':
                    if self.sortedNumber['even'] == True:
                        player.pot += player.betMultiplier*player.betAmmount + player.betAmmount
                        self.roulette.bank -= player.betMultiplier*player.betAmmount
                    else:
                        self.roulette.bank += player.betAmmount
                elif player.outsideBetId == '4':
                    if self.sortedNumber['even'] == False:
                        player.pot += player.betMultiplier*player.betAmmount + player.betAmmount
                        self.roulette.bank -= player.betMultiplier*player.betAmmount
                    else:
                        self.roulette.bank += player.betAmmount
                elif player.outsideBetId == '5':
                    if self.sortedNumber['lessOrEqual18'] == True:
                        player.pot += player.betMultiplier*player.betAmmount + player.betAmmount
                        self.roulette.bank -= player.betMultiplier*player.betAmmount
                    else:
                        self.roulette.bank += player.betAmmount
                elif player.outsideBetId == '6':
                    if self.sortedNumber['lessOrEqual18'] == False:
                        player.pot += player.betMultiplier*player.betAmmount + player.betAmmount
                        self.roulette.bank -= player.betMultiplier*player.betAmmount
                    else:
                        self.roulette.bank += player.betAmmount
                elif player.outsideBetId == '7':
                    if self.sortedNumber['firstTwelve'] == True:
                        player.pot += player.betMultiplier*player.betAmmount + player.betAmmount
                        self.roulette.bank -= player.betMultiplier*player.betAmmount
                    else:
                        self.roulette.bank += player.betAmmount
                elif player.outsideBetId == '8':
                    if self.sortedNumber['secondTwelve'] == True:
                        player.pot += player.betMultiplier*player.betAmmount + player.betAmmount
                        self.roulette.bank -= player.betMultiplier*player.betAmmount
                    else:
                        self.roulette.bank += player.betAmmount
                elif player.outsideBetId == '9':
                    if self.sortedNumber['thirdTwelve'] == True:
                        player.pot += player.betMultiplier*player.betAmmount + player.betAmmount
                        self.roulette.bank -= player.betMultiplier*player.betAmmount
                    else:
                        self.roulette.bank += player.betAmmount
                elif player.outsideBetId == '10':
                    if self.sortedNumber['firstColumn'] == True:
                        player.pot += player.betMultiplier*player.betAmmount + player.betAmmount
                        self.roulette.bank -= player.betMultiplier*player.betAmmount
                    else:
                        self.roulette.bank += player.betAmmount
                elif player.outsideBetId == '11':
                    if self.sortedNumber['secondColumn'] == True:
                        player.pot += player.betMultiplier*player.betAmmount + player.betAmmount
                        self.roulette.bank -= player.betMultiplier*player.betAmmount
                    else:
                        self.roulette.bank += player.betAmmount
                else:
                    if self.sortedNumber['thirdColumn'] == True:
                        player.pot += player.betMultiplier*player.betAmmount + player.betAmmount
                        self.roulette.bank -= player.betMultiplier*player.betAmmount
                    else:
                        self.roulette.bank += player.betAmmount

    def displayResults(self):
        print('\n------------------------------------------------')
        print(f'Money in casino bank: R${self.roulette.bank}')
        for player in self.players:
            print(f'Player: {player.name}; Pot {player.pot}; Remaining skips: {3 - player.roundSkipStreak}')
        print('------------------------------------------------\n')


    def resetAttrs(self):
        for player in self.players:
            player.betAmmount = None
            player.outsideBetId = None
            player.betTypeChoice = None
            player.insideBetCategory = None
            player.insideBet = None
            player.insideBetChoice = None
            player.isInsideBet = False
            player.betMultiplier = None
        self.playersPlayingRound = []

    # def doPayments(self):
    #     pass

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
    def __init__(self,name):
        self.name = name
        self.roundSkipStreak = 0
        self.pot = 100
        self.betAmmount = None
        self.betTypeChoice = None
        self.outsideBetId = None
        self.insideBetCategory = None
        self.insideBetChoice = None
        self.insideBet = None
        self.isInsideBet = False
        self.betMultiplier = None

    def  __repr__(self):
        return f'{self.name}'

    def setBetAmmount(self):
        if self.pot <= 0:
            game.players.remove(self)
            print(f'Player {self.name} removed from game')
        else:
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
                game.playersPlayingRound.append(self)
                print(game.playersPlayingRound)
                self.betAmmount = int(self.betAmmount)
                self.pot -= self.betAmmount
                if self.roundSkipStreak != 0:
                    self.roundSkipStreak = 0

    def setInOrOutBet(self):
        if self.roundSkipStreak == 0 and self in game.playersPlayingRound:
            print('\n------------------------------------------------------------------')
            print(f'{self.name}, Choose your bet type')
            while self.betTypeChoice not in (str(i) for i in range(1,3)):
                self.betTypeChoice = input('Enter 1 to make an INSIDE Bet - Enter 2 to make an OUTSIDE bet: ')
            if self.betTypeChoice == '1':
                self.setInsideBet()
            else:
                self.setOutsideBet()

    def setInsideBet(self):
        self.isInsideBet = True
        if isinstance(game.roulette, AmericanRoulette):
            self.setInsideBetType()
            self.setInsideGeneralBet()
        elif isinstance(game.roulette, EuropeanRoulette):
            self.setInsideBetType()
            self.setInsideGeneralBet()
        else:
            self.setInsideBetType()
            self.setInsideGeneralBet()

    def setInsideBetType(self):
        if isinstance(game.roulette, AmericanRoulette):
            while self.insideBetCategory not in (str(i) for i in range(1,8)):
                self.insideBetCategory = input('\n1 - Straight/Line\n2 - Split\n3 - Street\n4 - Corner/Square\n5 - Six Line/Double Street\n6 - Trio\n7 - First Four\nWhat type of inside bet you want to make? ')
                if self.insideBetCategory not in (str(i) for i in range(1,8)):
                    print('\nYou need to select your bet category by typing a interger (1-7)')
        else:
            while self.insideBetCategory not in (str(i) for i in range(1,7)):
                self.insideBetCategory = input('\n1 - Straight/Line\n2 - Split\n3 - Street\n4 - Corner/Square\n5 - Six Line/Double Street\n6 - Trio\nWhat type of inside bet you want to make? ')
                if self.insideBetCategory not in (str(i) for i in range(1,7)):
                    print('\nYou need to select your bet category by typing a interger (1-6)')


    def setInsideGeneralBet(self):
        if self.insideBetCategory == '1':
            options = [number['id'] for number in game.roulette.board]
            for i in options:
                print(i)
            while self.insideBet not in options:
                self.insideBet = input('Type the number you want to bet on: ')
            self.insideBet = [self.insideBet]
            self.betMultiplier = 35
            #Delete the print statements
            print(f'Multiplier: {self.betMultiplier}')
            print(self.insideBet)
        elif self.insideBetCategory == '2':
            insideBetChoices.displayOptions(insideBetChoices.splits)
            while self.insideBetChoice not in (str(i) for i in range(56)):
                self.insideBetChoice = input('Choose the Split: ')
            self.insideBet = insideBetChoices.splits[int(self.insideBetChoice)]
            self.betMultiplier = 17
            print(self.insideBet)
        elif self.insideBetCategory == '3':
            insideBetChoices.displayOptions(insideBetChoices.streets)
            while self.insideBetChoice not in (str(i) for i in range(12)):
                self.insideBetChoice = input('Choose the Trio: ')
            self.insideBet = insideBetChoices.streets[int(self.insideBetChoice)]
            self.betMultiplier = 11
            print(self.insideBet)
        elif self.insideBetCategory == '4':
            insideBetChoices.displayOptions(insideBetChoices.squares)
            while self.insideBetChoice not in (str(i) for i in range(22)):
                self.insideBetChoice = input('Choose the Square: ')
            self.insideBet = insideBetChoices.squares[int(self.insideBetChoice)]
            self.betMultiplier = 8
            print(self.insideBet)
        elif self.insideBetCategory == '5':
            insideBetChoices.displayOptions(insideBetChoices.doubleStreets)
            while self.insideBetChoice not in (str(i) for i in range(11)):
                self.insideBetChoice = input('Choose a Double Street: ')
            self.insideBet = insideBetChoices.doubleStreets[int(self.insideBetChoice)]
            self.betMultiplier = 5
            print(self.insideBet)
        elif self.insideBetCategory == '6':
            choice = 0
            if isinstance(game.roulette, AmericanRoulette):
                while choice not in (str(i) for i in range(1,4)):
                    choice = input('\n1 - [0,1,2]\n2 - [0,2,3]\n3 - [00,2,3]\nChoose: ')
                self.betMultiplier = 12
                if choice == '1':
                    self.insideBet = ['0','1','2']
                elif choice == '2':
                    self.insideBet = ['0','2','3']
                else:
                    self.insideBet = ['00','2','3']
            else:
                while choice not in (str(i) for i in range(1,3)):
                    choice = input('\n1 - [0,1,2]\n2 - [0,2,3]\nChoose: ')
                self.betMultiplier = 12
                if choice == '1':
                    self.insideBet = ['0','1','2']
                else:
                    self.insideBet = ['0','2','3']

        else:
            if isinstance(game.roulette, AmericanRoulette):
                self.insideBet = ['0','00','1','2','3']
                gameroulette.multiplier = 6
            else:
                self.insideBet = ['0','1','2','3']
                self.betMultiplier = 8

    #Need to map function
    def setOutsideBet(self):
        while self.outsideBetId not in (str(i) for i in range(1,13)):
            print('\n------------------------------------------------------------------')
            self.outsideBetId = input("\n1-Red\n2-Black\n3-Even\n4-Odd\n5-One to Eighteen\n6-Eighteen to Thirty-Six\n7-First 12\n8-Second 12\n9-Third 12\n10-Column 1\n11-Column 2\n12-Column 3\n+-+-+- Select bet category: ")
        if int(self.outsideBetId) <= 6:
            self.betMultiplier = 1
        else:
            self.Multiplier = 2

class Roulette:
    def __init__(self):
        self.sortedNumber = None
        self.bank = 1000
        self.board = self.setBoard()
        self.multiplier = None

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
        #Set attribute for choosing between la partage and en prison rules

    def __repr__(self):
        return 'French Roulette'

class InsideBetChoices:
    def __init__(self):
        self.splits = [['1','2'],['2','3'],['4','5'],['5','6'],['7','8'],['8','9'],['10','11'],['11','12'],['13','14'],['14','15'],['16','17'],['17','18'],['19','20'],['20','21'],['22','23'],['23','24'],['25','26'],['26','27'],['28','29'],['29','30'],['31','32'],['32','33'],['34','35'],['35','36'],['1','4'],['4','7'],['7','10'],['10','13'],['13','16'],['19','22'],['22','25'],['25','28'],['28','31'],['31','34'],['2','5'],['5','8'],['8','11'],['11','14'],['14','17'],['17','20'],['20','23'],['23','26'],['26','29'],['29','32'],['32','35'],['3','6'],['6','9'],['9','12'],['12','15'],['15','18'],['18','21'],['21','24'],['24','27'],['27','30'],['30','33'],['33','36']]
        self.streets = [['1','2','3'],['4','5','6'],['7','8','9'],['10','11','12'],['13','14','15'],['16','17','18'],['19','20','21'],['22','23','24'],['25','26','27'],['28','29','30'],['31','32','33'],['34','35','36']]
        self.squares = [['1','2','4','5'],['2','3','5','6'],['4','7','5','8'],['5','6','7','9'],['7','8','10','11'],['8','9','11','12'],['10','11','13','14'],['11','12','14','15'],['13','14','16','17'],['14','15','17','18'],['16','17','19','20'],['17','18','20','21'],['19','20','22','23'],['20','21','23','24'],['22','23','25','26'],['23','24','26','27'],['25','26','28','29'],['26','27','29','30'],['28','29','31','32'],['29','30','32','33'],['31','32','34','35'],['32','33','35','36']]
        self.doubleStreets = [['1','2','3','4','5','6'],['4','5','6','7','8','9'],['7','8','9','10','11','12'],['10','11','12','13','14','15'],['13','14','15','16','17','18'],['16','17','18','19','20','21'],['19','20','21','22','23','24'],['22','23','24','25','26','27'],['25','26','27','28','290','30'],['28','29','30','31','32','33'],['31','32','33','34','35','36']]

    def displayOptions(self,list):
        i = 0
        print('\nThis are your options\n')
        for group in list:
            print(f'{i}: {[int(i) for i in group]}')
            i+=1


insideBetChoices = InsideBetChoices()

game = Game()
game.runGame()
