# Player object

from Hand import Hand

class Player:
    def __init__(self, money):
        self.money = money
        self.hand = Hand([])

    def dealHand(self, deck):
        self.hand.addCards(deck.dealCards(2))
    
    def hit(self, deck):
        self.hand.addCards(deck.dealCards(1))

    def clearHand(self):
        self.hand = Hand([])