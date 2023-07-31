# Hand object

class Hand:
    nameToMinValMap = {str(i): i for i in range(2,11)}
    nameToMinValMap.update({i: 10 for i in ["J","Q","K"]})
    nameToMinValMap.update({"A":1})

    def __init__(self, cards):
        self.cards = cards

    def getDealt(self, deck):
        self.addCards(deck.dealCards(2))

    def addCards(self, cards):
        self.cards += cards
    
    def printHand(self):
        for card in self.cards:
            card.printCard()

    def getHandVal(self):
        val = 0
        numAces = 0

        # Iterate over the cards and get the value, counting aces as 1 and keeping track of how many aces.
        for card in self.cards:
            val += self.nameToMinValMap[card.name]
            if (card.name == "A"):
                numAces += 1

        # For each ace found, add 10 unless it gets us over 21
        while (val <= 11) and (numAces > 0):
            val += 10
            numAces -= 1
        
        return val

    def isSoft(self):
        val = 0
        numAces = 0

        # Iterate over the cards and get the value, counting aces as 1 and keeping track of how many aces.
        for card in self.cards:
            val += self.nameToMinValMap[card.name]
            if (card.name == "A"):
                numAces += 1

        return (val <= 11) and (numAces > 0)

    def isBust(self):
        return self.getHandVal() > 21

    def isPair(self):
        if(len(self.cards) != 2):
            return False

        return self.nameToMinValMap[self.cards[0].name] == self.nameToMinValMap[self.cards[1].name]
    
    def getStatName(self):
        if (self.isBust()):
            return "Bust"

        #if (self.isPair()):
        #    return "P" + self.cards[0].getCardValForStats()

        handVal = str(self.getHandVal())
        if (self.isSoft()):
            return "S" + handVal
        return handVal
