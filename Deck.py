# Deck object 

import random
from Card import Card

class Deck:
    def __init__(self, numDecks, shufflePct):
        # Declare vars
        self.cards = []
        self.numDecks = numDecks
        self.index = 0
        self.numCards = numDecks * 52
        self.shufflePct = shufflePct

        # Create the shoe. For each deck, name, and suit, add that card to the shoe.
        for i in range(numDecks):
            for name in [str(num) for num in range(2,11)] + ["J","Q","K","A"]:
                for suit in ["S","C","D","H"]:
                    self.cards.append(Card(suit, name))
    
    def printDeck(self):
        for card in self.cards:
            card.printCard()

    # Returns whether or not the deck needs to be shuffled
    def needsShuffle(self):
        return (self.shufflePct * self.numCards) <= self.index

    def shuffle(self):
        # Shuffle the deck by iterating over each card and swapping it with a card in the range [card, end of deck]
        for i in range(self.numCards):
            j = random.randrange(i, self.numCards)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]
        self.index = 0

    def dealCards(self, numCardsToDeal):
        # Safety check
        if (self.index + numCardsToDeal > self.numCards):
            return []

        # Create an array and put in the number of cards requested, updating our index in the deck
        cardArr = []
        for i in range(numCardsToDeal):
            cardArr.append(self.cards[self.index])
            self.index += 1
        
        return cardArr