import random

rank_name = {"1": "Ás", "2": "Dois",
             "3": "Três", "4": "Quatro",
             "5": "Cinco", "6": "Seis",
             "7": "Sete",
             "11": "Dama", "12": "Valete",
             "13": "Rei"}

suit_name = {"1": "Paus", "2" : "Ouros",
             "3": "Copas", "4" : "Espadas"}

class Card():
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    def __str__(self):
        return "%s de %s" % (rank_name[self._rank], 
                             suit_name[self._suit])

    def getSuit(self) -> str:
        return suit_name(self._suit)
    
    def getRank(self) -> str:
        return rank_name(self._rank)
    
    def getRankNumber(self) -> int:
        return int(self._rank)
    
    def setSuit(self, suit):
        self._suit = suit

    def setRank(self, rank):
        self._rank = rank
    
class Deck(list):
    def __init__(self):
        for rank in rank_name:
            for suit in suit_name:
                self.append(Card(rank, suit))

    def cut(self):
        """Split the deck into two packets randomly
           and placing the lower packet on top of the top packet"""
        cutting_card = random.randint(1, len(self)-1)
        new_deck = self[cutting_card:] + self[:cutting_card]
        self = new_deck

    def draw(self) -> Card:
        """Removes the top card."""
        return self.pop()
        
    def printCards(self):
        for card in self:
            print(card)
    
    def shuffle(self):
        """Shuffles the deck"""
        random.shuffle(self)

    

    


    
