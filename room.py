'''
Contains information about the various rooms possible in the game.
'''

from combat_room import Combat
from gift_room import Gift

class Room:
    '''
    Creates a room with a chosen event and the room number in the dungeon

    Use create_event() to create an instance of the chosen event 
    '''
    def __init__(self, event, number, player):
        self.event = event
        self.number = number
        self.player = player

    def create_event(self):
        '''
        Creates an instance of the room's chosen event
        '''
        if self.event == 'combat':
            return Combat(self.number, self.player)
        elif self.event == 'gift':
            return Gift(self.number, self.player)



