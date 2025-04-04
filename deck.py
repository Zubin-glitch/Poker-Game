from card import Card
import random
# Deck is of 52 cards
class Deck:
    def __init__(self):
        # Create a deck of 52 cards whenever a new Deck object is initialized
        self.cards = self.create_deck()
        self.drawn_pile = []
    
    def create_deck(self):
        deck = []
        for suit in Card.valid_suits:
            for rank in Card.valid_ranks:
                deck.append(Card(rank, suit))
        if len(deck) == 52:
            return deck
        else:
            raise Exception('Debug, number of cards is not 52!')

    def shuffle(self):
        print(f'Original deck = {self.cards}')
        random.shuffle(self.cards)
        # self.show_pile()
        print(f'\n \nDeck after shuffling = {self.cards}')

    def show_pile(self):
        for each_card in self.cards:
            print(f'{each_card}')

    def show_drawn_pile(self):
        for each_card in self.drawn_pile:
            print(f'{each_card}')

    def draw(self):
        # Pull card from top of deck
        drawn_card = self.cards.pop()
        # insert this card into the drawn pile
        self.drawn_pile.append(drawn_card)
        

deck_1 = Deck()
deck_1.shuffle()
deck_1.draw()

deck_1.show_drawn_pile()
deck_1.show_pile()