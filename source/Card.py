class Card():
    def __init__(self,  cardSuit, value):
         self.__value, self.__valueName = value
         self.__suit = cardSuit

    @property
    def value(self):
        return self.__value

    @property
    def suit(self):
        return self.__suit

    @property
    def valueName(self):
        return self.__valueName

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return hash((self.value,self.suit,self.valueName))

    def __repr__(self):
        return "The %s of %s" % (self.valueName,self.suit)
