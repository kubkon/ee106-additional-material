from random import choice
import unittest
from enum import Enum


class Gesture(Enum):
    rock = 0
    paper = 1
    scissors = 2


class Result(Enum):
    draw = 'Draw!'
    player = 'Player wins!'
    computer = 'Computer wins!'


class RPSGame:
    player_wins = [
        (Gesture.rock, Gesture.scissors),
        (Gesture.scissors, Gesture.paper),
        (Gesture.paper, Gesture.rock)
    ]
    
    # the rules of the game
    def _evaluate(self, player_move, computer_move):
        if player_move == computer_move:
            return Result.draw
        elif (player_move, computer_move) in RPSGame.player_wins:
            return Result.player
        else:
            return Result.computer

    # computer player
    def _computer_move(self):
        return choice(list(Gesture))

    # verify player's input
    def _verify_move(self, player_move):
        if player_move not in [g.name for g in Gesture]:
            raise Exception("Wrong input!")
        return Gesture[player_move]

    # play n rounds of the game against the computer
    def play(self, rounds=1):
        for i in range(rounds):
            player_move = self._verify_move(input("[rock,paper,scissors]: "))
            computer_move = self._computer_move()
            winner = self._evaluate(player_move, computer_move).value
            print(20 * "-")
            print("You played: %s" % player_move.value)
            print("Computer played: %s" % computer_move.value)
            print(winner)
            print(20 * "-")


class RPSGameTests(unittest.TestCase):
    def setUp(self):
        self.rps = RPSGame()

    def test_evaluate(self):
        # 1. test for draw
        for g in list(Gesture):
            self.assertEqual(self.rps._evaluate(g, g), Result.draw)
        # 2. test for player victory
        for g1, g2 in RPSGame.player_wins:
            self.assertEqual(self.rps._evaluate(g1, g2), Result.player)
        # note that we don't have to test for the conditions when
        # computer wins as there are no other possibilities

    def test_computer_move(self):
        moves = {Gesture.rock: 0, Gesture.paper: 0, Gesture.scissors: 0}
        n = 100000
        for i in range(n):
            cp = self.rps._computer_move()
            moves[cp] += 1
        for gesture in Gesture:
            # 1. Due to the fact the fraction 1/3 is infinite
            # assertEqual will never equate to true (unless n
            # is infinite). Therefore, we need to test
            # for almost equal.
            # self.assertEqual(moves[gesture] / n, 1/3)
            # 2. Test for almost equal with the precision of
            # up to 2 decimal places.
            self.assertAlmostEqual(moves[gesture] / n, 1/3, 2)

    def test_verify_move(self):
        correct_user_input = [g.name for g in Gesture]
        for ip in correct_user_input:
            self.assertEqual(self.rps._verify_move(ip), Gesture[ip])

        incorrect_user_input = ['Rock', 'pAPER', 'spock']
        self.assertRaises(Exception, self.rps._verify_move, incorrect_user_input)

if __name__ == '__main__':
    modes = ["test", "main"]
    switch = input("[test,main]: ")
    if switch == "test":
        unittest.main()
    else:
        rps = RPSGame()
        rps.play(rounds=3)

