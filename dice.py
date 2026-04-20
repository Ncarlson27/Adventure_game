import random

def dice(sides, times = 1):
    '''
    simulates a die with a number of sides based on the variable passed into it
    '''

    total = 0

    for _ in range(times):
        total += random.randint(1, sides)

    return total