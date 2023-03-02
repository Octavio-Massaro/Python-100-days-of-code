# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 22:52:06 2023

@author: Octavio
"""

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

import art

def caesar(text, shift, direction):
    final_text = ""
    new_position = 0
    if direction == "encode" or direction == "decode":
        for letter in text:
            if letter in alphabet:
                position = alphabet.index(letter)
                if direction == "encode":
                    new_position = position + shift
                    if new_position > 25:
                        new_position -= 26
                elif direction == "decode":
                    new_position = position - shift
                final_text += alphabet[new_position]
            else:
                final_text += letter
        print(f"Here's the {direction}d result: {final_text}")
    else:
        print("Please, just chose encode or decode")


print(art.logo)

flag = True
while flag:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift > 26:
        shift = shift % 26
    caesar(text, shift, direction)
    decision = input(
        'Type "yes" if you want to go again or "no" to finish the program\n')
    if decision == "no":
        flag = False