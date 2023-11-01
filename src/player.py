import random

class player:
    def __init__(self, name, hp, dmg, inventory):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.inventory = inventory

    def attack(self, player, mob):
        randomNum = random.randrange(0, 100)
        
        if (randomNum > 50):
            mob.hp = mob.hp - player.dmg
            if (mob.hp < 0):
                mob.hp = 0
            print("\n{} attacks {} for {} damage.\n{}'s hp: {}\n".format(player.name, mob.name, player.dmg, mob.name, mob.hp))
        else:
            player.hp = player.hp - mob.dmg
            print("\n{} has missed the attack! {} attacks {} for {} damage.\n{}'s hp: {}\n".format(player.name, mob.name, player.name, mob.dmg, player.name, player.hp))
        
    def checkBuffs(self, player):
        for i in player.inventory:
            if (i == "Master Sword"):
                player.dmg = 20
                       
    def checkStats(self, player):
        player.checkBuffs(player)
        print("""\n{}'s stats:
HP: {}
DPS: {}
""".format(player.name, player.hp, player.dmg))
        
    def checkInv(self, player):
        print("\nItems: ")
        for i in player.inventory:
            print("-" + str(i))
        print(" ")
    