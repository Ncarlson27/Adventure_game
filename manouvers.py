from attack import Attack
from dice import dice

class BasicAttack(Attack):

    def __init__(self):
        self.name = "Basic attack"
        self.damage_type = "physical"
        self.max_uses = None
        self.uses = None
    
    def use(self, player, enemy):
        for _ in range(player.level):
            damage = dice(10, player.level) + 5
            input(f'You attacked enemy {enemy} for {damage} damage! ')
            enemy.damage(damage)
