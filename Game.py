# Blackjack basic strategy simulator

import random

from Deck import Deck
from Hand import Hand
from Dealer import Dealer
from Player import Player
from Data import Data

data = Data()

deck = Deck(4, 0.75)
deck.shuffle()

NUM_ROUNDS = 1000000

# Init dealer
dealer = Dealer(False)
player = Player(1000)

# Main game loop
for _ in range(NUM_ROUNDS):
    player.dealHand(deck)
    dealer.dealHand(deck)

    dealerUpCardVal = dealer.getShowingCard().getCardValForStats()

    if (dealer.hand.getHandVal() == 21 or player.hand.getHandVal() == 21):
        player.clearHand()
        dealer.clearHand()
        continue
    else:
        # Make a random choice, 0 - Stand, 1 - Hit, 2 - Double
        choice = random.randrange(0, 2)

        if (choice == 0):
            playerHandVal = player.hand.getHandVal()

            dealer.hitUntilDone(deck)
            dealerHandVal = dealer.hand.getHandVal()

            data.compareHandsAndLogResult(player.hand.getStatName(), dealerUpCardVal, playerHandVal, dealerHandVal, choice)
        else:
            playerHandName = player.hand.getStatName()
            player.hit(deck)

            dealer.hitUntilDone(deck)
            dealerHandVal = dealer.hand.getHandVal()

            data.compareHandsAndLogResult(playerHandName, dealerUpCardVal, player.hand.getHandVal(), dealerHandVal, choice)

    player.clearHand()
    dealer.clearHand()

    if (deck.needsShuffle()):
        deck.shuffle()

data.printResults()