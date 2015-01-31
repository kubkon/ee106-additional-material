import unittest

# the rules of the game
# v1
# def evaluate(player_move, computer_move):
#     if player_move == computer_move:
#         return 'Draw!'
#     elif player_move == 'paper' and computer_move == 'rock':
#         return "Player wins!"
#     elif player_move == 'rock' and computer_move == 'scissors':
#         return "Player wins!"
#     elif player_move == 'scissors' and computer_move == 'paper':
#         return "Player wins!"
#     else:
#         return "Computer wins!"

# v2: simplify conditions
player_wins = [('paper', 'rock'), ('rock', 'scissors'), ('scissors', 'paper')]

def evaluate(player_move, computer_move):
    if player_move == computer_move:
        return 'Draw!'
    elif (player_move, computer_move) in player_wins:
        return 'Player wins!'
    else:
        return 'Computer wins!'

# let's test our implementation of the rules
class Tests(unittest.TestCase):
    def test_evaluate(self):
        # not very robust way of testing!
        self.assertEqual(evaluate('rock', 'paper'), 'Computer wins!')
        self.assertEqual(evaluate('rock', 'scissors'), 'Player wins!')
        self.assertEqual(evaluate('rock', 'rock'), 'Draw!')
        
        # more robust, automated way of testing!
        # 1. test for draw
        for g in ['rock', 'paper', 'scissors']:
            self.assertEqual(evaluate(g, g), 'Draw!')
        # 2. test for player victory
        for g1, g2 in player_wins:
            self.assertEqual(evaluate(g1, g2), 'Player wins!')
        # note that we don't have to test for the conditions when
        # computer wins as there are no other possibilities

if __name__ == '__main__':
    unittest.main()
