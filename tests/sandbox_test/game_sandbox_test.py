"""
Author: Adrien Funel
Date: Sept-2021
Summary: Sandbox testing for the game module
"""
import src.game as game
from src.players import Player

test_player1 = Player(1, 0.8, 0.8, 0.8)
test_player2 = Player(1, 0.2, 0.2, 0.2)
test_player3 = Player(1, 0.8, 0.8, 0.8)

test_bracket = {'seed': 1,
                'p1': test_player1,
                'p2': test_player3,
                'winner': None,
                'score': ''}


def test_play_match():
    output = game.play_match(test_bracket)
    print(output)


def test_play_set():
    output = game.play_set(test_player1, test_player3)
    print(output)


def test_play_game():
    output = game.play_game(test_player1, test_player3)
    print(output)


def test_play_point():
    output = game.play_point(test_player1, test_player2)
    print(output)


def test_play_deuce():
    output = game.play_deuce(test_player1, test_player3)
    print(output)


def test_play_tiebreak():
    output = game.play_tiebreak(test_player1, test_player3)
    print(output)


if __name__ == '__main__':
    # test_play_set()
    test_play_match()