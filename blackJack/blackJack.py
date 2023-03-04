# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 12:10:44 2023

@author: Octavio
"""

import os
from art import logo
import random


def score_counter(players_cards):
    total = 0
    for i in range(len(players_cards)):
        total += players_cards[i]
        
    if total == 21:
        total = 0

    return total


def hand_generator(cards, deck, times=2):
    for i in range(times):
        deck.append(random.choice(cards))

    return deck


def compare(players_final_score,computer_final_score):
  if computer_final_score > 21 or player_final_score > computer_final_score:
    print("You win")
  elif player_final_score == computer_final_score:
    print("Draw")
  else:
    print("You lose")
    

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
decision = "yes"
while decision == "yes":
    players_cards = []
    computer_cards = []
    decision = input('Do you want to play a blackjack game? Type "yes" or "no"\n')
    if decision == "no":
      break
    os.system("clear")
    print(logo)
    players_cards = hand_generator(cards, players_cards)
    computer_cards = hand_generator(cards, computer_cards)
    more_cards = "yes"
    while more_cards == "yes":
        if score_counter(players_cards) == 0:
            break
        
        print(f"Your cards: {players_cards} current score: {score_counter(players_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")
        more_cards = input('Type "yes" to get another card or "no" to pass: \n')
        if more_cards == "yes":
          hand_generator(cards,players_cards,1)
          if score_counter(players_cards) > 21:
            break
        
      
    while score_counter(computer_cards) < 17:
        hand_generator(cards, computer_cards, 1)

    print(f"Your Final cards: {players_cards} final score: {score_counter(players_cards)}")
    print(f"Computer's final cards: {computer_cards} final score: {score_counter(computer_cards)}")

    if score_counter(players_cards) > 21:
      print("You lose")
    else:
      player_final_score = score_counter(players_cards)
      computer_final_score = score_counter(computer_cards)
      compare(player_final_score,computer_final_score)