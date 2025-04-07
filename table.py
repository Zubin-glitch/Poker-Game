from player import Player
from poker_rules import compute_best_hand

def winning_player(players: Player):
    """"
    Given a list of players, return the player/players 
    with the best hand.
    """

    player_best_hands = [p.get_best_hand() for p in players]
    winning_hand = compute_best_hand(player_best_hands)
    winners = [p for p in players if p.get_best_hand() == winning_hand]
    return winners
