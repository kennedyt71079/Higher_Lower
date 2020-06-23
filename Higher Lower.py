# Higher Lower

import random

# initialise variables
already_guessed = []
guesses = 0
guess = ""

# Number Checking function
def intcheck(question, low=None, high=None):

    # sets  up error messages
    if low is not None and high is not None:
        error = "Please enter an integer between {} and {} " \
                "(inclusive)".format(low, high)
    elif low is not None and high is None:
        error = "Please enter an integer that is more than or " \
                "equal to {}".format(low)
    elif low is None and high is not None:
        error = "Please enter an integer that is less than or " \
                "equal to {}".format(high)
    else:
        error = "Please enter an integer"

    while True:

        try:
            response = int(input(question))

            # checks response is not too low
            if low is not None and response < low:
                print(error)
                continue

            # checks response is not too high
            if high is not None and response > high:
                print(error)
                continue

            return response

        except ValueError:
            print(error)
            continue

# Main Routine
low = intcheck("Low Number: ")
highest = intcheck("High Number: ", low + 1)
guesses_allowed = intcheck("Guesses allowed: ")

# Generate random number
random_num = random.randrange(low, highest)

# start game
while guess != random_num and guesses_allowed >= 1:

    # checks that guess is not a duplicate
    def intcheck(question, guess=None):

        # sets  up error messages
        if guess is not None:
            error = "Please enter an integer between {} and {} " \
                    "(inclusive)".format(low, high)

        else:
            error = "Please enter an integer"

        while True:

            try:
                response = int(input(question))

                # checks response is not too low
                if low is not None and response < low:
                    print(error)
                    continue

                # checks response is not too high
                if high is not None and response > high:
                    print(error)
                    continue

                return response

            except ValueError:
                print(error)
                continue


    guesses_allowed -= 1
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
