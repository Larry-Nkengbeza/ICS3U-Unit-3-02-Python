# !/usr/bin/env python

# Created by Larry Nkengbeza
# Created on December 2020
# This program is a guessing game program


def main():
    # this funtion tells user if they guessed the right number

    # Input
    random_guess = int(input("Enter a number between 0 to 9: "))
    # Output
    print("")
    # process
    if random_guess == 9:
        # Output
        print("Correct! Good Job!")
    # Process
    if random_guess == 5:
        # Output
        print("Wrong!")
    # Process
    if random_guess == 1:
        # Output
        print("Wrong!")
    # Process
    if random_guess == 3:
        # Output
        print("Wrong!")
    # Process
    if random_guess == 4:
        # Output
        print("Wrong!")
    # Process
    if random_guess == 8:
        # Output
        print("Wrong!")
    # Process
    if random_guess == 7:
        # Output
        print("Wrong!")
    if random_guess == 2:
        # Output
        print("Wrong!")
    # Process
    if random_guess == 6:
        # Output
        print("Wrong!")


if __name__ == "__main__":
    main()
