"""
    Implement a guessing number game where the computer generates a random number between 1 and 100, 
    and the user must guess the number,
    the user has 5 tries and the game can tell if the number is lower or higher .
"""

from random import randint

tries = 0
number = randint(1, 100)


print("Welcome to the Guessing Number Game!")
print("I have selected a number between 1 and 100.")
print("You have 5 tries to guess the number.")

while tries < 5:
    print(f"Try {tries + 1}: Guess the number: ")
    try:
        guessed_number = int(input())
        if 0 >= guessed_number or guessed_number > 100:
            print("Enter a valid number from 1 to 100 😡.")
            continue 
        if guessed_number == number:
            print(f"🎉 3aaa4 <3, you guessed the number correctly.")
            break
        elif guessed_number < number:
            print(f"my number is higher than your number.")
        else:
            print(f"my number is lower than your number.")
        tries += 1
    except:
        print("Enter a valid number 😡.")


if tries >= 5:
    print(f"ya ragel 7ram 3leek, tries limit exceeds. better luck next time 😔.")
    print(f"the number is {number}.")
