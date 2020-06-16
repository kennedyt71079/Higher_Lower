# HL component 3 - compares user guess with secret number

secret = 7
guesses_allowed = 4

# initialise variables
already_guessed = []
guesses_left = guesses_allowed
num_won = 0
guess = ""

# start game
while guess != secret and guesses_left >= 1:

    guess = int(input("Guess: "))

# checks that guess is not a duplicate
    if guess in already_guessed:
        print("You already guessed that number! Please try again. "
              "You *still* have {} guesses left".format(guesses_left))
        continue

    guesses_left -=1
    already_guessed.append(guess)

    # if user has guesses left
    if guesses_left >= 1:

        if guess < secret:
            print("Too low, try a higher number. Guesses left: {}".format(guesses_left))

        elif guess > secret:
            print("Too high, try a lower number. Guesses left: {}".format(guesses_left))
    else:
        if guess < secret:
            print("Too low")
        elif guess > secret:
            print("Too high")

if guess == secret:
    if guesses_left == guesses_allowed - 1:
        print("Amazing! you got it in one guess")
    else:
        print("Well done, you got it in {} guesses".format(len(already_guessed)))
    num_won += 1
else:
    print("Sorry, you lose this round as you have run out of guesses")
