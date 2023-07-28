# Card object

class Card:

    suitNameMap = {"S":"Spades", "C":"Clubs", "D":"Diamonds", "H":"Hearts"}

    def __init__(self,suit,name):
        self.suit = suit
        self.name = name

    def printCard(self):
        print(self.name + " of " + self.suitNameMap[self.suit])