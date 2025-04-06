from  card import Card
import random
# Deck is of 52 cards
class Deck:
    """
    The Deck class is very simple, it is simply a list of Cards. 
    The Deck constructor takes no arguments, 
    the deck will contain one Card of every suite and every value.
    """
    def __init__(self):
        # Create a deck of 52 cards whenever a new Deck object is initialized
        self._deck = self.create_deck()
        self.drawn_cards = []
    
    def create_deck(self):
        deck = []
        for suite in Card.static_suites:
            for rank in Card.static_ranks:
                deck.append(Card(rank, suite))
        if len(deck) == 52:
            return deck
        else:
            raise Exception('Debug please, number of cards is not 52!')

    def shuffle(self):
        print(f'Original deck = {self._deck}')
        # Randomly shuffle the deck between 1 and 5 times.
        # To mimic actual shuffling
        for i in range(random.randint(1, 5)):
            random.shuffle(self._deck)
        print(f'\n \nDeck after shuffling = {self._deck}')

    # This method wouldn't be needed since these cards should be hidden
    def show_drawn_cards(self):
        # print("Cards on the table are: ")
        for each_card in self.drawn_cards:
            print(each_card)
        
    def __len__(self):
        return len(self._deck)
    
    def deal_card(self):
        drawn_card = self._deck.pop()
        self.drawn_cards.append(drawn_card)
        return drawn_card
    def __str__(self):
        return " ".join([str(card) for card in self._deck])
    

# Unit tests
deck = Deck()
print(deck)
print(len(deck))

deck.shuffle()
dealt_card = deck.deal_card()
print(f"Dealt card = {dealt_card} and size of the deck is = {len(deck)}")