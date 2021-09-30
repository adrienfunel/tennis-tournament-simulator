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
                {'seed': i+1, 'p1': faceoff[0], 'p2': faceoff[1], 'winner': None, 'score': ''}
            )

    def generate_next_round(self):
        prev_rounds = [self.brackets[i:i + 2] for i in range(0, len(self.brackets), 2)]
        self.brackets = []
        for i, faceoff in enumerate(prev_rounds):
            # print("The faceoff is {}".format(faceoff))
            self.brackets.append(
                {'seed': i + 1, 'p1': faceoff[0]['winner'], 'p2': faceoff[1]['winner'], 'winner': None, 'score': ''}
            )

    def play_games(self):
        for game in self.brackets:
            game.update({'seed': game['seed'], 'p1': game['p1'], 'p2': game['p2'], 'winner': game['p1'], 'score': '6-2'})

