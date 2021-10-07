"""
Author: Adrien Funel
Date: Oct-2021
Summary: unit test for the game module
"""
import unittest
from unittest import mock

from src import game
from src.players import Player

test_player1 = Player(1, 0.8, 0.8, 0.8)
test_player2 = Player(1, 0.2, 0.2, 0.2)
test_player3 = Player(1, 0.8, 0.8, 0.8)

test_bracket = {'seed': 1,
                'p1': test_player1,
                'p2': test_player2,
                'winner': None,
                'score': ''
                }


class TestGame(unittest.TestCase):

    @mock.patch('src.game.play_set')
    def test_play_match(self, mocked_set):
        mocked_set.return_value = "set p1", "6-0"

        expected_bracket = {'seed': 1,
                            'p1': test_player1,
                            'p2': test_player2,
                            'winner': test_player1,
                            'score': '6-0;6-0;6-0'
                            }

        result = game.play_match(test_bracket)

        self.assertEqual(result, expected_bracket)

    @mock.patch('src.game.play_game')
    def test_play_set(self, mocked_game):
        mocked_game.return_value = "game p1"

        result = game.play_set(test_player1, test_player2)

        self.assertEqual(result, ("set p1", "6-0"))

    @mock.patch('src.game.play_point')
    def test_play_game(self, mocked_point):
        mocked_point.return_value = "point p1"

        result = game.play_game(test_player1, test_player2)

        self.assertEqual(result, "game p1")

    def test_play_point(self):
        import random
        random.seed(0)

        input_expected = [
            (test_player1, test_player2, "point p1"),
            (test_player2, test_player1, "point p2")
        ]

        for input1, input2, output in input_expected:
            self.assertEqual(game.play_point(input1, input2), output)

    @mock.patch('src.game.play_point')
    def test_play_deuce(self, mocked_point):
        mocked_point.return_value = "point p1"

        result = game.play_deuce(test_player1, test_player2)

        self.assertEqual(result, "game p1")

    @mock.patch('src.game.play_point')
    def test_play_tiebreak(self, mocked_point):
        mocked_point.return_value = "point p1"

        result = game.play_tiebreak(test_player1, test_player2)

        self.assertEqual(result, ("set p1", "7(7)-6(0)"))


if __name__ == '__main__':
    unittest.main()
