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


roleta = Roulette()
roletaAmericana = AmericanRoulette()
roletaEuropeia = EuropeanRoulette()
roletaFrancesa = FrenchRoulette()

x = [number['id'] for number in roletaAmericana.board]
print(x)

# for number in roletaAmericana.board:
#     print(number['id'])
# bet = None
# while bet not in (number['id'] for number in roletaAmericana.board):
#     bet = input('Faça sua aposta istepo')
