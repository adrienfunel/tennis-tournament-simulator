"""
Author: Adrien Funel
Date: Sept-2021
Summary: the main entry point
"""
import time
import math
import logging

from common import my_logger
from organisation import play_rounds

logger = logging.getLogger()


def setup():
    """
    Function to start service-level setup.
    :return: N/A
    """
    my_logger.set_logger()


def main():
    """
    Main entry point.
    :return: N/A
    """
    nb_players = get_input_players()
    while not math.log2(nb_players).is_integer() \
            or not nb_players <= 64:
        print("The number of participants is invalid,"
              "please enter a number of participants that fits a single-elimination tournament.\n"
              "Nb: to be valid the number of participants must be a power of 2 (max 64)"
              "(i.e 2, 4, 8, 16, etc.)."
              )
        nb_players = get_input_players()

    logger.info("****** TENNIS TOURNAMENT SIMULATION STARTING ******")

    play_rounds(nb_players)


def get_input_players():
    """
    Function to get the number of players.
    :return: int, inputed number of players
    """
    return int(input("Enter the number of participants (up to 64):- "))


if __name__ == "__main__":
    start_time = time.time()
    setup()
    main()
    logger.info("--- The service ran in %s seconds ---\n\n\n"
                % round((time.time() - start_time), 6)
                )
