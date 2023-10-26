from src.player import player

class mob(player):

    def __init__(self, name, hp, dmg, inventory):
        super().__init__(name, hp, dmg, inventory)