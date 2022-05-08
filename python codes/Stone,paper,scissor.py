import random

def play():
    user = input("Whats your choice, 's' for stone, 'p' for paper, 'c' for scissor \n")
    computer = random.choice(['s','p','c'])

    if user == computer:
        return 'it\'s a tie'

    if is_win(user, computer):
        return 'You won!'
    
    return 'you lost!'


def is_win(player, opponent):
    if (player == 's' and opponent == 'c') or (player == 'c' and opponent == 'p') or (player == 'p' and opponent == 's'):
        return True


print(play())
