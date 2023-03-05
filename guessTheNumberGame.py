# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 20:50:17 2023

@author: Octavio
"""

logo = """
   _____                      _______  _            _   _                    _                 
  / ____|                    |__   __|| |          | \ | |                  | |                
 | |  __  _   _   ___  ___  ___ | |   | |__    ___ |  \| | _   _  _ __ ___  | |__    ___  _ __ 
 | | |_ || | | | / _ \/ __|/ __|| |   | '_ \  / _ \| . ` || | | || '_ ` _ \ | '_ \  / _ \| '__|
 | |__| || |_| ||  __/\__ \\__ \| |   | | | ||  __/| |\  || |_| || | | | | || |_) ||  __/| |   
  \_____| \__,_| \___||___/|___/|_|   |_| |_| \___||_| \_| \__,_||_| |_| |_||_.__/  \___||_|                                                                                        
"""
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
dificult = input("Choose a difficulty. Type 'easy' or 'hard': ")
anwser = random.randint(1, 100)
user_guess = 0
flag = True
if dificult == "easy":
    lifes = 10
elif dificult == "hard":
    lifes = 5
else:
    print("Please just type 'easy' or 'hard' nothing else")
    flag = False

while user_guess != anwser and flag:

    print(f"You have {lifes} attempts remaining to guess the number.")

    user_guess = int(input("Make a guess: "))

    if user_guess < anwser:
        print("too low")
        lifes -= 1
    elif user_guess > anwser:
        print("too high")
        lifes -= 1
    else:
        print(f"You got it! The answer was {anwser}.")
        break

    if lifes == 0:
        print("You've run out of guesses, you lose.")
        print(f"The number was {anwser}")
        break

    print("guess again")