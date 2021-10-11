"""
Author: Adrien Funel
Date: Sept-2021
Summary: generate tournament brackets
"""
import math
import logging

from game import play_match

logger = logging.getLogger()


class Bracket:
    """
    Class to perform brackets operations for the successive rounds.
    """
    def __init__(self):
        self.brackets = []
        self.players_list = None
        self.nb_players = None
        self.nb_rounds = None

    def add_participants(self, players):
        """
        Function to initialise the tournament with a list of players.
        :param players: list of objects
        :return: N/A
        """
        self.players_list = players
        self.nb_players = len(players)
        self.nb_rounds = int(math.log2(len(players)))

    def generate_round_brackets(self):
        """
        Function to organise the first round of the tournament.
        :return: N/A
        """
        try:
            matchups = [self.players_list[i:i + 2] for i in range(0, self.nb_players, 2)]
            for i, faceoff in enumerate(matchups):
                self.brackets.append(
                    {'seed': i+1,
                     'p1': faceoff[0],
                     'p2': faceoff[1],
                     'winner': None,
                     'score': ''
                     }
                )
        except Exception as e:
            logger.exception(e)
            raise

    def generate_next_round(self):
        """
        Function to organise the next round of brackets.
        :return: N/A
        """
        try:
            prev_rounds = [self.brackets[i:i + 2] for i in range(0, len(self.brackets), 2)]
            self.brackets = []
            for i, faceoff in enumerate(prev_rounds):
                self.brackets.append(
                    {'seed': i + 1,
                     'p1': faceoff[0]['winner'],
                     'p2': faceoff[1]['winner'],
                     'winner': None,
                     'score': ''
                     }
                )
        except Exception as e:
            logger.exception(e)
            raise

    def play_matches(self):
        """
        Function to play all the matches of a round.
        :return: N/A
        """
        self.brackets = list(map(play_match, self.brackets))
