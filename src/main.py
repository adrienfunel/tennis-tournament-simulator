"""
Author: Adrien Funel
Date: Sept-2021
Summary: the main entry point
"""
import time
import math

from organisation import play_rounds

def main():
    # main entry point
    nb_players = get_input_players()
    while not math.log2(nb_players).is_integer():
        print("The number of participants is invalid, "
              "please enter a number of participants that fits a single-elimination tournament.\n"
              "Nb: to be valid the number of participants must be a power of 2 (i.e 2, 4, 8, 16, etc.).")
        nb_players = get_input_players()

    play_rounds(nb_players)


def get_input_players():
    return int(input("Enter the number of participants:- "))


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % round((time.time() - start_time), 6))
