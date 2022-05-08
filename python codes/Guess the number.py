import random


def guess(x):
    random_number=random.randint(1, x)
    guess=0
    while guess != random_number:
        guess=int(input(f"Enter a number between 1 and {x}: "))
        if guess < random_number:
            print("sorry,Guess again,too low")
        elif guess >random_number:
            print("sorry,Guess again,toooooo high")    
    print(f'congrats,you gottcha, {random_number} guessed succesfully')


def computer_guess(x):
    low=1
    high=x
    feedback=' '
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess=low
        feedback=input(f"Is {guess} too high (H),too low (L),or correct (C) ")
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'yah!, the computer guessed your number {guess} correctly!')               


guess(1000)
computer_guess(1000)
# just calling the function


