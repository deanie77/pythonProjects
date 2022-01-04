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


def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f'{guess} is this number too high (H), too low (L) or correct (C)?').lower()
        
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f'Yayyyyy the computer has guessed you number {guess} correctly!!!')
            break
        else:
            print('what the hell are you doing?!')


def autoGuessGame():
    
    low = 1
    high = random.randint(2, 10000)
    number = random.randint(1, high)
    feedback = ''

    while feedback != 'correct':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        if guess > number:
            print(f'wrong guess {guess} too low')
            high = guess - 1
        elif  guess < number:
            print(f'wrong guess {guess} too high')
            low = guess + 1
        elif  guess == number:
            feedback = 'correct'
            print(f'thats right {guess} is correct!')

#guess(20)
#computer_guess(1000)
autoGuessGame()