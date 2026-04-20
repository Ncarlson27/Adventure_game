from items import *

class Gift:
    '''
    Simulates the player opening a treasure chest and finding an item inside

    Use run_event() to run the event
    '''
    def __init__(self, number, player):
        self.number = number
        self.player = player

    def run_event(self):
        '''
        Randomly determines what the player finds
        Potions get stronger as the room level increases
        '''
        input("You enter the room and find an open treasure chest ")
        input("You decide to look inside ")
        if self.number in (0, 1, 2, 3):
            self.player.add_potion(Potion('potion (2d8 + 2)'))
            input('You got a potion!')
            return True
        elif self.number in (4, 5, 6):
            self.player.add_potion(Potion('greater potion (4d8 + 4)'))
            input('You got a greater potion!')
            return True
        elif self.number in (7, 8, 9):
            self.player.add_potion(Potion('superior potion (6d8 + 6)'))
            input('You got a superior potion!')
            return True