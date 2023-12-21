import random

# Single-point crossover
def crossover(p1, p2, r_cross):
    # check for recombination
    if random.random() < r_cross:
        # select crossover point that is not on the end of the string
        pt = random.randint(1, len(p1) - 2)
        # perform crossover
        c1 = p1[:pt] + p2[pt:]
        c2 = p2[:pt] + p1[pt:]
    else:
        # children are slices of parents by default
        c1, c2 = p1[:], p2[:]
    return c1, c2

print(crossover(["Hi", "Bye", "Good", "Bad"], ["Hello", "World", "Open", "Mesh"], 0.9))