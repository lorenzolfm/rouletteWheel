import random

class Game:
    #Game is composed of player(s) and a Roulette child class (american,european,french)
    def __init__(self):
        pass

    def runGame(self):
        #While runGame
            #Define and instantiate roulette class
            #Define player number and instantiate player(s)
            #Sort number
            #For each player:
                #setBetAmmount
                #chooseBet
                #Check result
                #Transfer Money
        pass


class Settings:
    #Settings class is used to define game settings (i.e.: Number of players and roullete type)
    def __init__(self):
        pass

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

class EuropeanRoulette(Roulette):
    def __init__(self):
        super().__init__()

class FrenchRoulette(Roulette):
    def __init__(self):
        super().__init__()
