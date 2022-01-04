import random

def guess(x):

    random_number = random.randint(1, x)
    guess_number = 0

    while guess_number != random_number:
        guess_number = int(input('Enter your guess number: '))
        if guess_number > random_number:
            print('sorry guess is too high!')
        elif guess_number < random_number:
            print('guess too low :(')

    print(f'You got it!!! {random_number} is the one')

guess(20)