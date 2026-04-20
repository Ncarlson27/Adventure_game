from abc import ABC, abstractmethod


class Attack(ABC):

    def __init__(self):
        self.name = None
        self.damage_type = None
        self.max_uses = None
        self.uses = None
        self.damages = True

    @abstractmethod
    def use(self, player, enemy):
        ...
    
    def does_damage(self):
        return self.damages

    def __str__(self):
        return self.name
