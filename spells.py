from attack import Attack
from dice import dice
from math import ceil

class Firebolt(Attack):

    def __init__(self):
        self.name = "Firebolt"
        self.damage_type = "fire"
        self.max_uses = None
        self.uses = None
        self.damages = True
        
    
    def use(self, player, enemy):
        damage = dice(10, player.level + 1)
        input(f'You attacked enemy {enemy} for {damage} damage! They\'ve been ignited!')
        enemy.damage(damage)

        if 'ignite' in enemy.end_conditions.keys():
            enemy.end_conditions['ignite'][1] += 1
        else:
            enemy.end_conditions['ignite'] = [4, player.level]


class FrostRay(Attack):

    def __init__(self):
        self.name = "Ray of Frost"
        self.damage_type = "ice"
        self.max_uses = None
        self.uses = None
        self.damages = True

    
    def use(self, player, enemy):
        damage = dice(8, player.level)
        input(f'You attacked enemy {enemy} for {damage} damage! They\'ve become brittle! ')
        enemy.damage(damage)

        if 'brittle' in enemy.conditions.keys():
            enemy.conditions['brittle'][1] += 1
        else:
            enemy.conditions['brittle'] = [4, player.level]


class EldritchBlast(Attack):

    def __init__(self):
        self.name = "Eldritch blast"
        self.damage_type = "force"
        self.max_uses = None
        self.uses = None
        self.damages = True

    
    def use(self, player, enemy):
        damage = dice(10, player.level) + (5 * player.level)
        input(f'You attacked enemy {enemy} for {damage} damage! ')
        enemy.damage(damage)


class SoulSiphon(Attack):

    def __init__(self):
        self.name = "Soul siphon"
        self.damage_type = None
        self.max_uses = None
        self.uses = None
        self.damages = False

    
    def use(self, player, enemy):
        if player.souls > 0:
                damage = dice(8, player.level) + player.level
                health = int(ceil(damage) / 2)
                player.souls -= 1
                if player.health != player.health_max:
                    input(f'You consumed a soul to damage enemy {enemy} for {damage} damage! \
                        \n You were healed for {health} health!\nYou have {player.souls} souls left. ')
                    player.heal(health)
                else:
                    if player.temp_hp is not None:
                        player.temp_hp += health
                    else: 
                        player.temp_hp = health
                    input(f'You consumed a soul to damage enemy {enemy} for {damage} damage! \
                        \n You gained {health} temp hp!\nYou have {player.souls} souls left. ')
                enemy.damage(damage)           
        else:
            input('You have no souls to use. ')
    



class RayOfSickness(Attack):
    def __init__(self):
        self.name = "Ray of sickness"
        self.damage_type = "poison"
        self.max_uses = 2
        self.uses = 2
        self.damages = True

    
    def use(self, player, enemy):
        self.uses -= 1
        damage = dice(6, 2 + player.level)
        input(f'You attacked enemy {enemy} for {damage} damage! There\'ve been poisoned! ')
        enemy.damage(damage)
        
        if 'poison' in enemy.end_conditions.keys():
            enemy.end_conditions['poison'][1] += player.level
        else:
            enemy.end_conditions['poison'] = [6, player.level]


class FrostArmor(Attack):

    def __init__(self):
        self.name = "Armor of ice"
        self.damage_type = "ice"
        self.max_uses = 2
        self.uses = 2
        self.damages = False
    
    def use(self, player, enemy):
        self.uses -= 1
        player.armor_of_ice = True
        player.temp_hp = 10 * player.level
        input(f'You got {10 * player.level} temp hp as an armor of ice encases your body!\nIf an enemy hits you, they\'ll take damage! ')


class LightningBolt(Attack):
    def __init__(self):
        self.name = "Lightning bolt"
        self.damage_type = "lightning"
        self.max_uses = 2
        self.uses = 2
        self.damages = True

    
    def use(self, player, enemy):
        self.uses -= 1
        damage = dice(8, 4 * player.level)
        input(f'You shot a lightningbolt to attack enemy {enemy} for {damage} damage! ')
        enemy.damage(damage)


