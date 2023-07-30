from Deck import Deck
from Hand import Hand
from Dealer import Dealer

deck = Deck(4)
deck.shuffle()

'''
hand = Hand(deck.dealCards(2),100)
print("\nHand:")
hand.printHand()
print("Val: " + str(hand.getHandVal()) + "\n")
if(hand.isPair()):
    print("It's a pair!")

while(not hand.isBust()):
    dealtCard = deck.dealCards(1)
    hand.addCards(dealtCard)
    print("Dealt a " + dealtCard[0].getCardStr() + ", val: " + str(hand.getHandVal()))
    if(hand.isBust()):
        print("Busted!")
'''

dealer = Dealer(False)
playerHand = Hand(deck.dealCards(2), 100)
dealer.addCards(deck.dealCards(2))
print("Dealer hand: ")
dealer.hand.printHand()