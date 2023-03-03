# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 14:49:26 2023

@author: Octavio
"""

from art import logo
import os

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

print(logo)

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide 
}
end = True
while end == True:
    try:
        n1 = float(input("What's the first number?:\n"))
        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation: \n")
        if operation not in operations:
            os.system("clear")
            print("Please, give a valid operation")
            continue
        n2 = float(input("What's the second number?:\n"))
    except:
        print("You didn't provide a valid number. Please try again")
        break
    calculation_function = operations[operation]
    result = calculation_function(n1, n2)
    print(f"{n1} {operation} {n2} = {result}")
    choice = input(
        f'Type "yes" to continue calculating with {result} or type "no" to start a new calculation or "end" to close the program:\n'
    )
    choice = choice.lower()
    if choice == "no":
        os.system("clear")
    elif choice == "yes":
        while choice == "yes":
            try:
                operation = input("Pick an operation: \n")
                if operation not in operations:
                    os.system("clear")
                    print("Please, give a valid operation")
                    continue
                n3 = float(input("What's the next number?\n"))
            except:
                print("You didn't provide a valid number. Please try again")
            temp = result
            calculation_function = operations[operation]
            result = calculation_function(result, n3)
            print(f"{temp} {operation} {n3} = {result}")
            choice = input(
                f'Type "yes" to continue calculating with {result} or type "no" to start a new calculation or "end" to close the program:\n'
            )
            if choice == "no":
                os.system("clear")
            elif choice == "end":
                end = False
                break
            elif choice == "yes":
              continue
            else:
                os.system("clear")
                print(
                    'You did not type "yes", "no" or "end". So by default we picked "no"'
                )
    elif choice == "end":
        break
    else:
        os.system("clear")
        print(
            'You did not type "yes", "no" or "end". So by default we picked "no"'
        )