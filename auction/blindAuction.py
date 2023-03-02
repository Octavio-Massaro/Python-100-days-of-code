# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 20:02:18 2023

@author: Octavio
"""

from replit import clear
import art

bid_list = []
print(art.logo)
print("Welcome to the secret auction program")
condition = "yes"
while condition != "no":
    name = input(" What is your name?: \n")
    bid = int(input("What is your bid?: $"))
    condition = input("Are there any other bidders? Type 'yes' or 'no'\n")
    bid_list.append({"name": name, "bid": bid})
    clear()

max_var = bid_list[0]["bid"]
index = 0
for i in range(len(bid_list)):
    if max_var < bid_list[i]["bid"]:
        max_var = bid_list[i]["bid"]
        index = i

winner_name = bid_list[index]["name"]
winner_bid = bid_list[index]["bid"]
print(f"The winner is {winner_name} with a bid of ${winner_bid}")