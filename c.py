class Card:
    
    cards = [None, None, '2', '3', '4', '5', '6', '7', '8', '9', '10',
             'Jack', 'Queen', 'King', 'Ace']
    suits = ['hart', 'diamond', 'spade', 'crab']
    
    def __init__ (self, number, suit):
        self.number = number
        self.suit = suit

    def __lt__(self, other):
        if self.number < other.number:
            return True
        elif self.number == other.number:
            if self.suit < other.suit:
                return True
            else :
                return False
        else :
            return False

    def __gt__(self, other):
        if self.number > other.number:
            return True
        elif self.number == other.number:
            if self.suit > other.suit:
                return True
            else:
                return False
        else:
            return False

    def __repr__(self):
        return '{} of {}'.format(self.cards[self.number], \
                                self.suits[self.suit])

from random import shuffle
class Deck:
    def __init__(self):
        self.yamahuda = []
        for i in range (2, 15):
            for j in range (4):
                self.yamahuda.append(Card(i, j))
        shuffle(self.yamahuda)

    def rm_card(self):
        if len (self.yamahuda) == 0:
            return
        return self.yamahuda.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0

class Game:
    def __init__(self):
        self.p1 = Player(input('Type your name:'))
        self.p2 = Player(input('Type another name:'))
        self.deck = Deck()

    def game_start(self):
        while True:
            n = input('Type space. You want stop game, q:')
            if n == 'q':
                print('Game set')
                break
            elif n == ' ':
                self.p1card = self.deck.rm_card()
                self.p2card = self.deck.rm_card()
                print('{} draw {}.\n{} draw {}'\
                      .format(self.p1.name, self.p1card, self.p2.name, \
                              self.p2card))
                if self.p1card > self.p2card:
                    self.p1.wins += 1
                    print(self.p1.name, ' is win!')
                elif self.p1card < self.p2card:
                    self.p2.wins += 1
                    print(self.p2.name, ' is win!')
        
        message = '{} gets {} points.\n{} gets {} points.'\
                  .format(self.p1.name, self.p1.wins, \
                          self.p2.name, self.p2.wins)
        if self.p1.wins == self.p2.wins:
            print(message)

        elif self.p1.wins > self.p2.wins:
            print(message + '\n{} win!'.format(self.p1.name))
        elif self.p1.wins < self.p2.wins:
            print(message + '\n{} win!'.format(self.p2.name))

game1 = Game()
game1.game_start()
            
            
        
        
        
