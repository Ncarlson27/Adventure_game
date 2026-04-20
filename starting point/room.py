'''
Contains information about the various rooms possible in the game.
'''

from items import *
from characters import Enemy, FinalBoss
import random

class Room:
    '''
    Creates a room with a chosen event and the room number in the dungeon

    Use create_event() to create an instance of the chosen event 
    '''
    def __init__(self, event, number):
        self.event = event
        self.number = number

    def create_event(self):
        '''
        Creates an instance of the room's chosen event
        '''
        if self.event == 'combat':
            return Combat(self.number)
        elif self.event == 'gift':
            return Gift(self.number)
        elif self.event == 'door':
            return Door(self.number)


class Door:
    '''
    Manages the puzzle event rooms with varying difficulties based on the room number

    Use door() to manage the locked door portion of the event in the case of having no key/choosing not to use it

    Use run_event() to start the room's event. Will see if the player has a key or if they want to use it.
    '''
    def __init__(self, number):
        self.number = number

    def door(self):
        '''
        If the player has no keys or chooses not to use one then this manages the riddle part
        Becomes more difficult as the room number increases
        '''
        if self.number in (0, 1, 2, 3):
            input("It looks like you'll need to solve a riddle to open it")
            first_num = random.randint(1, 100)
            second_num = random.randint(1, 100)
            while True:
                answer = input(f"What's {first_num} + {second_num}?: ")
                try:
                    if int(answer) == first_num + second_num:
                        input('You solved the riddle and opened the door!')
                        return True
                except:
                    print('Please enter a number')
        elif self.number in (4, 5, 6):
            input("It looks like you'll need to solve a riddle to open it")
            first_num = random.randint(1, 100)
            second_num = random.randint(1, 100)
            third_num = random.randint(1, 100)
            while True:
                answer = input(f"What's {first_num} + {second_num} + {third_num}?: ")
                try:
                    if int(answer) == first_num + second_num + third_num:
                        input('You solved the riddle and opened the door!')
                        return True
                except:
                    print('Please enter a number')
        elif self.number in (7, 8, 9):
            input("It looks like you'll need to solve a riddle to open it")
            first_num = random.randint(1, 100)
            second_num = random.randint(1, 100)
            third_num = random.randint(1, 100)
            fourth_num = random.randint(1, 100)
            while True:
                answer = input(f"What's {first_num} + {second_num} + {third_num} + {fourth_num}?: ")
                try:
                    if int(answer) == first_num + second_num + third_num + fourth_num:
                        input('You solved the riddle and opened the door!')
                        return True
                except:
                    print('Please enter a number')

    def run_event(self, player):
        '''
        Determines if the player has a key and if so, asks if they want to use it to open the door
        If the player doesn't have a key it calls the door() function 
        '''
        input('You find yourself at a locked door')
        choice = ''
        while True:
            if player.keys > 0:
                while choice not in ['yes', 'no']:
                    choice = input('Would you like to use a key? yes/no: ')
                    if choice not in ['yes', 'no']:
                        print('Please choose yes or no')
                if choice == 'yes':
                    input('You used the key to open the door but it broke in the lock')
                    player.keys -= 1
                    choice = ''
                    break
                else:
                    result = Door.door(self)
                    if result: 
                        break
            else:
                result = Door.door(self)
                if result: 
                    break


class Gift:
    '''
    Simulates the player opening a treasure chest and finding an item inside

    Use run_event() to run the event
    '''
    def __init__(self, number):
        self.number = number

    def run_event(self, player):
        '''
        Randomly determines what the player finds
        Potions get stronger as the room level increases
        '''
        input("You enter the room and find an open treasure chest ")
        input("You decide to look inside ")
        chance = random.randint(1, 100)
        if chance < 2:
            player.keys += 1
            input('You found a key!')
        else:
            if self.number in (0, 1, 2, 3):
                player.add_potion(Potion('potion (2d8 + 2)'))
                input('You got a potion!')
            elif self.number in (4, 5, 6):
                player.add_potion(Potion('greater potion (4d8 + 4)'))
                input('You got a greater potion!')
            elif self.number in (7, 8, 9):
                player.add_potion(Potion('superior potion (6d8 + 6)'))
                input('You got a superior potion!')


class Combat:
    '''
    Creates an enemy for the player to fight and runs combat

    Use run_event to run combat
    '''
    def __init__(self, number):
        self.number = number

    def run_event(self, player):
        '''
        Creates an enemy based on the room number and the runs through combat with the various choices possible

        Player can attack and do damage, but will also take damage
        Player can defend to take no damage from the enemy
        Player can use a potion that the have to heal, will not take damage that turn
        '''
        if self.number in (0, 1, 2, 3):
            enemy = Enemy(16, 1, 'Goblin')
        elif self.number in (4, 5, 6):
            enemy = Enemy(32, 2, 'Hobgoblin')
        elif self.number in (7, 8, 9):
            enemy = Enemy(48, 3, 'Goblin chief')
        elif self.number == 10:
            enemy = FinalBoss(150, 4, 'Elric, King of the Goblins')
        
        if self.number < 10:
            input(f'Enemy {enemy} has appeared! ')
        elif self.number == 10:
            input(f'Final boss {enemy} has appeared! ')
        while True:
            choice = input(f'Your health = {player.health}\nEnemy health = {enemy.health}\nWhat will you do?\n1: Attack\n2: Defend\n3: Item\n')
            if choice == '1':
                damage = player.attack()
                input(f'You attacked enemy {enemy} for {damage} damage! ')
                enemy.damage(damage)
                if enemy.health <= 0:
                    input(f'Enemy {enemy} was defeated! ')
                    break
                else:
                    damage = enemy.attack()
                    input(f'Enemy {enemy} attacked you for {damage} damage! ')
                    player.damage(damage)
                if player.health <= 0:
                    print('You died!')
                    return 'player dead'
            elif choice == '2':
                input(f'{enemy} attacked for {enemy.attack()} damage but you managed to block it ')
            elif choice == '3':
                counter = 1
                if len(player.inventory) == 0:
                    input('You have no potions ')
                else:
                    for item in player.inventory:
                        print(f'{counter}: {item}')
                        counter += 1
                item_choice = input('Which item would you like to use? (0 to exit): ')
                try:
                    item_choice = int(item_choice)
                    if item_choice == 0:
                        pass
                    elif item_choice <= len(player.inventory):
                        item = player.inventory.pop(item_choice - 1)
                        healing = item.effect()
                        player.heal(healing)
                        input(f'You used {item.name} and were healed for {healing}! ')
                    else:
                        print('Please enter a valid choice')
                except ValueError:
                    print('Please enter a valid choice')
                    
