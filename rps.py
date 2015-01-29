from random import choice
import unittest

class RPSGame:
    shapes = ['rock', 'paper', 'scissors']
    draws = [('rock', 'rock'), ('paper', 'paper'), ('scissors', 'scissors')]
    first_wins = [('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock')]
    
    def _evaluate(self, player_move, computer_move):
        if (player_move, computer_move) in RPSGame.draws:
            return "Draw!"
        elif (player_move, computer_move) in RPSGame.first_wins:
            return "Player wins!"
        else:
            return "Computer wins!"

    def _computer_move(self):
        return choice(RPSGame.shapes)

    def play(self, rounds=1):
        for i in range(rounds):
            player_move = input("[rock,paper,scissors]: ")
            computer_move = self._computer_move()
            winner = self._evaluate(player_move, computer_move)
            print(20 * "-")
            print("You played: %s" % player_move)
            print("Computer played: %s" % computer_move)
            print(winner)
            print(20 * "-")


class RPSGameTests(unittest.TestCase):
    def setUp(self):
        self.rps = RPSGame()

    def test_computer_move(self):
        moves = {'rock': 0, 'paper': 0, 'scissors': 0}
        n = 100000
        for i in range(n):
            cp = self.rps._computer_move()
            moves[cp] += 1
        for shape in moves:
            # self.assertEquals(moves[shape] / n, 1/3)
            self.assertAlmostEqual(moves[shape] / n, 1/3, 2)

if __name__ == '__main__':
    unittest.main()
