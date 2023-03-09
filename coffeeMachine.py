# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 22:19:49 2023

@author: Octavio
"""

#I need to revise this project later
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report_ingredients(money):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]

    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}ml")
    print(f"Money: ${money:.2f}")


def consume_ingredints(drink):
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
    if drink != "espresso":
        resources["milk"] -= MENU[drink]["ingredients"]["milk"]


def enough_resource(drink):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    water_left = water - MENU[drink]["ingredients"]["water"]
    milk_left = milk - MENU[drink]["ingredients"]["milk"]
    coffee_left = coffee - MENU[drink]["ingredients"]["coffee"]
    if water_left < 0:
        print("Not enough water")
        return False
    elif coffee_left < 0:
        print("Not enough coffee")
        return False
    elif milk_left < 0:
        print("Not enough milk")
        return False
    else:
        return True


valid_choices = ["espresso", "latte", "cappuccino", "report"]
flag = True
change = 0.0
while flag:
    choice = input("What would you like? (espresso,latte/cappuccino): ")

    if choice == "report":
        report_ingredients(change)
        continue
    if choice not in valid_choices:
        print("You didn't provide a valid choice of Coffee. Please try again")
        continue

    print("Please insert coins")
    number_quarters = float(input("How many quarters: "))
    number_dimes = float(input("How many dimes: "))
    number_nickles = float(input("How many nickles: "))
    number_pennies = float(input("How many pennies: "))
    change = (number_dimes * 0.1) + (number_nickles * 0.05) + (
        number_pennies * 0.01) + (number_quarters * 0.25)
    enough = enough_resource(choice)

    if not enough:
        print("Try another coffee")
        continue

    if choice == "espresso" and change >= 1.5:
        consume_ingredints(choice)
        change -= 1.5
        print("Heres is you espresso, enjoy")
    elif choice == "latte" and change >= 2.5:
        consume_ingredints(choice)
        change -= 2.5
        print("Heres is you Latte, enjoy")
    elif choice == "cappuccino" and change >= 3.0:
        consume_ingredints(choice)
        change -= 3.0
        print("Heres is you Cappuccino, enjoy")
    else:
        print(f"Not enough money {change}")