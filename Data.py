# Data class

import numpy as np

class Data:
    def __init__(self):
        # Create possible player and dealer hands/cards
        self.playerHands = [str(val) for val in range(4,21)]
        self.playerHands += ["S" + str(val) for val in range(12,21)]
        #playerHands += ["P" + str(val) for val in range(2,11)]
        #playerHands += ["PA"]

        self.dealerCards = [str(val) for val in range(2,11)] + ["A"]

        # Create maps from player hand/dealer card to indices in results array
        self.playerHandsMap = {self.playerHands[i]: i for i in range(len(self.playerHands))}
        self.dealerCardsMap = {self.dealerCards[i]: i for i in range(len(self.dealerCards))}

        self.resultsArr = np.zeros((len(self.playerHands), len(self.dealerCards), 3, 4))
    
    # Increments a result
    def addResult(self, playerHand, dealerCard, action, result):
        self.resultsArr[self.playerHandsMap[playerHand]][self.dealerCardsMap[dealerCard]][action][3] += 1
        self.resultsArr[self.playerHandsMap[playerHand]][self.dealerCardsMap[dealerCard]][action][result] += 1

    # Compare the values of the player and dealer hands and return the result
    #   0 - Player wins
    #   1 - Push
    #   2 - Dealer wins
    def compareHandsAndGetResult(self, playerHandVal, dealerHandVal):
        if playerHandVal > 21:
            return 2
        elif dealerHandVal > 21:
            return 0

        if playerHandVal > dealerHandVal:
            return 0
        elif playerHandVal < dealerHandVal:
            return 2
        else:
            return 1

    # Given the player's starting hand, dealer's up-card, player hand, dealer hand, and action, gets the result and logs it to the results array.
    def compareHandsAndLogResult(self, playerHandName, dealerCard, playerHandVal, dealerHandVal, action):
        result = self.compareHandsAndGetResult(playerHandVal, dealerHandVal)

        self.addResult(playerHandName, dealerCard, action, result)

    def printResults(self):
        print("    " + "".join([dealerCard + " " * (7 - len(dealerCard)) for dealerCard in self.dealerCards]))
        for playerHand in self.playerHands:
            self.printRow(playerHand)

    def printRow(self, playerHand):
        for action in range(2):
            if action == 0:
                print(playerHand + (" " * (4 - len(playerHand))), end='')
            else:
                print(" " * 4, end='')

            for dealerCard in self.dealerCards:
                standResults = self.resultsArr[self.playerHandsMap[playerHand]][self.dealerCardsMap[dealerCard]][action]
                standPercentage = "{0:.2f}".format(round((standResults[0] / (standResults[3] - standResults[1])) * 100, 2))
                print(standPercentage + (" " * (7 - len(standPercentage))), end='')

            print()
        print()