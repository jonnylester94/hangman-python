import random

from words import words, alph


def get_valid_word(words):
    word = random.choice(words) # randomly chooses a word from imported list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(alph)
    used_letters = set() # to keep track of what the user has guessed

    lives = 7

    # get user input
    while len(word_letters) > 0 and lives > 0:
        #letters used
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # current word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))


        user_letter = input('Choose a letter: ')
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                print('Correct!')
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print('Letter is not in word.')

        elif user_letter in used_letters:
            print('You have already guessed that letter. Try again.')

        else:
            print('Invalid character.')
    
    if lives == 0:
        print('You lost, sorry. The word was', word)
    
    else:
        print('You guessed the word', word, '! Well done!')
    

hangman()



