import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card():
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank+ " of "+self.suit


class Deck:
    
    def __init__(self, deck):
        self.deck = deck 
        deck = []  # start with an empty list
        for suit in suits:
            x = suit.random.append[]
            
            for rank in ranks:
                y = suit.random.append[]
                
                (x,y) = append.deck []
    
    def __str__(self):
        return print("You were dealt the {} of {}".format[suit,rank])

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        while playing == True: 
            for __init__(): 
                hand = []
                if hand < 2: 
                    break
             

test_deck = Deck()
print(test_deck)