class SummonSkeleton(Attack):
    def __init__(self):
        self.name = "Summon skeleton"
        self.damage_type = None
        self.max_uses = None
        self.uses = None
        self.damages = True

    
    def use(self, player, enemy):
            if player.souls > 0:
                skeletons_to_animate = player.souls
                player.souls = 0
                input(f'You summoned {skeletons_to_animate} skeleton(s)! You can command them with a bonus action. ')
                damage = dice(8, (player.level + skeletons_to_animate)) + 5
                input(f'Your new skeleton(s) attacked enemy {enemy} for {damage} damage! ')
                enemy.damage(damage)
                player.minions += skeletons_to_animate
                input(f'You now have {player.minions} skeletons! ')

                add_command = True
                for attack in player.bonus_actions:
                    if attack.name == "Command skeletons":
                        add_command = False
                if add_command:
                    player.bonus_actions.append(SkeletonAttack())
                
            else:
                input('You have no souls to use. ')


class SkeletonAttack(Attack):
    def __init__(self):
        self.name = "Command skeletons"
        self.damage_type = 'physical'
        self.max_uses = None
        self.uses = None
        self.damages = True


    def use(self, player, enemy):
        damage = dice(8, player.level + player.minions) + 5
        input(f'Your skeletons attacked enemy {enemy} for {damage} damage! ')
        enemy.damage(damage)


class Hex(Attack):
    def __init__(self):
        self.name = "Hex"
        self.damage_type = 'necrotic'
        self.max_uses = 3
        self.uses = 3
        self.damages = False

    def use(self, player, enemy):
        self.uses -= 1
        input(f'You hexed enemy {enemy}! They\'ll take extra damage. ')
        
        if 'hex' in enemy.conditions.keys():
            enemy.conditions['hex'][1] += player.level
        else:
            enemy.conditions['hex'] = [6, player.level]
        

class Fireball(Attack):

    def __init__(self):
        self.name = "Fireball"
        self.damage_type = "fire"
        self.max_uses = 3
        self.uses = 3
        self.damages = True

    
    def use(self, player, enemy):
        if self.uses > 0:
            self.uses -= 1
            damage = dice(6, player.level * 3)
            input(f'You fireballed enemy {enemy} for {damage} damage! ')
            enemy.damage(damage)
        else:
            return None
        

class Blight(Attack):

    def __init__(self):
        self.name = "Blight"
        self.damage_type = "necrotic"
        self.max_uses = 2
        self.uses = 2
        self.damages = True

    
    def use(self, player, enemy):
        if self.uses > 0:
            self.uses -= 1
            damage = dice(8, player.level * 4)
            input(f'You cast blight on enemy {enemy} for {damage} damage! ')
            enemy.damage(damage)
        else:
            return None


class AbsorbHealth(Attack):

    def __init__(self):
        self.name = "Absorb health"
        self.damage_type = "necrotic"
        self.max_uses = 2
        self.uses = 2
        self.damages = True

    
    def use(self, player, enemy):
        if self.uses > 0:
            self.uses -= 1
            damage = dice(8, player.level * 4)
            input(f'You drained enemy {enemy} for {damage} damage! ')
            enemy.damage(damage)
            player.heal(damage//2)
            input(f'You were healed for {damage//2}! ')
        else:
            return None


class MagicMissle(Attack):

    def __init__(self):
        self.name = "Magic Missle"
        self.damage_type = "force"
        self.max_uses = 3
        self.uses = 3
        self.damages = True

    
    def use(self, player, enemy):
        if self.uses > 0:
            self.uses -= 1
            damage = dice(4, player.level + 5)
            input(f'You launched magic missles at enemy {enemy} for {damage} damage! ')
            enemy.damage(damage)
        else:
            return None


class Disintegrate(Attack):
    def __init__(self):
        self.name = "Disintegrate"
        self.damage_type = "force"
        self.max_uses = 1
        self.uses = 1
        self.damages = True

    
    def use(self, player, enemy):
        if self.uses > 0:
            self.uses -= 1
            damage = dice(10, 10) + 40
            input(f'You disintegrated enemy {enemy} for {damage} damage! ')
            enemy.damage(damage)
        else:
            return None