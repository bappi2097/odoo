from hangman_art import stages, logo
from hangman_words import word_list
import random

print(logo)
letter = random.choice(word_list).lower()
wrong_count = 7

blank = "_" * len(letter)
print(letter)
while True:
    if wrong_count == 0 or blank.find("_") == -1:
        if wrong_count == 0:
            print('You have lost')
        else:
            print('You have won')
        break
    else:
        char = input('Guess the letter: ')
        if len(char) != 1 or not char.isalpha():
            print("Character is not alphabet")
            continue
        elif char in letter:
            for n in range(len(letter)):
                if letter[n] == char:
                    letter = letter[0:n] + "_" + letter[n+1:]
                    blank = blank[0:n] + char + blank[n+1:]
                    if letter.find(char) == -1:
                        break
            print(blank)
        elif char in blank:
            print("Already insert this character")
        else:
            wrong_count-=1
            print(stages[wrong_count])
            print(blank)
    