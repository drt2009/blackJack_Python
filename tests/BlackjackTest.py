from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))
__package__ = "source"

import unittest
from source.Blackjack import Blackjack
from source.Card import Card

class BlackjackTest(unittest.TestCase):

    def setUp(self):
        self.game = Blackjack()

    def testDealCard(self):
        card = self.game.dealCard()

        self.assertTrue(type(card) is Card)

    def testDealCards(self):
        cards = self.game.dealCards()
        self.assertEqual(len(cards), 2)
        #This test only works in a single deck game, but is needed to make sure
        #it is cycling thorugh cards
        self.assertNotEqual(cards[0], cards[1])

if __name__ == '__main__':
    unittest.main()
