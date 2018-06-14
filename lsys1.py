# Lindenmayer L-System
# by Daniel Miller
# June 2018

# from https://en.wikipedia.org/wiki/L-system

# Lindenmayer's original L-system for modelling the growth of algae.
# - variables : A B
# - constants : none
# - axiom  : A
# - rules  : (A → AB), (B → A)

import sys

initiator = sys.argv[1]
n = sys.argv[2]

lSystem = list(initiator)
counter = 0

def Rules(oldList):
    global counter
    newList = []
    for letter in oldList:
        if (letter == "A"):
            newList.extend(["A", "B"])
            oldList = newList
        elif (letter == "B"):
            newList.extend("A")
            oldList = newList
        else:
            print("Error: wrong input")
            sys.exit()
    counter += 1
    return oldList

while counter < int(n):
    print(f"n={counter}: {lSystem}")
    lSystem = Rules(lSystem)
