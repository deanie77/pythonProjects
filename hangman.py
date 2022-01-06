import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    # getting user input
    while len(word_letters) > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have used these letters: ', ' '.join(used_letters))

        # what current word letters are (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:  # make sure letter hasn't already been used
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                if word_letters == set():
                    word_list = [letter if letter in used_letters else '-' for letter in word]
        elif user_letter in used_letters:
            print('You have already used the letter. Please try again.')
        else:
            print('You din\'t type in a valid letter.')

    print(''.join(word_list))


hangman()
