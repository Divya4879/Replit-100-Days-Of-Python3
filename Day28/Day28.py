# Day 28 Challenge

import random, os, time
from colorama import Fore
print("⚔️ BATTLE OF LEGENDS 🙍🏻‍♂️🧙🏻‍♀️🧝🏻‍♀️👺 ⚔️")

time.sleep(2)
print()

def legend_name():
  print("Name your legend:")
  name = input("")
  time.sleep(1)
  print()
  return name
  
def random_roll(side):
  dice_roll = random.randint(1,side)
  return dice_roll

def health_legend():
  product = random_roll(6) * random_roll(12)
  health_stats = (product//2) + 10
  return health_stats

def strength_legend():
  product = random_roll(6) * random_roll(12)
  strength_stats = (product//2) + 12
  return strength_stats



def legend_type():
  print("Character Type (Human, Elf, Wizard, Orc):")
  legend_type = input("").capitalize()
  if legend_type == "Human":
    emoji = "🙍🏻‍♂️"

  elif legend_type == "Elf":
    emoji = "🧙🏻‍♀️"

  elif legend_type == "Wizard":
    emoji = "🧝🏻‍♀️"

  elif legend_type == "Orc":
    emoji = "👺"
  time.sleep(1)
  print()
  return emoji


def legend_stats():
  name = legend_name()
  emoji = legend_type()
  
  print(f"{Fore.GREEN}{name}{Fore.WHITE}{emoji}")
  health = health_legend()
  strength = strength_legend()
  print(f"HEALTH STATUS: {Fore.GREEN}{health}{Fore.WHITE} lp")
  print(f"STRENGTH STATUS: {Fore.GREEN}{strength}{Fore.WHITE} lp")
  
  print()
  return name, type, health, strength, emoji


name1, type1, health1, strength1,emoji1 = legend_stats()

print("Who are they battling?")
print()
name2, type2, health2, strength2,emoji2 = legend_stats()
time.sleep(2)
os.system("clear")
time.sleep(1)

round = 0

while True:
  
  print("⚔️ BATTLE TIME ⚔️")
  print()
  if round == 1:
    print("The battle begins!")

  elif round > 1:
    print("The battle continues!")
  
  print()
  time.sleep(2)
  
  legend1_roll = random_roll(6)
  legend2_roll = random_roll(6)
  strength_diff = (abs(strength1 - strength2)) + 1
  if legend1_roll > legend2_roll:
    round_winner = name1
    round_loser = name2
    round += 1

  elif legend2_roll > legend1_roll:
    round_winner = name2
    round_loser = name1
    round += 1
    
  if round_winner == name1:
    health1 += strength_diff  
    health2 -= strength_diff 
  else:
    health2 += strength_diff  
    health1 -= strength_diff 
    
  print(f"{round_winner}  wins the round {round}")
  print(f"{round_loser} takes a hit, with {strength_diff} damage")
  time.sleep(3)
  print()
  
  
  print()
  print(name1)
  print(health1)
  
  print()
  print(name2)
  print(health2)

  if health1 <= 0 :
    print(f"Oh no!! {name1} has died🥺🥺!")
    os.system("clear")
    print(f"Congratulations {name2}{emoji2}🤩🥳")
    print(f"{name1}{emoji1} dear, Better Luck Next Time!")
    exit()

  elif health2 <= 0 :
    print(f"Oh no!! {name2} has died🥺🥺!")
    os.system("clear")
    print(f"Congratulations {name1}{emoji1}🤩🥳")
    print(f"{name2}{emoji2} dear, Better Luck Next Time!")
    exit()
    
  
  print("And they're both standing for the next round!")
  time.sleep(6)
  os.system("clear")
