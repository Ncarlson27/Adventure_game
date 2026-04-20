from player import Player
from spells import *

class Mage(Player):
    '''
    Sets the attack power and health of a mage character besed on their level

    Use attack() to determine how much damage the character does

    Use level_up() to level up the character and set the new health and health_max
    '''

    def __init__(self, name):
        super().__init__(name)
        self.actions = [Firebolt()]
        self.bonus_actions = [FrostRay(), MagicMissle(), FrostArmor()]


    def level_up(self):
        '''
        Levels up the character and increases its health and health_max
        '''
        self.level += 1
        self.health_max += 12
        self.health = self.health_max
        self.temp_hp = None

        for action in self.actions:
            if action.uses is not None:
                action.max_uses += 1
        
        for bonus in self.bonus_actions:
            if bonus.uses is not None:
                bonus.max_uses += 1

        if self.level == 2:
            self.actions.append(Fireball())
        
        if self.level == 4:
            self.actions.append(Disintegrate())
            

        for action in self.actions:
            if action.uses is not None:
                action.uses = action.max_uses
        
        for action in self.bonus_actions:
            if action.uses is not None:
                action.uses = action.max_uses