from player import *
from mage import *
from necromancer import *
from items import *
from room import *
from weapons import *
import random


def level_up(player):
    player.level_up()
    input(f"Congratulations! {player} leveled up! You're now level {player.level} and you health is now {player.health}\nYour action uses are now refreshed")


def run_room(player):
    input("You see a door and enter the room. ")
    event_type = random.randint(1, 4)
    if event_type in (1, 2, 3):
        room = Room('combat', counter, player)
    else:
        room = Room('gift', counter, player)
    event = room.create_event()
    outcome = event.run_event()
    if not outcome:
        print('Better luck next time')
        return None
    else:
        return True


def run_boss(player):
    input("As you approach the next room you see the skelton of an adventurer before you ")
    input("You loot the skeleton and find an ultimate potion ")
    player.add_potion(Potion('ultimate potion (8d8 + 8)'))
    input("Before you stands a menacing door, this is the final fight. Are you ready? ")
    room = Room('combat', counter, player)
    event = room.create_event()
    outcome = event.run_event()
    if not outcome:
        print('Better luck next time')
    else:
        print('You defeated the evil king Elric!')


"""
TODO
Change display to be in player and enemy
Update potion creation
Change conditions to classes


"""



if __name__ == "__main__":

    player = Necromancer("Pain")
    staff = FireboltStaff()

    player.equip_weapon(staff)

    
    input("Before you enter you see a health potion by the door and grab it. You never know what'll happen ")
    player.add_potion(Potion('potion (2d8 + 2)'))
    counter = 0
    input("You steel yourself and enter the dungeon! ")
    while True:
        if counter in (4, 7, 10):
            level_up(player)
        if counter < 10:
            outcome = run_room(player)
            if outcome is None:
                break
            counter += 1
        elif counter == 10:
           run_boss(player)
           break