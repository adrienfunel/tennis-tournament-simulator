"""
Author: Adrien Funel
Date: Sept-2021
Summary: generate tournament brackets
"""
import math


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
        # return {'seed': i+1, 'p1': self.players_list[i], 'p2': self.players_list[i + 2], 'winner': '' for i in range(0, self.nb_players, 2)}
        for i, faceoff in enumerate(matchups):
            self.brackets.append(
                {'seed':i+1, 'p1':faceoff[0], 'p2':faceoff[1], 'winner':None, 'score':''}
            )
        return self.brackets

    def generate_next_round(self):
        prev_rounds = [self.brackets[i:i + 2] for i in range(0, len(self.brackets), 2)]
        self.brackets = []
        for i, round in enumerate(prev_rounds):
            self.brackets.append(
                {'seed': i + 1, 'p1': round[0]['winner'], 'p2': round[1]['winner'], 'winner': None, 'score': ''}
            )
        return self.brackets
