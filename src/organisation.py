"""
Author: Adrien Funel
Date: Sept-2021
Summary: pre-processing module
"""
import random
import logging

from players import Player
from brackets import Bracket

logger = logging.getLogger()


def generate_players(nb_participants):
    """
    Function to generate the list of participants along with their skill levels
    :param nb_participants: int representing how many players are participating
    :return: list of instances of the Player class representing the participants
    """
    list_players = []
    for i in range(0, nb_participants):
        instance_player = Player(str(i + 1),
                                 attribute_score(),
                                 attribute_score(),
                                 attribute_score()
                                 )
        list_players.append(instance_player)

    return list_players


def play_rounds(nb_players):
    """
    Function to organise and run the successive rounds of the tournament.
    :param nb_players: int representing how many players are participating
    :return: N/A
    """
    participants = generate_players(nb_players)
    Tournament = Bracket()
    Tournament.add_participants(participants)
    logger.info("Tournament has been initialized with {} participants and {} rounds.".format(Tournament.nb_players,
                                                                                             Tournament.nb_rounds
                                                                                             )
                )
    logger.info("There are {} rounds".format(Tournament.nb_rounds))
    Tournament.generate_round_brackets()
    logger.info("The first round brackets have been generated. There are {} games to be played.\n"
                .format(len(Tournament.brackets)))

    for i in range(0, Tournament.nb_rounds):
        logger.info("This is round nb: {}".format(i+1))
        logger.info(Tournament.brackets)
        Tournament.play_matches()

        if i != Tournament.nb_rounds-1:
            # Last round is the finale, no further brackets
            Tournament.generate_next_round()
            logger.info("There are {} players remaining".format(2*len(Tournament.brackets)))

    logger.info("Finale results: {}".format(Tournament.brackets[0]))
    logger.info("The tournament winner is: {}".format(Tournament.brackets[0]['winner']))


def attribute_score():
    """
    Function to randomly attribute skill levels.
    :return: float between 0 and 1
    """
    return round(random.uniform(0, 1), 2)
