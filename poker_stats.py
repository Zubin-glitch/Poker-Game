from card import Card
from itertools import combinations

def create_stats_dict(starting_hand_stats, stats_dict):
    """
    This function creates an updated dictionary with
    169 keys that represent every unique starting 
    hand combination.
    """
    
    pocket_pairs = [(c * 2) for c in Card.static_ranks]
    combos = list(combinations(Card.static_ranks, 2))
    suited_hands = [b + a + 's' for a, b in combos]
    off_suited_hands = [b + a + 'o' for a, b in combos]
    starting_hand_stats.update({k: stats_dict.copy() for k in pocket_pairs + suited_hands + off_suited_hands})
