# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 12:10:44 2023

@author: Octavio
"""

import os
from art import logo
import random


def score_counter(players_cards):
    total = -1
    for i in range(len(players_cards)):
        total += players_cards[i]

    if total == 21:
        total = 0

    return total+1


def hand_generator(cards, deck, times=2):
    for i in range(times):
        deck.append(random.choice(cards))

    return deck


def compare(players_final_score, computer_final_score):
    if computer_final_score > 21 or player_final_score > computer_final_score:
        print("You win")
    elif player_final_score == computer_final_score:
        print("Draw")
    else:
        print("You lose")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
decision = "yes"
player_black_jack = False
computer_black_jack = False
while decision == "yes":
    players_cards = []
    computer_cards = []
    decision = input(
        'Do you want to play a blackjack game? Type "yes" or "no"\n')
    if decision == "no":
        break
    os.system("clear")
    print(logo)
    players_cards = hand_generator(cards, players_cards)
    computer_cards = hand_generator(cards, computer_cards)
    more_cards = "yes"
    while more_cards == "yes":
      if score_counter(players_cards) == 0 or score_counter(computer_cards) == 0:
          if score_counter(computer_cards):
              computer_black_jack = True
          if score_counter(players_cards):
              player_black_jack = True
          break
      print(f"Your cards: {players_cards} current score: {score_counter(players_cards)}")
      print(f"Computer's first card: {computer_cards[0]}")
      more_cards = input(
          'Type "yes" to get another card or "no" to pass: \n')
      if more_cards == "yes":
          hand_generator(cards, players_cards, 1)
          if score_counter(players_cards) > 21:
              break

    while score_counter(computer_cards) < 17:
        if player_black_jack or computer_black_jack:
            break
        hand_generator(cards, computer_cards, 1)

    if player_black_jack and computer_black_jack:
        print(f"Your Final cards: {players_cards} final score: 21")
        print(f"Computer's final cards: {computer_cards} final score: 21")
        print("Draw")
    elif player_black_jack:
        print(f"Your Final cards: {players_cards} final score: 21")
        print(
            f"Computer's final cards: {computer_cards} final score: {score_counter(computer_cards)}"
        )
        print("You win")
    elif computer_black_jack:
        print(
            f"Your Final cards: {players_cards} final score: {score_counter(players_cards)}"
        )
        print(f"Computer's final cards: {computer_cards} final score: 21")
        print("You lose")
    else:
        print(
            f"Your Final cards: {players_cards} final score: {score_counter(players_cards)}"
        )
        print(
            f"Computer's final cards: {computer_cards} final score: {score_counter(computer_cards)}"
        )

        if score_counter(players_cards) > 21:
            print("You lose")
        else:
            player_final_score = score_counter(players_cards)
            computer_final_score = score_counter(computer_cards)
            compare(player_final_score, computer_final_score)