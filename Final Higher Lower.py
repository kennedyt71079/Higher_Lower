# Higher Lower

import random

# ask for values
lowest = int(input("Please enter a low number: "))

# verify values are valid
if lowest < 1:
    print("Your number is too low, try again ")

highest = int(input("Please enter a high number: "))

if highest < lowest:
    print("Your number is too low, Try again ")

guesses_allowed = int(input("How many guesses do you want: "))

# Generate random number
random_num = random.randrange(lowest, highest)

# initialise variables
already_guessed = []
guesses = 0
guess = ""

# start game
while guess != random_num and guesses_allowed >= 1:

    guess = int(input("Guess: "))

# checks that guess is not a duplicate
    if guess in already_guessed:
        print("You already guessed that number! Please try again. "
              "You *still* have {} guesses left".format(guesses_allowed))
        continue

    if guess < lowest or guess > highest:
        print()
        print("Your guess is not between {} and {}, Try again".format(lowest,highest))
        continue

    guesses_allowed -=1
    already_guessed.append(guess)

    # if user has guesses left
    if guesses_allowed >= 1:

        if guess < random_num:
            print("^^^ Too low, try a higher number. Guesses left: {} ^^^".format(guesses_allowed))

        elif guess > random_num:
            print("vvv Too high, try a lower number. Guesses left: {} vvv".format(guesses_allowed))
    guesses += 1

if guess == random_num:
    if guesses_allowed == guesses_allowed - 1:
        print("!!!Amazing! you got it in one guess!!!")
    else:
        print("!!!Well done, you got it in {} guesses!!!".format(guesses))

else:
    print("Sorry, you lose this game as you have run out of guesses")
    print("The number was {}".format(random_num))
