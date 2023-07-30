# Dealer object

from Hand import Hand

class Dealer:
    def __init__(self, standSoft17):
        self.standSoft17 = standSoft17
        self.hand = Hand([], 0)

    # Deal out the initial face up and face down cards
    def dealThemselves(self, deck):
        self.hand.addCards(deck.dealCards(2))

    def addCards(self, cards):
        self.hand.addCards(cards)

    # Return if the dealer needs to draw another card
    def needsToHit(self):
        val = self.hand.getHandVal()

        if val < 17:
            return True
        elif val > 17:
            return False
        else:
            return self.hand.isSoft() and not self.standSoft17

    def hit(self, deck):
        self.hand.addCards(deck.dealCards(1))

    def clearHand(self):
        self.hand = Hand([], 0)

    # Get the dealer's face-up card
    def getShowingCard(self):
        return self.hand.cards[0]
        
