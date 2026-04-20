'''
Contains information for the potion item
'''

import random

def dice(sides):
    '''
    simulates a die with a number of sides based on the variable passed into it
    '''
    return random.randint(1, sides)    


class Potion:
    '''
    Creates a potion item and based on it's name wil have different strength

    Use effect() to determine the healing done to the player character
    '''
    def __init__(self, name):
        self.name = name

    def effect(self):
        '''
        Determines the amount of healing done to the player character
        '''
        if self.name == 'potion (2d8 + 2)':
            healing = 0
            for i in range(2):
                healing += dice(8)
            return healing + 2
        elif self.name == 'greater potion (4d8 + 4)':
            healing = 0
            for i in range(4):
                healing += dice(8)
            return healing + 4
        elif self.name == 'superior potion (6d8 + 6)':
            healing = 0
            for i in range(6):
                healing += dice(8)
            return healing + 6
        elif self.name == 'ultimate potion (8d8 + 8)':
            healing = 0
            for i in range(8):
                healing += dice(8)
            return healing + 8

    def __str__(self):
        '''
        Allows the potion to be printed by returning its name
        '''
        return self.name
