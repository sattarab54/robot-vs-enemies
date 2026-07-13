
import random

print("=== PYQUEST ===")
print("enemy Robot Detected!")
print("1. Start Game")
print("2. Quit")
print()

menu_choice = input("Choose option: ").strip()

if menu_choice == "2":
    print("Game closed.")
    quit()
print()

print("=== HOW TO PLAY ===")
print("You control your own robot.")
print("Defeat all enemy robots to win.")
print("Commands:")
print("- attack  = normal laser attack")
print("- heal    = use a repair kit")
print("- special = special attack (Speed Bot can use it twice)")
print("- shield  = block the next enemy attack")
print()

input("Press Enter to start the mission...")
print()

print("Choose Your Robot Class")
print("1. Tank Bot  - High health, stronger special attack")
print("2. Speed Bot - Balanced health, two special attacks")
print("3. Power Bot - Lower health, highest attack bonus")

robot_class = input("Select robot: ").strip()

robot_name = input("Name your robot: ").strip().title()

if robot_class == "1":

    player = {
        "health": 280,
        "repair_kits": 6,
        "xp": 0,
        "level": 1,
        "coins": 0,
        "special_used": False,
        "attack_bonus": 0,
        "shield_uses": 3,
    }

    class_name = "Tank Bot"

elif robot_class == "2":

    player = {
        "health": 220,
        "repair_kits": 5,
        "xp": 0,
        "level": 1,
        "coins": 0,
        "special_used": False,
        "attack_bonus": 5,
        "shield_uses": 2
    }

    class_name = "Speed Bot"

elif robot_class == "3":

    player = {
        "health": 180,
        "repair_kits": 4,
        "xp": 0,
        "level": 1,
        "coins": 0,
        "special_used": 0,
        "attack_bonus": 10,
        "shield_uses": 2
    }

    class_name = "Power Bot"

else:

    print("Invalid choice")    
    quit()

print("Robot Class:", class_name)
print()

shield_active = False
shield_turns = 0
boss_charging = False

