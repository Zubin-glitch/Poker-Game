from deck import Deck
from table import *
from poker_stats import *
import csv


starting_hand_stats = {}
hand_stats = {'won': 0, 'played': 0}
create_stats_dict(starting_hand_stats, hand_stats)

num_simulations = 1000
num_players = 8

for n in range(2, num_players + 1):
    for i in range(num_simulations):
        print(f"Game {i}")
        playing_deck = Deck()
        playing_deck.shuffle()
        assert len(playing_deck) == 52, "A Deck should contain exactly 52 cards."

        # set players
        players = [Player(f"Player {p}") for p in range(n)]
        
        # Deal cards
        for _ in range(2):
            # Deal each player a card for 2 rounds
            for player in players:
                player.draw_card(playing_deck.deal_card())

        for p in players:
            p_hand = p.get_holecards_pokernotation()
            starting_hand_stats[p_hand]['played'] += 1
        
        playing_deck.deal_card() # burn before flop
        flop = [playing_deck.deal_card() for _ in range(3)]

        # update each player's best hand


        playing_deck.deal_card() # burn before turn
        turn = [playing_deck.deal_card()]

        # Update each player's best hand

        playing_deck.deal_card() # burn before river
        river = [playing_deck.deal_card()]

        # Calculate final best hand for each player
        table = flop + turn + river
        # Publish the winner

        for p in players:
            best_hand = p.update_best_hand(table)
        
        for p in winning_player(players):
            p_hand = p.get_holecards_pokernotation()
            starting_hand_stats[p_hand]['won'] += 1
        
    with open(f"simulation_{n}.csv", 'w', newline='') as f:
        cols = ['hand','won','played']
        w = csv.DictWriter(f, cols)
        w.writeheader()
        for hand, stat in starting_hand_stats.items():
            row = {"hand": hand}
            row.update(stat)
            w.writerow(row)

