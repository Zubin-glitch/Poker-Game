"""
Description: A player is a participant in the game of poker. 
My player class stores a name, the player’s hole cards 
(the two cards you are dealt at the start of a round), 
and the player's best possible poker hand constructed from 
the two hole cards, and upto five community cards on the table.
The class is importing a bunch of methods from the module 
poker_rules.py which is defining how poker hands are compared 
and ranked, more on this later.
"""

from deck import Deck
from card import Card
from poker_rules import compute_best_hand, categorize_hand
from itertools import combinations

class Player:
    def __init__(self, name):
        self._name = str(name)
        self._holeCards = []
        self._bestHand = None
    

    def __str__(self):
        # Check if a best hand is computed and prints accordingly
        if not self._bestHand:
            return f"{self._name}: {self._holeCards}"
        else:
            return f"{self._name} : {self._bestHand}, {categorize_hand(self._bestHand)}"

    def __repr__(self):
        return str(self)
    

    def draw_card(self, card: Card) -> None:
        if len(self._holeCards) < 2:
            self._holeCards.append(card)
        else:
            raise Exception("A player cannot be dealt more than 2 cards!")
    
    def update_best_hand(self, table):
        """
        This function calculates the best possible hand
        for a player from combinations possible from two
        hole cards and upto 5 community cards.
        """
        if len(table) < 3:
            raise ValueError("Not enough cards on the table!")
        if len(table) >= 3:
            # TODO: Either use itertools.combinations or write own combination listing function
            list_cards = []
            list_cards.extend(table)
            list_cards.extend(self._holeCards)
            list_hands = [list(combo) for combo in combinations(list_cards, 5)]
            self._bestHand = compute_best_hand(list_hands)
            self._bestHand.sort(reverse=True)
            return self._bestHand
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
    
    def get_hole_cards(self):
        return self._holeCards
    
    def get_best_hand(self):
        if not self._bestHand:
            raise Exception("Best hand is undetermined. Call update_best_hand() first!")
        else:
            return self._bestHand

    def get_holecards_pokernotation(self):
        """
        This function returns the hole cards as a compact string
        specifying the cards and if they are suited.

        If hole cards are a pair, returns the ranks as is.
        If hole cards are suited, append a 's' to denote suited.
        otherwise, append an 'o' to denote offsuited
        """
        if len(self._holeCards) == 2:
            self._holeCards.sort(reverse=True)
            poker_notation = self._holeCards[0].rank + self._holeCards[1].rank

            if poker_notation[0] == poker_notation[1]:
                return poker_notation
            else:
                if self._holeCards[0].suit == self._holeCards[1].suit:
                    return poker_notation + "s"
                else:
                    return poker_notation + "o"