enemies = [
    {"name": "Scout Bot", "health": 80,
     "mini_damage": 10,
     "max_damage": 20,
     "mini_coins": 15,
     "max_coins": 25},

    {"name": "Guard Bot", "health": 130,
     "mini_damage": 15,
     "max_damage": 28,
     "mini_coins": 25,
     "max_coins": 40},
        
    {
        "name": "Boss Bot", "health": 200,
        "mini_damage": 20,
        "max_damage": 35,
        "mini_coins": 40,
        "max_coins": 60
    },

    {
        "name": "Mega Boss", "health": 350,
        "mini_damage": 10,
        "max_damage": 20,
        "mini_coins": 80,
        "max_coins": 120,
    }
]
for enemy in enemies:
 
    print()
    print("New Enemy:", enemy["name"])

    while enemy["health"] > 0 and player["health"] > 0:

        print()        
        print(robot_name, "Energy:", player["health"])
        print("Enemy:", enemy["name"])
        print("Enemy Robot Energy:", enemy["health"])
        print("Repair Kits:", player["repair_kits"])
        print("Shields:", player["shield_uses"])
        print("XP:", player["xp"])
        print("Level:", player["level"])

        action = input("Choose action (attack/heal/special/shield): ").strip()
    
        if action == "attack":
            damage = random.randint(10, 30) + player["attack_bonus"]

            if player["level"] == 2:
                damage = damage + 15

            if class_name == "Power Bot":
                critical = random.randint(1, 3)
            else:
                critical = random.randint(1, 5)
                        
            if critical == 1:
                damage = damage * 2
                print("CRITICAL HIT!")

            if player["level"] == 3:
                power_chance = random.randint(1, 4)

                if power_chance == 1:
                    damage = damage + 20
                    print("LEVEL 3 POWER STRIKE!")

            if enemy["name"] == "Guard Bot":
                armor = random.randint(1, 4)

                if armor == 1:
                    print("GUARD BOT ARMOR ABSORBED DAMAGE!")
                    damage = damage // 2

            enemy["health"] = enemy["health"] - damage

            if enemy["health"] <= 0:
                    enemy["health"] = 0

            print("Laser attack did", damage, "demage!")

            player["xp"] = player["xp"] + 10

        elif action == "special":

            can_use_special = False
            
            if class_name == "Speed Bot":
                if player["special_used"] < 2:
                    can_use_special = True
                    player["special_used"] = player["special_used"] + 1                                    
            else:
                if player["special_used"] == False:
                    can_use_special = True
                    player["special_used"] = True

            if can_use_special:
                if class_name == "Tank Bot":
                    damage = random.randint(45, 65)
                else:
                    damage = random.randint(30, 50)

                enemy["health"] = enemy["health"] - damage
                                                                                                                                                    
                if enemy["health"] <= 0:
                    enemy["health"] = 0

                print("SPECIAL ROBOT BLAST did", damage, "damage")
            else:
                print("Special power already used!")                
                                                                                       
        elif action == "heal":
            if player["repair_kits"] > 0:

                heal_amount = random.randint(40,70)

                player["health"] = player["health"] + heal_amount

                player["repair_kits"] = player["repair_kits"] - 1
                print("Repair system restored", heal_amount, "robot energy!")

            else:

                print("No repair kits left")
                continue

        elif action == "shield":
            if player["shield_uses"] <= 0:
                print("No shields left!")
                continue

            shield_active = True
            if class_name == "Tank Bot":
                shield_turns = 2
            else:
                shield_turns = 1

            player["shield_uses"] = player["shield_uses"] - 1
            print("Shield activated!")
            print("Shields left:", player["shield_uses"])

        else:

            print("Invalid command")
            continue
        
        if player["xp"] >= 30 and player["level"] == 1:

            player["level"] = 2
            print("LEVEL UP!")
            print("Your attacks are now stronger.")

        if player["xp"] >= 80 and player["level"] == 2:
            player["level"] = 3
            player["attack_bonus"] = player["attack_bonus"] + 5

            print("LEVEL UP!")
            print("Attack power increased again.")

        if enemy["health"] > 0:
            if enemy["name"] == "Mega Boss" and enemy["health"] <= 200 and "rsge_used" not in enemy:
                print("MEGA BOSS RAGE MODE ACTIVATED")
                enemy["max_damage"] = enemy["max_damage"] + 15
                enemy["rage_used"] = True

            if enemy["name"] == "Mega Boss" and enemy["health"] <= 150 and "repair_used" not in enemy:
                enemy["health"] = enemy["health"] + 50
                enemy["repair_used"] = True
                print("MEGA BOSS REPAIR MODE ACTIVATED!")
                print("Mega Boss restored 50 energy")

            if enemy["name"] == "Boss Bot" and enemy["health"] <= 100:

                if "rage_used" not in enemy:
                    print("WARNING: Boss Rage Mode Activated!")
                    enemy["max_damage"] = enemy["max_damage"] + 10
                    enemy["rage_mode"] = True
                                                            
            enemy_damage = random.randint(enemy["mini_damage"], enemy["max_damage"])

            if enemy["name"] == "Scout Bot":
                quick_shot = random.randint(1, 4)

                if quick_shot == 1:
                    extra_damage = random.randint(
                        enemy["mini_damage"],
                        enemy["max_damage"]
                    )
                    enemy_damage = enemy_damage + extra_damage
                    print("SCOUT BOT QUICK SHOT!")

            if enemy["name"] == "Mega Boss":
                critical_chance = random.randint(1, 5)

                if critical_chance == 1:
                    enemy_damage = enemy_damage + 20
                    print("MEGA BOSS CRITICAL STRIKE!")

            if enemy["name"] == "Boss Bot" and enemy["health"] <= 100 and not boss_charging:
                print("WARNING: Boss is charging a Mega Attack!")
                boss_charging = True

            if enemy["name"] == "Boss Bot" and "rage_used" in enemy:
                mega_chance = random.randint(1, 4)

                if mega_chance == 1:
                    enemy_damage = enemy_damage +15
                    print("BOSS MEGA ATTACK!")

            if player["level"] == 2:
                enemy_damage = enemy_damage + 5

            if shield_active:
                enemy_damage = enemy_damage // 2
                shield_turns = shield_turns - 1

                print("Shield reduced damage!")
                print("Shield blocks left:", shield_turns)

                if shield_turns <= 0:                    
                    shield_active = False
            boss_charging = False

            if class_name =="Speed Bot":
                dodge = random.randint(1, 5)

                if dodge ==1:
                    print("SPEED BOT DODGED THE ATTACK")
                    enemy_damage = 0

            player["health"] = player["health"] - enemy_damage
            if player["health"] < 0:
                player["health"] = 0

            print("Enemy attacked back for", enemy_damage, "damage!")

        if enemy["health"] <=0:
            print()
            print(enemy["name"], "destroyed")
            coins_earned = random.randint(
                enemy["mini_coins"],
                enemy["max_coins"]
            )
            player["coins"] = player["coins"] + coins_earned

            print("Coins earned:", coins_earned)
            print("Total Coins:", player["coins"])

            print()
            print("=== ROBOT SHOP ===")
            print("Upgrade Laser = 40 coins")
            print("Buy Shield = 25 coins")
            print("Buy Repair Kit = 30 coins")

            shop_choice = input("Choose; laser / shield / repair / no: ").strip().lower()


            if shop_choice == "laser":

                if player["coins"] >= 40:

                    player["coins"] = player["coins"] - 40

                    player["attack_bonus"] = player["attack_bonus"] + 5

                    print("Laser upgraded!")
                    print("Attack Bonus:", player["attack_bonus"])
                    print("Coins left:", player["coins"])
       
                else:
                    print("Not enough coins.")

            elif shop_choice == "shield":

                if player["coins"] >= 25:

                    player["coins"] = player["coins"] - 25
                    player["shield_uses"] = player["shield_uses"] + 1

                    print("Shield purchased!")
                    print("Shields:", player["shield_uses"])
                    print("Coins left:", player["coins"])

                else:
                    print("Not enough coins.")

            elif shop_choice == "repair":

                if player["coins"] >= 30:

                    player["coins"] = player["coins"] - 30
                    player["repair_kits"] = player["repair_kits"] + 1

                    print("Repair kit purchased!")
                    print("Repair Kits:", player["repair_kits"])
                    print("Coins left:", player["coins"])
                
            else:
                print("Shop closed.")

else:
    print()
    if player["health"] <= 0:
        print(robot_name, "WAS DESTROYED")
        print("GAME OVER")

    else:
        print()
        print("ALL ENEMIES DESTROYED!")
        print("MISSION COMPLETE")
        print("Final XP:", player["xp"])
        print("Final Level:", player["level"])
                           
        if player["health"] >= 50:
            print("Rating: Excellent")
        
        elif player["health"] >= 20:
            print("Rating: Good")
        else:
            print("Rating: Barely survived")
    
print()
play_again = input("Play again? (yes/no): ").strip().lower()

if play_again == "yes":
    print("Close this run and start again with:")
    print("python pyquest.py")    
else:
    print("Thanks for playing PyQuest!")

        
 





















