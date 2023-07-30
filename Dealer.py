# Dealer object

from Hand import Hand

class Dealer:
    def __init__(self, standSoft17):
        self.standSoft17 = standSoft17
        self.hand = Hand([], 0)

    def addCards(self, cards):
        self.hand.addCards(cards)

    # Return if the dealer needs to draw another card
    def needsToHit(self):
        val = self.hand.getHandVal()

        if val < 17:
            return true
        elif val > 17:
            return false
        else:
            return hand.isSoft() and not self.standSoft17

    # Get the dealer's face-up card
    def getShowingCard(self):
        return self.hand.cards[0]
        
