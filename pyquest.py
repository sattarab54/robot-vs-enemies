
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
print("- special = powerful blast, only once")
print()

input("Press Enter to start the mission...")
print()

print("Choose Your Robot Class")
print("1. Tank Bot")
print("2. Speed Bot")
print("3. Power Bot")

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
        "attack_bonus": 0,
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
        "special_used": False,
        "attack_bonus": 0,
        "shield_uses": 2
    }

    class_name = "Power Bot"

else:

    print("Invalid choice")    
    quit()

print("Robot Class:", class_name)
print()

shield_active = False
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
     "max_coins": 40,},
        
    {"name": "Boss Bot", "health": 200,
     "mini_damage": 20,
     "max_damage": 35,
     "mini_coins": 40,
     "max_coins": 60} 
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

            critical = random.randint(1, 5)

            if critical == 1:
                damage = damage * 2
                print("CRITICAL HIT!")

            if player["level"] == 3:
                power_chance = random.randint(1, 4)

                if power_chance == 1:
                    damage = damage + 20
                    print("LEVEL 3 POWER STRIKE!")

            enemy["health"] = enemy["health"] - damage
            if enemy["health"] <= 0:
                    enemy["health"] = 0

            print("Laser attack did", damage, "demage!")

            player["xp"] = player["xp"] + 10

        elif action == "special":
            if player["special_used"] == False:

                damage = random.randint(30, 50)
                enemy["health"] = enemy["health"] - damage

                if enemy["health"] <= 0:
                    enemy["health"] = 0

                print("SPECIAL ROBOT BLAST did", damage, "damage")
                
                player["special_used"] =True
                
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
            if enemy["name"] == "Boss Bot" and enemy["health"] <= 100:

                if "rage_used" not in enemy:
                    print("WARNING: Boss Rage Mode Activated!")
                    enemy["max_damage"] = enemy["max_damage"] + 10
                    enemy["rage_mode"] = True
                                                            
            enemy_damage = random.randint(enemy["mini_damage"], enemy["max_damage"])

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
                print("Shield reduced damage!")
                shield_active = False
            boss_charging = False

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
    print("ALL ENEMIES DESTROYED!")
    print("MISSION COMPLETE")
    print("Final XP:", player["xp"])
    print("Final Level:", player["level"])
           
    if player["health"] <= 0:
        print()
        print(robot_name, "WAS DESTROYED")
    
    if player["health"] >= 50:
        print("Rating: Excellent")
        
    elif player["health"] >= 20:
        print("Rating: Good")
    else:
        print("Rating: Barely survived")
    
print()
play_again = input("Play again? (yes/no): ").strip().lower()

if play_again == "yes":
    print("Restart the program to play again.")
else:
    print("Thanks for playing PyQuest!")

        
 





















