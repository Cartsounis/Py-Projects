import sys

import cards

import player

class Game:
    def __init__(self):
        self.rival_rounds, self.rival_points = 0, 0
        self.player_rounds, self.player_points = 0, 0
        self._deck = cards.Deck()
        self._table = []
        self._player = player.Player('Player', False)
        self._ally = player.Player('Ally', True)
        self._rival_right = player.Player('Rival on the right', True)
        self._rival_left = player.Player('Rival on the left', True)
        self._player_list = [self._player,self._rival_right,
                                  self._ally,self._rival_left]
        self._running = True
        
    def getNextPlayer(self) -> player.Player:
        return self._player_list[0]
    
    def nextPlayer(self):
        last_player = self._player_list.pop(0)
        self._player_list.append(last_player)
    
    def dealCards(self):
        self._deck.shuffle()
        for i in range(3):
            self._player.takeCard(self._deck.draw())
            self._rival_right.takeCard(self._deck.draw())
            self._ally.takeCard(self._deck.draw())
            self._rival_left.takeCard(self._deck.draw())
    
    def restart(self):
        for player in self._player_list:
            player.resetHand()
        self.rival_rounds, self.player_rounds = 0, 0
        self._deck = cards.Deck()
        self.dealCards()

    def printTable(self):
        for index, card in enumerate(self._table):
            print(self._player_list[index].getName() + ' jogou um ' + str(card))

    def checkRoundWinner(self, playerRounds, rivalRounds) -> tuple:
        higherCard = cards.Card
        higherCardNumber = 0
        multFactor = 1
        winningPlayer = ''
        for index, card in enumerate(self._table):
            if card.getRankNumber() <= 3: multFactor = 100
            else: multFactor = 1
            if ((multFactor * card.getRankNumber()) > higherCardNumber):
                higherCard = card
                higherCardNumber = multFactor * card.getRankNumber()
                winningPlayer = self._player_list[index].getName()

        if (winningPlayer.lower().count('rival')):
            print('Your rival won the round because they played %s' % (higherCard))
            return playerRounds+0,rivalRounds+1
        print('You won the round because your team played %s' % (higherCard))
        return playerRounds+1,rivalRounds+0

    def run(self):
        self.dealCards()
        print('Game is set, type "exit" to quit. Have fun\n')
        while (self._running):
            self.worth = 2

            for i in range(4):
                #player turn
                player = self.getNextPlayer()
                if (player.getName().lower() == 'player'):
                    player.printPlayerCards()
                    choice = input()
                    if (choice.lower() == 'exit'):
                        return 0
                    self._table.append(player.playCard(choice))
                    self.nextPlayer()
                    continue
                    #input decision
                #any bot turn 
                self._table.append(player.playCard())
                self.nextPlayer()
            
            self.printTable()
            self.player_rounds, self.rival_rounds = self.checkRoundWinner(self.player_rounds, self.rival_rounds)
            self._table = []

            # How to improve this next 2 if statement?
            if (self.player_rounds >= 2):
                self.restart()
                self.player_points += self.worth
                print('\nYou won %s points' % (self.worth))
                print('You have %s points, and your oponent have %s\n' % (self.player_points, self.rival_points))
            elif (self.rival_rounds >= 2):
                self.restart()
                self.rival_points += self.worth
                print('\nYour oponent won %s points' % (self.worth))
                print('You have %s points, and your oponent have %s\n' % (self.player_points, self.rival_points))

            # Game Over (Same thing on previous comment - improving if statements)
            if (self.rival_points >= 12):
                print('\nYou lose, keep improving your game!\n')
                break
            elif (self.player_points >= 12):
                print('\nYou won, congratulations!\n')
                break
        return 0

def main():
    game = Game()
    return game.run()

if __name__ == '__main__':
    sys.exit(main())