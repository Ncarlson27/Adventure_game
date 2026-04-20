'''
Contains information for the player charater and the possible classes as well as enemies and the final boss
'''

from items import *

def dice(sides):
    '''
    simulates a die with a number of sides based on the variable passed into it
    '''
    return random.randint(1, sides)

class Player:
    '''
    Provides the framwork of a player character.

    Use damage() to indicate how much damage the player takes

    Use heal() to indicate how much healing the player receives

    Use add_potion() to add a potion item to the player's inventory
    '''
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.health_max = 10
        self.level = 1
        self.inventory = []
        self.keys = 0

    def damage(self, damage):
        '''
        Takes the damage passed and applies it to the player's health
        '''
        self.health -= damage

    def heal(self, healing):
        '''
        Takes the healing passed and applies it to the player's health. Doesn't go above the health_max
        '''
        new_health = self.health + healing
        if new_health < self.health_max:
            self.health = new_health
        elif new_health > self.health_max:
            self.health = self.health_max

    def add_potion(self, potion):
        '''
        Adds the potion passed to the player's inventory
        '''
        self.inventory.append(potion)


class Mage(Player):
    '''
    Sets the attack power and health of a mage character besed on it's level

    Use attack() to determine how much damage the character does

    Use level_up() to level up the character and set the new health and health_max
    '''
    def __init__(self, name):
        super().__init__(name)
        self.health = 12
        self.health_max = 12

    def attack(self):
        '''
        Determines how much damage the character does based on it's level
        '''
        if self.level == 1:
            damage = 0
            for i in range(3):
                damage += dice(8)
            return damage
        elif self.level == 2:
            damage = 0
            for i in range(5):
                damage += dice(8)
            return damage
        elif self.level == 3:
            damage = 0
            for i in range(8):
                damage += dice(8)
            return damage
        elif self.level == 4:
            damage = 0
            for i in range(10):
                damage += dice(8)
            return damage

    def level_up(self):
        '''
        Leveles up the character and increases it's health and health_max
        '''
        if self.level == 1:
            self.health = 24
            self.health_max = 24
            self.level += 1
        elif self.level == 2:
            self.health = 36
            self.health_max = 36
            self.level += 1
        elif self.level == 3:
            self.health = 48
            self.health_max = 48
            self.level += 1


class Fighter(Player):
    '''
    Sets the attack power and health of a fighter character besed on it's level

    Use attack() to determine how much damage the character does

    Use level_up() to level up the character and set the new health and health_max
    '''
    def __init__(self, name):
        super().__init__(name)
        self.health = 24
        self.health_max = 24

    def attack(self):
        '''
        Determines how much damage the character does based on it's level
        '''
        if self.level == 1:
            return dice(8) + 2
        elif self.level == 2:
            damage = 0
            for i in range(2):
                damage += (dice(8) + 3)
            return damage
        elif self.level == 3:
            damage = 0
            for i in range(3):
                damage += (dice(8) + 4)
            return damage
        elif self.level == 4:
            damage = 0
            for i in range(4):
                damage += (dice(8) + 5)
            return damage

    def level_up(self):
        '''
        Leveles up the character and increases it's health and health_max
        '''
        if self.level == 1:
            self.health = 48
            self.health_max = 48
            self.level += 1
        elif self.level == 2:
            self.health = 72
            self.health_max = 72
            self.level += 1
        elif self.level == 3:
            self.health = 96
            self.health_max = 96
            self.level += 1


class Rogue(Player):
    '''
    Sets the attack power and health of a rogue character besed on it's level. Also has it start with a key

    Use attack() to determine how much damage the character does

    Use level_up() to level up the character and set the new health and health_max
    '''
    def __init__(self, name):
        super().__init__(name)
        self.health = 18
        self.health_max = 18
        self.keys = 1

    def attack(self):
        '''
        Determines how much damage the character does based on it's level
        '''
        if self.level == 1:
            damage = dice(8)
            for i in range(2):
                damage += dice(6)
            crit = dice(20)
            if crit in (19, 20):
                damage = damage * 2
            return damage
        elif self.level == 2:
            damage = dice(8)
            for i in range(3):
                damage += dice(6)
            crit = dice(20)
            if crit in (18, 19, 20):
                damage = damage * 2
            return damage
        elif self.level == 3:
            damage = dice(8)
            for i in range(4):
                damage += dice(6)
            crit = dice(20)
            if crit in (17, 18, 19, 20):
                damage = damage * 2
            return damage
        elif self.level == 4:
            damage = dice(8)
            for i in range(5):
                damage += dice(6)
            crit = dice(20)
            if crit in (16, 17, 18, 19, 20):
                damage = damage * 2
            return damage

    def level_up(self):
        '''
        Leveles up the character and increases it's health and health_max
        '''
        if self.level == 1:
            self.health = 36
            self.health_max = 36
            self.level += 1
        elif self.level == 2:
            self.health = 54
            self.health_max = 54
            self.level += 1
        elif self.level == 3:
            self.health = 72
            self.health_max = 72
            self.level += 1


class Enemy:
    '''
    Creates an enemy for the player to fight

    Use attack() to determine the damage that the enemy does

    use damage() to take the damage done by the character and apply it to the enemy's health
    '''
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name

    def attack(self):
        '''
        Determines the amount of damage done to the player character based on the enemy's power
        '''
        damage = 0
        for i in range(self.power):
            damage += dice(8)
        return damage + self.power

    def damage(self, damage):
        '''
        Takes the damage done to the enemy and applies it to it's health
        '''
        self.health -= damage

    def __str__(self):
        '''
        Allows the enemy to be printed by returning it's name
        '''
        return self.name


class FinalBoss(Enemy):
    '''
    Creates the final boss bassed

    Use attack() to determine how mnuch damage the final boss does to the player
    '''
    def __init__(self, health, power, name):
        super().__init__(health, power, name)

    def attack(self):
        '''
        Determines how much damage the final boss does based on it's power
        '''
        damage = 0
        for i in range(self.power):
            damage += dice(8)
        return round(damage * 1.5)
