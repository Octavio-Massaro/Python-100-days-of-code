# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 20:52:34 2023

@author: Octavio
"""

import random
import hangman_art
import hangman_words

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
used_words = []
end_of_game = False
lives = 6

print(hangman_art.logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#Join all the elements in the list and turn it into a String.
print(f"{' '.join(display)}\n")

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in used_words:
      print(f"You already guessed the letter {guess}. Try another letter")
      continue
      
    used_words += guess
  
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
      print(f"the letter {guess} is not in the secret word")
      lives -= 1
      if lives == 0:
          end_of_game = True
          print("You lose.")

    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])