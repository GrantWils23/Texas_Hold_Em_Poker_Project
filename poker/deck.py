# from poker.card import Card #CREATING DEPENDENSE...!!!
import random

class Deck():
    def __init__(self):        # (self, shuffle_func) this is how to decouple and give it independancy
        self.cards = []     #self._cards

    def __len__(self):
        return len(self.cards)

    def add_cards(self, cards):
        self.cards.extend(cards)    #self._cards
 
    def remove_cards(self, number):
        cards_to_remove = self.cards[0:number]
        del self.cards[0:number]

        return cards_to_remove

    def shuffle(self):
        random.shuffle(self.cards) # self.shuffle_func(self.cards)

   

    # def create_cards(self):
    #     cards = Card.Create_52_cards() 

        # for suit in card.SUITS:
        #     for rank in card.RANKS:
        #         Card(# Rank Suit)

    