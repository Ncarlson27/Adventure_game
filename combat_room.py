from items import *
from necromancer import Necromancer
from enemies import Enemy, FinalBoss

'''
Functions
    Show player and enemy information
    Show attack, defend, and item
    Actions
    Bonus actions
    Damage
    Check end of turn effects and damage effects

QOL
    Make incorect inputs recursivly call the function


'''


class Combat:
    '''
    Creates an enemy for the player to fight and runs combat

    Use run_event to run combat
    '''
    def __init__(self, number, player):
        self.number = number
        self.player = player
        self.enemy = None
    

    def show_combat_info(self):
        souls = self.player.souls
        if souls is not None:
            souls = f"\nSouls = {souls}"
        else:
            souls = ''

        if self.player.temp_hp is None:
            print(f'Your health = {self.player.health}\nEnemy health = {self.enemy.health}{souls}\n')
        else:
            print(f'Your health = {self.player.health} + {self.player.temp_hp} temp hp\nEnemy health = {self.enemy.health}{souls}\n')


    def check_player_dead(self):
        if self.player.health <= 0:
            return True
        
        return False


    def check_enemy_dead(self):
        if self.enemy.health <= 0:
            return True
        
        return False


    def end_of_turn(self, condition):
        damage, intensitiy = self.enemy.end_conditions[condition]

        damage = dice(damage, intensitiy)

        self.enemy.damage(damage)
        input(f'Enemy {self.enemy.name} took {damage} damage from {condition}')


    def on_damage(self, condition):
        damage, intensitiy = self.enemy.conditions[condition]

        damage = dice(damage, intensitiy)

        self.enemy.damage(damage)
        input(f'Enemy {self.enemy.name} took {damage} damage from {condition}')


    def do_damage(self, action):
        action.use(self.player, self.enemy)
        
        if action.does_damage() and self.enemy.conditions:
            for condition in self.enemy.conditions.keys():
                self.on_damage(condition)


    def enemy_attack(self):
        damage = self.enemy.attack()
        input(f'Enemy {self.enemy} attacked you for {damage} damage! ')
        if self.player.armor_of_ice:
            input(f'Enemy {self.enemy} took {10 * self.player.level} damage from your armor of frost! ')
            self.enemy.damage(10 * self.player.level)
        
        self.player.damage(damage)


    def item_menu(self):
        '''
        Shows the player a list of their items. If they have no items then returns to menu
        Gets player input and uses the item if able
        '''
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
                # TODO
                # Maybe have the enemy attack or change this to a bonus action
                # This is currently very broken. Makes it very hard to die.
            else:
                print('Please enter a valid choice')
                
        except ValueError:
            print('Please enter a valid choice')
            


    def guard(self):
        '''
        Guards against the enemy's attack
        '''
        # TODO
        # Make this more interesting
        input(f'{self.enemy} attacked for {self.enemy.attack()} damage but you managed to block it ')
        


    def bonus_action_menu(self):
        '''
        
        '''
        self.show_combat_info()

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
                return
            elif bonus_choice <= len(self.player.bonus_actions) and self.player.bonus_actions[bonus_choice - 1].uses != 0:
                action = self.player.bonus_actions[bonus_choice - 1]
                self.do_damage(action)
            else:
                print('Please enter a valid choice')
                self.bonus_action_menu()
                return
        except ValueError:
            print('Please enter a valid choice')
            self.bonus_action_menu()
            return



    def action_menu(self):
        '''
        
        '''
        self.show_combat_info()

        counter = 1
        for action in self.player.actions:
            if action.uses is None:
                print(f'{counter}: {action}')
            else:
                print(f'{counter}: {action} Uses: {action.uses}')
            counter += 1
        action_choice = input('Which action would you like to use? (0 to skip): ')

        try:
            action_choice = int(action_choice)
            if action_choice == 0:
                return
            elif action_choice <= len(self.player.actions) and self.player.actions[action_choice - 1].uses != 0:
                action = self.player.actions[action_choice - 1]
                self.do_damage(action)
            else:
                print('Please enter a valid choice')
                self.action_menu()
                return
        except ValueError:
            print('Please enter a valid choice')
            self.action_menu()
            return

    
    def combat(self):
        '''
        
        '''
        self.action_menu()
        if self.check_enemy_dead():
            return 1
        
        self.bonus_action_menu()
        if self.check_enemy_dead():
            return 1
        
        self.enemy_attack()
        if self.check_player_dead():
            return False
        
        if self.enemy.end_conditions:
            for condition in self.enemy.end_conditions.keys():
                self.end_of_turn(condition)
        
        if self.check_enemy_dead():
            return 1

        return 2


    def menu(self):
        '''
        
        '''

        while True:
            self.show_combat_info()
            choice = int(input('What will you do?\n1: Attack\n2: Defend\n3: Item\n'))

            if choice == 1:
                combat_outcome = self.combat()

                if combat_outcome == 1:
                    print(f'You defeated enemy {self.enemy.name}! ')
                    self.player.weapon.recharge()
                    if isinstance(self.player, Necromancer):
                        self.player.souls += 1
                        input('You gained a soul to use. ')
                    return True
                elif combat_outcome == 2:
                    continue
                else:
                    print('You died! ')
                    return False

            elif choice == 2:
                self.guard()
            elif choice == 3:
                self.item_menu()


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
        
        return self.menu()