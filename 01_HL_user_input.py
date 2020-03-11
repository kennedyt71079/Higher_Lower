
# Number Checking function
def intcheck(question, low = None, high = None):

# Main routine

    lowest = intcheck("Low Number: ")
    highest = intcheck("High Number: ", lowest + 1)
    rounds = intcheck("Rounds: ", 1)
    guess = intcheck("Guess: ", lowest, highest)