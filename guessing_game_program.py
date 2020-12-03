# !/usr/bin/env python

# Created by Larry Nkengbeza
# Created on December 2020
# This program is a guessing game program

import constants


def main():
    # this funtion tells user if they guessed the right number

    # Input
    user_guess = int(input("Enter a number between 0 to 9: "))

    # Process
    if user_guess == constants.COMPUTER_GUESS:
        # Output
        print("Good guess you got it right")
        # Process
    if user_guess > constants.COMPUTER_GUESS:
        # Output
        print("Wrong, the answer you gave is incorrect")
        # Process
    if user_guess < constants.COMPUTER_GUESS:
        # Output
        print("Wrong, the answer you gave is incorrect")


if __name__ == "__main__":
    main()
