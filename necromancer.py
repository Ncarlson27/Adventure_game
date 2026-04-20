from player import Player
from spells import *

class Necromancer(Player):
    '''
    Sets the attack power and health of a mage character besed on their level

    Use attack() to determine how much damage the character does

    Use level_up() to level up the character and set the new health and health_max
    '''

    def __init__(self, name):
        super().__init__(name)
        self.actions = [EldritchBlast(), RayOfSickness(), SummonSkeleton()]
        self.bonus_actions = [FrostRay(), FrostArmor(), SoulSiphon()]
        self.health_max = 14
        self.health = 14
        self.souls = 1
        self.minions = 0


    def level_up(self):
        '''
        Levels up the character and increases their health and health_max
        '''
        self.level += 1
        self.health_max += 16
        self.health = self.health_max
        self.temp_hp = None
        self.armor_of_ice = False


        if self.level == 2:
            self.bonus_actions.append(Hex())


        if self.level == 3:
            self.actions.append(Blight())
        
        if self.level == 4:
            self.actions.append(AbsorbHealth())

        for action in self.actions:
            if action.uses is not None:
                action.uses = action.max_uses
        
        for action in self.bonus_actions:
            if action.uses is not None:
                action.uses = action.max_uses