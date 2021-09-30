"""
Author: Adrien Funel
Date: Sept-2021
Summary: generate tournament brackets
"""
import math

from game import play_game


class Bracket:

    def __init__(self):
        self.brackets = []
        self.players_list = None
        self.nb_players = None
        self.nb_rounds = None

    def add_participants(self, players):
        self.players_list = players
        self.nb_players = len(players)
        self.nb_rounds = int(math.log2(len(players)))

    def generate_round_brackets(self):
        matchups = [self.players_list[i:i + 2] for i in range(0, self.nb_players, 2)]
        for i, faceoff in enumerate(matchups):
            self.brackets.append(
                {'seed': i+1,
                 'p1': faceoff[0],
                 'p2': faceoff[1],
                 'winner': None,
                 'score': ''}
            )

    def generate_next_round(self):
        prev_rounds = [self.brackets[i:i + 2] for i in range(0, len(self.brackets), 2)]
        self.brackets = []
        for i, faceoff in enumerate(prev_rounds):
            # print("The faceoff is {}".format(faceoff))
            self.brackets.append(
                {'seed': i + 1,
                 'p1': faceoff[0]['winner'],
                 'p2': faceoff[1]['winner'],
                 'winner': None,
                 'score': ''}
            )

    def play_games(self):
        self.brackets = list(map(play_game, self.brackets))

