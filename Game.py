from Deck import Deck
from Hand import Hand

deck = Deck(4)
deck.printDeck()
deck.shuffle()
deck.printDeck()

hand = Hand(deck.dealCards(3),100)
print("\nHand")
hand.printHand()
print("Val: " + str(hand.getHandVal()))