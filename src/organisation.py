"""
Author: Adrien Funel
Date: Sept-2021
Summary: pre-processing module
"""
import random

from players import Player
from brackets import Bracket


def generate_players(nb_participants):
    list_players = []
    for i in range(0, nb_participants):
        instance_player = Player(str(i + 1), attribute_score(), attribute_score(), attribute_score())
        list_players.append(instance_player)

    return list_players


def play_rounds():
    participants = generate_players(8)
    Tournament = Bracket()
    Tournament.add_participants(participants)
    print("There are {} rounds".format(Tournament.nb_rounds))
    Tournament.generate_round_brackets()
    for i in range(0, Tournament.nb_rounds):
        print("This is round nb: {}".format(i+1))
        print(Tournament.brackets)
        Tournament.play_games()
        # print([x for x in round_brackets if x['seed'] == 1])
        if i != Tournament.nb_rounds-1:
            # Last round is the finale, no further brackets
            Tournament.generate_next_round()
            print("There are {} players remaining".format(2*len(Tournament.brackets)))

    print("Finale results: {}".format(Tournament.brackets))


def attribute_score():
    return round(random.uniform(0, 1), 2)


