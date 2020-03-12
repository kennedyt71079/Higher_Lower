
# Number Checking function
def intcheck(question, low = None, high = None):

    # sets  up error messages
    if low is not None and high is not None:
        error = "Please enter an interger between {} and {} " \
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

# Main routine

    lowest = intcheck("Low Number: ")
    highest = intcheck("High Number: ", lowest + 1)
    rounds = intcheck("Rounds: ", 1)
    guess = intcheck("Guess: ", lowest, highest)
