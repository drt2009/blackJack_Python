from sys import path
from os.path import dirname as dir

path.append(dir(path[0]))
__package__ = "source"

import unittest
from source.Card import Card

class CardTest(unittest.TestCase):
    def testCard(self):
        card = Card(1,"Spades","Ace")
        self.assertEqual(card.value, 1)
        self.assertEqual(card.suit, "Spades")
        self.assertEqual(card.valueName, "Ace")


if __name__ == '__main__':
    unittest.main()
