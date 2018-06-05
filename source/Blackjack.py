from .Card import Card

class Blackjack():

    cards = []

    def __init__(self):
        self.cards.append(Card("Spades",(1, "Ace")))
        self.cards.append(Card("Spades",(2, "Two")))

    def dealCard(self):
        return self.cards.pop()

    def dealCards(self):
        dealtCards = []
        dealtCards.append(self.dealCard())
        dealtCards.append(self.dealCard())
        return dealtCards
