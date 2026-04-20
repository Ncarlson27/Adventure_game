from dice import dice

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
        self.conditions = {}
        self.end_conditions = {}

    def attack(self):
        '''
        Determines the amount of damage done to the player character based on the enemy's power
        '''
        return dice(10, self.power) + self.power


    def damage(self, damage):
        '''
        Takes the damage done to the enemy and applies it to its health
        '''
        
        self.health -= damage


    def __str__(self):
        '''
        Allows the enemy to be printed by returning its name
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
        return round(dice(10, self.power) * 1.5)
    


