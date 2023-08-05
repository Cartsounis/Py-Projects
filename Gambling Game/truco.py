import sys

import regex

import cards

class Game:
    def __init__(self):
        # self.rival_rounds, self.rival_points, self.rival_matches = 0
        # self.player_rounds, self.player_points, self.player_matches = 0
        self.incomed_points = 0
        self._deck = cards.Deck()
        self._player = cards.Hand()
        self._ally = cards.Hand()
        self._rival_right = cards.Hand()
        self._rival_left = cards.Hand()
        self._table = cards.Hand()

    def giveCards(self):
        self._deck.shuffle()
        for i in range(3):
            self._player.pickCard(self._deck.draw())
            self._rival_right.pickCard(self._deck.draw())
            self._ally.pickCard(self._deck.draw())
            self._rival_left.pickCard(self._deck.draw())

    def restart(self):
        self._deck = cards.Deck()
        self._table = cards.Hand()
        self.giveCards()

    def run(self):
        game_over = False
        while not game_over:
            #game code here
            if (self.rival_rounds or self.player_rounds) >= 2:
                game_over = True

    def printTable(self):
        if (self._table):
            table_str = 'As cartas na mesa são:'
            for index, card in enumerate(self._table):
                #adicionar lista de jogadores no lugar de alessandro e usar como parametro o index do for
                table_str += ' %s jogada por %s' % (card, 'Alessandro')
            print(table_str)
            return
        print('Você é o primeiro a jogar')
        return
        

    def printHand(self):
        hand_str = 'Você tem '
        for index, card in enumerate(self._player):
            hand_str += str(card).lower() + '( %s), ' % (index+1)
        print(hand_str + 'qual carta deseja jogar?')

       

def main():
    game = Game()
    game.giveCards()
    # game._deck.printCards()
    # game._player.printCards()
    game._table.append(game._deck.draw())
    game.printTable()
    game.printHand()
    return 0

if __name__ == '__main__':
    sys.exit(main())