from random import choice
import unittest


class RPSGame:
    gestures = ['rock', 'paper', 'scissors']
    player_wins = [('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock')]
    
    # the rules of the game
    def _evaluate(self, player_move, computer_move):
        if player_move == computer_move:
            return "Draw!"
        elif (player_move, computer_move) in RPSGame.player_wins:
            return "Player wins!"
        else:
            return "Computer wins!"

    # computer player
    def _computer_move(self):
        return choice(RPSGame.gestures)

    # verify player's input
    def _verify_move(self, player_move):
        if player_move not in RPSGame.gestures:
            raise Exception("Wrong input!")
        return player_move

    # play n rounds of the game against the computer
    def play(self, rounds=1):
        for i in range(rounds):
            player_move = self._verify_move(input("[rock,paper,scissors]: "))
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

    def test_evaluate(self):
        # 1. test for draw
        for g in RPSGame.gestures:
            self.assertEqual(self.rps._evaluate(g, g), 'Draw!')
        # 2. test for player victory
        for g1, g2 in RPSGame.player_wins:
            self.assertEqual(self.rps._evaluate(g1, g2), 'Player wins!')
        # note that we don't have to test for the conditions when
        # computer wins as there are no other possibilities

    def test_computer_move(self):
        moves = {'rock': 0, 'paper': 0, 'scissors': 0}
        n = 100000
        for i in range(n):
            cp = self.rps._computer_move()
            moves[cp] += 1
        for gesture in RPSGame.gestures:
            # 1. Due to the fact the fraction 1/3 is infinite
            # assertEqual will never equate to true (unless n
            # is infinite). Therefore, we need to test
            # for almost equal.
            # self.assertEqual(moves[gesture] / n, 1/3)
            # 2. Test for almost equal with the precision of
            # up to 2 decimal places.
            self.assertAlmostEqual(moves[gesture] / n, 1/3, 2)

    def test_verify_move(self):
        pairs = [('rock', 'rock'), ('paper', 'paper'), ('scissors', 'scissors')]
        for pair in pairs:
            self.assertEqual(self.rps._verify_move(pair[0]), pair[1])

        wrong_input = 'something'
        self.assertRaises(Exception, self.rps._verify_move, wrong_input)

if __name__ == '__main__':
    modes = ["test", "main"]
    switch = input("[test,main]: ")
    if switch == "test":
        unittest.main()
    else:
        rps = RPSGame()
        rps.play(rounds=3)

