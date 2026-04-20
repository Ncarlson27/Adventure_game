from dice import dice
from abc import ABC, abstractmethod
from spells import *


class Weapon(ABC):

    def __init__(self):
        self.name = None
        self.attack = None

    @abstractmethod
    def use(self, player, enemy):
        ...
    
    @abstractmethod
    def equip(self, player):
        ...
    
    @abstractmethod
    def unequip(self, player):
        ...

    def __str__(self):
        return self.name


class LightningStaff(Weapon):

    def __init__(self):
        self.name = "Staff of lightning"
        self.attack = LightningBolt()

    def use(self, player, enemy):
        self.attack.use(player, enemy)
    
    def equip(self, player):
        player.actions.append(self.attack)
    
    def recharge(self):
        if self.attack.uses != self.attack.max_uses:
            self.attack.uses += 1
            input("Your weapon gained 1 use. ")

    def unequip(self, player):
        for i in range(len(player.actions)):
            if player.actions[i].name == "Lightning bolt":
                del player.actions[i]



class FireballStaff(Weapon):

    def __init__(self):
        self.name = "Staff of fireball"
        self.attack = Fireball()

    def use(self, player, enemy):
        self.attack.use(player, enemy)
    
    def equip(self, player):
        player.actions.append(self.attack)
    
    def recharge(self):
        if self.attack.uses != self.attack.max_uses:
            self.attack.uses += 1
            input("Your weapon gained 1 use. ")

    def unequip(self, player):
        for i in range(len(player.actions)):
            if player.actions[i].name == "Fireball":
                del player.actions[i]


class FireboltStaff(Weapon):

    def __init__(self):
        self.name = "Staff of lightning"
        self.attack = Firebolt()

    def use(self, player, enemy):
        self.attack.use(player, enemy)
    
    def equip(self, player):
        player.actions.append(self.attack)
    
    def recharge(self):
        if self.attack.uses != self.attack.max_uses:
            self.attack.uses += 1
            input("Your weapon gained 1 use. ")

    def unequip(self, player):
        for i in range(len(player.actions)):
            if player.actions[i].name == "Firebolt":
                del player.actions[i]
