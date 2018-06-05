from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))
__package__ = "source"

import unittest
from source.Card import Card

class CardTest(unittest.TestCase):
    def testCard(self):
        card = Card("Spades",(1, "Ace"))
        self.assertEqual(card.value, 1)
        self.assertEqual(card.suit, "Spades")
        self.assertEqual(card.valueName, "Ace")

    def testEquals(self):
        card1 = Card("Spades",(1, "Ace"))
        card2 = Card("Spades",(1, "Ace"))
        self.assertEquals(card1,card2)
        self.assertEquals(hash(card1),hash(card2))

    def testNotEquals(self):
        card1 = Card("Spades",(1, "Ace"))
        card2 = Card("Spades",(2, "Two"))
        self.assertNotEqual(card1,card2)
        self.assertNotEqual(hash(card1),hash(card2))


if __name__ == '__main__':
    unittest.main()
