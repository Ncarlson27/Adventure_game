from items import *
from enemies import Enemy, FinalBoss
from necromancer import *


class Combat:
    '''
    Creates an enemy for the player to fight and runs combat

    Use run_event to run combat
    '''
    def __init__(self, number, player):
        self.number = number
        self.player = player
        self.enemy = None
    

    def bonus_actions(self):
        if self.player.temp_hp is None:
            print(f'Your health = {self.player.health}\nEnemy health = {self.enemy.health} ')
        else:
            print(f'Your health = {self.player.health} + {self.player.temp_hp} temp hp\nEnemy health = {self.enemy.health} ')
        counter = 1
        for action in self.player.bonus_actions:
            if action.uses is None:
                print(f'{counter}: {action}')
            else:
                print(f'{counter}: {action} Uses: {action.uses}')
            counter += 1
        bonus_choice = input("What bonus action will you use? (0 to skip): ")
        try:
            bonus_choice = int(bonus_choice)
            if bonus_choice == 0:
                return True
            elif bonus_choice <= len(self.player.bonus_actions) and self.player.bonus_actions[bonus_choice - 1].uses != 0:
                action = self.player.bonus_actions[bonus_choice - 1]
                action.use(self.player, self.enemy)
                return True
            else:
                valid = False
                print('Please enter a valid choice')
                return valid
        except ValueError:
            valid = False
            print('Please enter a valid choice')
            return valid

    
    def actions(self):
        counter = 1
        for action in self.player.actions:
            if action.uses is None:
                print(f'{counter}: {action}')
            else:
                print(f'{counter}: {action} Uses: {action.uses}')
            counter += 1
        action_choice = input('Which action would you like to use? (0 to exit): ')

        try:
            action_choice = int(action_choice)
            if action_choice == 0:
                pass
            elif action_choice <= len(self.player.actions) and self.player.actions[action_choice - 1].uses != 0:
                action = self.player.actions[action_choice - 1]
                action.use(self.player, self.enemy)
                return True
            else:
                valid = False
                print('Please enter a valid choice')
                return valid
        except ValueError:
            valid = False
            print('Please enter a valid choice')
            return valid


    def menu(self):
        while True:
            if self.player.temp_hp is None:
                choice = input(f'Your health = {self.player.health}\nEnemy health = {self.enemy.health}\nWhat will you do?\n1: Attack\n2: Defend\n3: Item\n')
            else:
                choice = input(f'Your health = {self.player.health} + {self.player.temp_hp} temp hp\nEnemy health = {self.enemy.health}\nWhat will you do?\n1: Attack\n2: Defend\n3: Item\n')
            if choice == '1':
                valid = True
                bonus_valid = True

                valid = self.actions()

                if valid and self.enemy.health <= 0:
                    input(f'Enemy {self.enemy} was defeated! ')
                    self.player.weapon.recharge()
                    if isinstance(self.player, Necromancer):
                        self.player.souls += 1
                        input('You gained a soul to use. ')
                    break

                bonus_valid = self.bonus_actions()

                if bonus_valid:
                    if self.enemy.health <= 0:
                        input(f'Enemy {self.enemy} was defeated! ')
                        self.player.weapon.recharge()
                        if isinstance(self.player, Necromancer):
                            self.player.souls += 1
                            input('You gained a soul to use. ')
                        break

                damage = self.enemy.attack()
                input(f'Enemy {self.enemy} attacked you for {damage} damage! ')
                damage_result = self.player.damage(damage)
                if damage_result == 1:
                    input(f'Enemy {self.enemy} took {10 * self.player.level} damage from your armor of frost! ')
                    self.enemy.damage(10 * self.player.level)
                    if self.enemy.health <= 0:
                        input(f'Enemy {self.enemy} was defeated! ')
                        break
                
                if self.enemy.is_poisoned():
                    damage = dice(6, self.enemy.poison_damage)
                    input(f'Enemy {self.enemy} took {damage} damage from poison! ')
                    self.enemy.damage(damage)
                    if self.enemy.health <= 0:
                        input(f'Enemy {self.enemy} was defeated! ')
                        break

                if self.player.health <= 0:
                    print('You died!')
                    return 'player dead'
            elif choice == '2':
                input(f'{self.enemy} attacked for {self.enemy.attack()} damage but you managed to block it ')
            elif choice == '3':
                counter = 1
                if len(self.player.potions) == 0:
                    input('You have no potions ')
                else:
                    for item in self.player.potions:
                        print(f'{counter}: {item}')
                        counter += 1
                item_choice = input('Which item would you like to use? (0 to exit): ')
                try:
                    item_choice = int(item_choice)
                    if item_choice == 0:
                        pass
                    elif item_choice <= len(self.player.potions):
                        item = self.player.potions.pop(item_choice - 1)
                        healing = item.effect()
                        self.player.heal(healing)
                        input(f'You used {item.name} and were healed for {healing}! ')
                    else:
                        print('Please enter a valid choice')
                except ValueError:
                    print('Please enter a valid choice')



    def run_event(self):
        '''
        Creates an enemy based on the room number and the runs through combat with the various choices possible

        Player can attack and do damage, but will also take damage
        Player can defend to take no damage from the enemy
        Player can use a potion that the have to heal, will not take damage that turn
        '''
        if self.number in (0, 1, 2, 3):
            self.enemy = Enemy(32, 1, 'Goblin')
        elif self.number in (4, 5, 6):
            self.enemy = Enemy(64, 2, 'Hobgoblin')
        elif self.number in (7, 8, 9):
            self.enemy = Enemy(96, 3, 'Goblin chief')
        elif self.number == 10:
            self.enemy = FinalBoss(700, 4, 'Elric, King of the Goblins')
        
        if self.number < 10:
            input(f'Enemy {self.enemy} has appeared! ')
        elif self.number == 10:
            input(f'Final boss {self.enemy} has appeared! ')
        
        self.menu()
                    
