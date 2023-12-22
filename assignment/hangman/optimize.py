from hangman_art import stages, logo
from hangman_words import word_list
import random

print(logo)

def display_word(word, guessed_letters):
    return ''.join(char if char in guessed_letters else '_' for char in word)

word_to_guess = random.choice(word_list)
guessed_letters = set()
wrong_count = 7

while True:
    if wrong_count == 0 or '_' not in display_word(word_to_guess, guessed_letters):
        print('You have', 'lost' if wrong_count == 0 else 'won')
        break

    print(display_word(word_to_guess, guessed_letters))

    guess = input('Guess the letter: ').lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet character.")
        continue

    if guess in guessed_letters:
        print("You've already guessed this letter.")
    elif guess in word_to_guess:
        guessed_letters.add(guess)
    else:
        wrong_count -= 1
        print(stages[wrong_count])

print("The word was:", word_to_guess)
