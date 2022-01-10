from words import words
from visuals import visuals
import string
import random

def get_word() -> str:
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_word()
    alpha_in_word = set(word)   # Letters in word
    alphabet = set(string.ascii_uppercase)
    alpha_used = set()          # Letters guess by user
    lives = 7

    # Getting User Input and making moves
    while (len(alpha_in_word) > 0) and (lives > 0):
        print(f"Lives left: {lives}, Used word: ", ' '.join(alpha_used))
    
        # Showing Current Words
        list1 = [letter if letter in alpha_used else '-' for letter in word]
        print(visuals[lives], "Current Progress:", ' '.join(list1))

        # Taking input
        temp = input('Enter your guess: ').upper()
        if temp not in alphabet - alpha_used:
            print('Guess already made')
        elif temp in alphabet - alpha_used:
            alpha_used.add(temp)
            if temp in alpha_in_word:
                print('Right Guess!!!')
                alpha_in_word.remove(temp)
            else:
                print('Wrong Guess!!!')
                lives -= 1
        else:
            print('Invalid Input')
    
    if lives == 0:
        print('Bad Luck!! Word was:', word)
    else:
        print('Hurray!!!')


if __name__ == "__main__":
    hangman()