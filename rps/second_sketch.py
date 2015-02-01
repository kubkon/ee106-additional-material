from random import choice
import unittest

# the rules of the game
gestures = ['rock', 'paper', 'scissors']
player_wins = [('paper', 'rock'), ('rock', 'scissors'), ('scissors', 'paper')]

def evaluate(player_move, computer_move):
    if player_move == computer_move:
        return 'Draw!'
    elif (player_move, computer_move) in player_wins:
        return 'Player wins!'
    else:
        return 'Computer wins!'

# computer AI
def computer_move():
    random_draw = choice(gestures)
    return random_draw

# let's test our implementation of the rules
class Tests(unittest.TestCase):
    def test_evaluate(self):
        # more robust, automated way of testing!
        # 1. test for draw
        for g in gestures:
            self.assertEqual(evaluate(g, g), 'Draw!')
        # 2. test for player victory
        for g1, g2 in player_wins:
            self.assertEqual(evaluate(g1, g2), 'Player wins!')
        # note that we don't have to test for the conditions when
        # computer wins as there are no other possibilities

    def test_computer_move(self):
        moves = {'rock': 0, 'paper': 0, 'scissors': 0}
        n = 100000
        for i in range(n):
            cp = computer_move()
            moves[cp] += 1
        for gesture in moves:
            # 1. Due to the fact the fraction 1/3 is infinite
            # assertEqual will never equate to true (unless n
            # is infinite). Therefore, we need to test
            # for almost equal.
            # self.assertEqual(moves[gesture] / n, 1/3)
            # 2. Test for almost equal with the precision of
            # up to 2 decimal places.
            self.assertAlmostEqual(moves[gesture] / n, 1/3, 2)

if __name__ == '__main__':
    unittest.main()
