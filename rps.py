from random import choice

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

    def play(self, rounds=1):
        for i in range(rounds):
            player_move = input("[rock,paper,scissors]: ")
            computer_move = choice(RPSGame.shapes)
            winner = self._evaluate(player_move, computer_move)
            print(20 * "-")
            print("You played: %s" % player_move)
            print("Computer played: %s" % computer_move)
            print(winner)
            print(20 * "-")

if __name__ == '__main__':
    game = RPSGame()
    game.play(rounds=10)

