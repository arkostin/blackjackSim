# Card object

class Card:

    suitNameMap = {"S":"Spades", "C":"Clubs", "D":"Diamonds", "H":"Hearts"}

    def __init__(self,suit,name):
        self.suit = suit
        self.name = name
    
    def getCardStr(self):
        return (self.name + " of " + self.suitNameMap[self.suit])

    def printCard(self):
        print(self.getCardStr())