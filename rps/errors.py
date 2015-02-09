gestures = ["rock", "paper", "scissors"]

def verify_move(player_move):
    if player_move not in gestures:
        raise Exception("Wrong input!")
    return player_move

# let's catch an exception
try:
    player_move = verify_move(input("[rock,paper,scissors]: "))
    print("The move was correct.")
except Exception:
    print("The move was incorrect and Exception was raised.")
