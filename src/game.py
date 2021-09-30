"""
Author: Adrien Funel
Date: Sept-2021
Summary: simulate a competitive tennis game
"""


def play_game(bracket):
    player1 = bracket['p1']
    player2 = bracket['p2']
    print(player1)
    print(player2)
    bracket.update({'seed': bracket['seed'],
                    'p1': bracket['p1'],
                    'p2': bracket['p2'],
                    'winner': bracket['p1'],
                    'score': '6-2'})

    return bracket