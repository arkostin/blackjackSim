from Deck import Deck
from Hand import Hand
from Dealer import Dealer
from time import sleep

deck = Deck(4, 0.75)
deck.shuffle()

NUM_ROUNDS = 1

# Init dealer
dealer = Dealer(False)

# Main game loop
for _ in range(NUM_ROUNDS):
    sleep(1)
    print("\n\n--- NEW ROUND ---")

    # Deal out initial cards
    playerHand = Hand([], 100)
    playerHand.getDealt(deck)
    dealer.dealThemselves(deck)

    # Print out hands
    sleep(1)
    print("Dealer's up card: " + dealer.getShowingCard().getCardStr())
    sleep(0.5)
    print("Your hand: ")
    playerHand.printHand()

    doneHitting = False
    # Get player input
    while (playerHand.getHandVal() < 21) and not doneHitting:
        sleep(0.5)
        choice = input("\nChoice (S/H/D/P/R): ").upper()
        if (choice == 'S'):
            doneHitting = True
        elif (choice == 'H'):
            card = deck.dealCards(1)[0]
            print("Dealt a " + card.getCardStr())
            playerHand.addCards([card])
        elif (choice == 'D'):
            card = deck.dealCards(1)[0]
            print("Dealt a " + card.getCardStr())
            playerHand.addCards([card])
            doneHitting = True
    
    # Check if busted
    if (playerHand.isBust()):
        print("Busted! You lose.")
        sleep(0.5)
        print("Dealer had a " + dealer.hand.cards[0].getCardStr() + " and a " + dealer.hand.cards[1].getCardStr())
    else:
        sleep(0.5)
        print("Dealer flips over a " + dealer.hand.cards[1].getCardStr())
        sleep(2)
        while (dealer.needsToHit()):
            card = deck.dealCards(1)[0]
            print("Dealer draws a " + card.getCardStr())
            dealer.addCards([card])
            sleep(1)
        if dealer.hand.isBust():
            print("Dealer busted, you win!")
        else:
            sleep(1)
            print("\nDealer final hand: ")
            dealer.hand.printHand()
            print("\nYour final hand: ")
            playerHand.printHand()

            dealerHandVal = dealer.hand.getHandVal()
            playerHandVal = playerHand.getHandVal()

            sleep(2)
            if dealerHandVal < playerHandVal:
                print("\nResult: You win!!!")
            elif dealerHandVal > playerHandVal:
                print("\nResult: You lose :(")
            else:
                print("\nResult: Push...")