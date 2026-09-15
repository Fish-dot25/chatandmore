#SETUP (This is where lists, functions and variables go.)
import random

player_attack = 20  # Player's attack power
enemy_names = ["Evil Jeremy", "Evil Bob", "Evil Joe" ] # Enemy's name
enemy_hps = [45,70,90]  # Enemy's HP
player_hp = int(input("Player Max HP >> "))
if player_hp > 120:
    int(input("Under 120!!! \n Player Max HP >> "))
enemy_attacks = [5,10,15]
player_name= input("Name your player")
turns = 3
heal = 10

event_log = []


def show_results():
    if player_hp > 0:
        print("You beat them all!")
    else:
        print("OH NO! You died.")
        

def calc_damage(attack):
    d = attack + random.randint(-2,2 )  
    if d < 1:
        d = 1
    return d
    
def is_valid_choice(text):
    if text == "1":
        return True
    elif text == "2":
        return True
    elif text == "3":
        return True
    else:
        return False

def make_text(e_name, e_hp, p_hp, p_name):
    text = ""
    text = text + "Turn Battle\n"
    text = text + e_name + "  HP:" + str(e_hp) + "\n"
    text = text + "  vs\n"
    text = text + p_name +"  HP:" + str(p_hp) + "\n"
    return text

def do_player_attack(enemy_hp, is_critical):
    dmg = calc_damage(player_attack)
    if is_critical == True:
        dmg = dmg*2
        enemy_hp = enemy_hp - dmg
        return enemy_hp

def do_player_heal(p_hp):
    p_hp = heal + p_hp
    return p_hp
    
def check_battle(enemy_hp, player_hp):
    if player_hp < 0 :
        return "Lose"
    elif enemy_hp < 0 :
        return "Win"
    else:
        return "continue"
        
order = [0,1,2]
random.shuffle(order)
    
#MAIN BATTLE CODE

for count in range(len(enemy_names)):
    enemy_index = order[count]
    enemy_hp = enemy_hps[enemy_index]
    current_enemy_name = enemy_names[enemy_index]
    print(current_enemy_name + " appeared!")

    while check_battle(enemy_hp, player_hp) == "continue":
        print(make_text(current_enemy_name, enemy_hp, player_hp, player_name))
        ans = input("1) Attack \n 2) Defend \n 3) Heal > \n Type in the number ")
        critical = random.randint(0, 3)
        
        if is_valid_choice(ans) == False:
            ans = input("I said CHOOSE ONE" + "\n 1)Attack 2)Defend. Type in the number.(i.e., 1)")
        else:
            match ans:
                case "1":
                    if critical != 0:
                        dmg = calc_damage(player_attack) * 2
                        print("Critical hit! " + str(dmg) + " damage!")
                        enemy_hp = enemy_hp - dmg
                        player_hp = player_hp - enemy_attacks[enemy_index]
                        print(current_enemy_name + " attacks! " + str(enemy_attacks[enemy_index]) + " damage!")
                        event_log.append("Critical " + str(dmg) + " damage")
                    else:
                        dmg = calc_damage(player_attack)
                        enemy_hp = enemy_hp - dmg # Reduce HP by the attack power
                        print( str(player_name) + " attacks! " + str(player_attack) + " damage!")  # Use str() to turn a number into a string
                        print(current_enemy_name + "'s HP: " + str(enemy_hp))
                        print("Enemy_attacks! " + str(enemy_attacks[enemy_index]) + " damage!")
                        player_hp= player_hp - enemy_attacks[enemy_index]
                        print(str(player_name) + "'s HP: " + str(player_hp))
                        event_log.append( "Enemy took" + str(dmg) + " damage" )
                        
                case "2":
                    print(str(player_name) + " Defends " + str(enemy_attacks[enemy_index]) + " damage!")
                    print(str(player_name) + "'s HP: " + str(player_hp))
                    event_log.append( str(player_name) + " defended")
                   
                case "3":
                    if player_hp < 120:
                        print(str(player_name) + " heals!")
                        player_hp = player_hp + heal
                        print(str(player_name) + "'s HP:" +str(player_hp) )
                        event_log.append( str(player_name) + " healed" + str(heal) + "HP.")
                    else:
                       ans = input("Sorry, you are at max HP! Choose again:\n 1) Attack \n 2) Defend \n Type in the number>> ") 
            
        
    result = check_battle(enemy_hp, player_hp)
    
    if result == "Win":
        print("Results of this battle: ")
        print("")
        print("Enemy HP"+str(enemy_hp))
        print( player_name+"'s HP"+str(player_hp))
        print(current_enemy_name+ " was defeated")
    if result == "Lose":
        print("Results of this battle: ")
        print("")
        print("Enemy HP"+str(enemy_hp))
        print( str(player_name)+" HP"+str(player_hp))
        print(player_name+ "has fallen")


show_results()

print(event_log)


