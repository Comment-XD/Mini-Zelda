from src.mob import mob
from src.player import player

class main:
    print("Welcome to Mini Zelda!")
    characterName = input("What is the name of your character? ")
    character = player(characterName, 100, 5, ["Master Sword"])
    enemy = mob("Ganon", 150, 10, ["Diamond"])
    print(" ")
    while (character.hp > 0 and enemy.hp > 0):
        user_input = input("""[Menu]
1. Attack
2. Player Stats
3. Mob Stats
4. Inventory
5. Quit
Choice: """)
        match user_input:
            case "1":
                character.checkBuffs(character)
                character.attack(character, enemy)
                if (character.hp <= 0):
                    print("{} has died...".format(character.name))
                elif (enemy.hp <= 0):
                    character.inventory.append(enemy.inventory)
                    print("{} has died! GG!".format(enemy.name))
                    character.checkInv(character)
            case "2":
                character.checkStats(character)
            case "3":
                enemy.checkStats(enemy)
            case "4":
                character.checkInv(character)
            case "5":
                character.hp = 0
