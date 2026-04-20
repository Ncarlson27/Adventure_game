'''
Contains information for the player charater and the possible classes as well as enemies and the final boss
'''

class Player:
    '''
    Provides the framwork of a player character.

    Use damage() to indicate how much damage the player takes

    Use heal() to indicate how much healing the player receives

    Use add_potion() to add a potion item to the player's inventory
    '''
    def __init__(self, name):
        self.name = name
        self.health = 12
        self.health_max = 12
        self.temp_hp = None
        self.level = 1
        self.inventory = []
        self.potions = []
        self.actions = []
        self.bonus_actions = []
        self.weapon = None
        self.armor_of_ice = False
        self.souls = None
        


    def damage(self, damage):
        '''
        Takes the damage passed and applies it to the player's health

        Checks if the player has temp hp, uses temp hp first
        '''
        if self.temp_hp is not None:
            if damage >= self.temp_hp:
                damage -= self.temp_hp
                
                self.temp_hp = None
                self.armor_of_ice = False

                self.health -= damage
                
            else:
                self.temp_hp -= damage
        else:
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
        Adds the potion passed to the player's potion supply
        '''
        self.potions.append(potion)
    

    def add_item(self, item):
        '''
        Adds the item passed to the player's inventory
        '''
        self.inventory.append(item)
    

    def equip_weapon(self, weapon):
        '''
        Equips a weapon
        '''

        try:
            old_weapon = self.weapon
            self.weapon = weapon
            weapon.equip(self)
            if old_weapon is not None:
                self.inventory.append(old_weapon)
                old_weapon.unequip(self)
            return True
        except:
            input(f"There was an error equiping {weapon}. Please try again.")


    def __str__(self):
        """
        Allows a player to be printed. Returns player's name
        """

        return self.name
        



class Fighter(Player):
    '''
    Sets the attack power and health of a fighter character besed on their level

    Use attack() to determine how much damage the character does

    Use level_up() to level up the character and set the new health and health_max
    '''

    def __init__(self, name):
        super().__init__(name)
        self.health = 24
        self.health_max = 24


    def level_up(self):
        '''
        Leveles up the character and increases their health and health_max
        '''
        self.level += 1
        self.health_max += 24
        self.health = self.health_max


class Rogue(Player):
    '''
    Sets the attack power and health of a rogue character besed on their level. Also has it start with a key

    Use attack() to determine how much damage the character does

    Use level_up() to level up the character and set the new health and health_max
    '''
    def __init__(self, name):
        super().__init__(name)
        self.health = 18
        self.health_max = 18
        self.keys = 1


    def level_up(self):
        '''
        Leveles up the character and increases their health and health_max
        '''
        self.level += 1
        self.health_max += 18
        self.health = self.health_max
