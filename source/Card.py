class Card():
    def __init__(self, cardValue, cardSuit, cardValueName):
         self.__value = cardValue
         self.__suit = cardSuit
         self.__valueName = cardValueName

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
