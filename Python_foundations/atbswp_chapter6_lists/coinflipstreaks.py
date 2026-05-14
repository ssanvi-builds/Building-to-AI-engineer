import random

SIX_HEADS = ["H", "H", "H", "H", "H", "H"]
SIX_TAILS = ["T", "T", "T", "T", "T", "T"]

streak_count = 0

for i in range(10000):
    throws = []
    j = 0
    while len(throws) != 100:
        throws.append(random.choice(["H","T"]))
    while j < 93:
        if throws[j:j+6] == SIX_HEADS or throws[j:j+6] == SIX_TAILS:
            streak_count += 1
            j += 6
        else:
                j += 1

print("There's been " + str(streak_count) + " occurrences of a sequence of six heads or tails in a row")