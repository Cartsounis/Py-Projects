import cards

import random as r

class Player:
    def __init__(self, name : str, bot : bool):
        self._name = name
        self._cards = []
        self._bot = bot

    def getName(self) -> str:
        return self._name
    
    def getCards(self) -> list:
        return self._cards
    
    def setCards(self, cards : cards.Card):
        self._cards = cards

    def resetHand(self):
        self._cards = []

    def printPlayerCards(self):
        hand_str = 'Você tem '
        for index, card in enumerate(self._cards):
            hand_str += str(card).lower() + ' (%s), ' % (index+1)
        print(hand_str + 'qual carta deseja jogar?')

    def playCard(self, which : str = '1') -> cards.Card:
        if (not self._bot):
            print(which)
            try: 
                return self._cards.pop(int(which)-1)
            except:
                return self._cards.pop(0)
        #implement ai algorithm, for now its random
        return self._cards.pop(r.randint(0,len(self._cards)-1))
    
    def takeCard(self, card : cards.Card):
        self._cards.append(card)