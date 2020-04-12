# HL component 5 - statement generator

def hl_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))
    print()

# main routine

too_low = hl_statement("^^ Too low, try a higher number.    |    "
                       "Guesses Left: 3 ^^", "^")
print()
too_high = hl_statement("vv Too high, try a lower number.    |  "
                        "Guesses Left: 2 vv", "v")
print()
duplicate = hl_statement("!! You Already guessed that number    Please try agin.    |   "
                         "Guesses Left: 2 !!", "!")
print()
well_done = hl_statement("*** Well done! you got it in 3 guesses ***", "*")

print()
start_round = hl_statement("### Round 1 of 3 ###", "#")
