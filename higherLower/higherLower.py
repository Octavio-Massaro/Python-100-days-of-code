# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 14:39:48 2023

@author: Octavio
"""

from game_data import data
from art import logo,vs
import random
import os

data_length = len(data)
def compare(option1,option2,decision):
  flag = False
  if option1[1] > option2[1] and decision == "A":
    print("Passei")
    flag = True
  elif option1[1] < option2[1] and decision == "B":
    print("passei")
    flag = True
  else:
    flag = False

  return flag

def create_list(data,position):
  list = []
  for item in data[position]:
    list.append(data[position][item])
    
  return list
  
score = 0
first_iteration = True
option2 = []
while True:
  print(logo)
  if score > 0:
    print(f"You're right! Current score: {score}.")
  position1 = random.randint(0,data_length-1)
  if first_iteration:
    option1 = create_list(data,position1)
    first_iteration = False
  else:
    option1 = option2
  
  print(f"Compare A: {option1[0]}, a {option1[2]}, from {option1[3]}.")
  
  print(vs)
  
  position2 = random.randint(0,data_length-1)
  option2 = create_list(data,position2)

  while option2 == option1:
    option2 = create_list(data,position2)

  
  print(f"Against B: {option2[0]}, a {option2[2]}, from {option2[3]}.")
  
  decision = input("Who has more followers? Type 'A' or 'B':")
  if decision != "A" or decision != "B":
    os.system("clear")
    print("Please just Type 'A' or 'B'")
    break
  
  result = compare(option1,option2,decision)
  
  if result:
    os.system("clear")
    score += 1
  else:
    os.system("clear")
    print(f"Sorry, that's wrong. Final score: {score}")
    break