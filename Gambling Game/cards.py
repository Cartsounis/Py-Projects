import random

rank_name = {"1": "Ace", "2": "Two",
             "3": "Three", "4": "Four",
             "5": "Five", "6": "Six",
             "7": "Seven", "8": "Eight",
             "9": "Nine", "10": "Ten",
             "11": "Jack", "12": "Queen",
             "13": "King"}

suit_name = {"1": "Clubs", "2" : "Diamonds",
             "3": "Hearts", "4" : "Spades"}

class Card():
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    def __str__(self):
        return "%s of %s" % (rank_name[self._rank], 
                             suit_name[self._suit])

    def getSuit(self) -> str:
        return suit_name(self._suit)
    
    def getRank(self) -> str:
        return rank_name(self._rank)
    
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

    def draw(self, which : str):
        """Removes the 'top', 'bottom' or a 'random' card. (top by default)"""
        which = which.lower()
        try:
            if which == 'bottom':
                return self.pop(0)
            elif which == 'random':
                return self.pop(random.randint(0, len(self)-1))
        except:
            return self.pop()
        
    def printCards(self):
        for card in self:
            print(card)
    
    def shuffle(self):
        """Shuffles the deck"""
        random.shuffle(self)

class Hand(Deck):
    def __init__(self):
        pass

    def pickCard(self, card : Card):
        self.append(card)

    def discardCard(self, which : str):
        """Discard the 'first', 'second' or the 'third' card. (Third by default)"""
        which = which.lower()
        try:
            if which == 'first':                
                return self.pop(0)
            elif which == 'second':
                return self.pop(1)
        except:
            return self.pop()


    
    


    

    


    
