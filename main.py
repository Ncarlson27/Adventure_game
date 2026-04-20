'''
Author: Nathan Carlson
CS 1410-001 Final project

This program creates an adventure game with you as the adventurer. You choose your class and name and then set out to defeat
the final boss. 

To run: Simply run through the terminal and use the enter button to advance the text.
'''

from player import *
from items import *
from room import *

def game():
    '''
    This runs the main game taking input from the user
    '''
    input("Welcome to to your new adventure. In this game you will take the role of an adventurer decending into a dungeon\nYou will have to clear 10 rooms to make it to the final boss. The room could be a puzzle, a gift, or combat\nYou will level up periodically, get stronger, find better potions, and fight harder enemies\nWell, time for you to get started (press enter to continue) ")
    input("Welcome adventurer, you've been choosen to save our town from the evil goblin king Elric. ")
    input("Before you start I have a couple of questions for you. Are you ready? ")
    while True:
        print("Fighters have lots of health and consistant damage\nMages have low health but do lots of damage\nRogues have moderate health, do volitale damage, and start with a key")
        subtype = input("Are you a mage, fighter, or rogue?: ")
        if subtype in ('mage', 'fighter', 'rogue'):
            break
        else:
            print('Please choose one of the classes above')
    name = input("What's your name?: ")
    try:
        if subtype == 'mage':
            player = Mage(name)
        elif subtype == 'fighter':
            player = Fighter(name)
        elif subtype == 'rogue':
            player = Rogue(name)
    except:
        pass
    
    input("With those questions out of the way you're ready to begin your adventure! Good luck. ")
    input("You arrive at the entrance to the cave ")
    input("Before you enter you see a health potion by the door and grab it. You never know what'll happen ")
    player.add_potion(Potion('potion (2d8 + 2)'))
    counter = 0
    input("You steel yourself and enter the dungeon! ")
    while True:
        if counter in (4, 7, 10):
            player.level_up()
            input(f"Congratulations! {player.name} leveled up! You're now level {player.level} and you health is now {player.health}")
        if counter < 10:
            input("You see a door and enter the room. ")
            event_type = random.randint(1, 4)
            if event_type in (1, 2):
                room = Room('combat', counter)
            elif event_type in (3, 4):
                room = Room('gift', counter)
            '''elif event_type == 3:
                room = Room('door', counter)'''
            event = room.create_event()
            outcome = event.run_event(player)
            if outcome == 'player dead':
                print('Better luck next time')
                break
            counter += 1
        elif counter == 10:
            input("As you approach the next room you see the skelton of an adventurer before you ")
            input("You loot the skeleton and find an ultimate potion ")
            player.add_potion(Potion('ultimate potion (8d8 + 8)'))
            input("Before you stands a menacing door, this is the final fight. Are you ready? ")
            room = Room('combat', counter)
            event = room.create_event()
            outcome = event.run_event(player)
            if outcome == 'player dead':
                print('Better luck next time')
                break
            else:
                print('You defeated the evil king Elric!')
                break


def main():
    '''
    Calls the game function
    '''
    game()

if __name__ == '__main__':
    main()
