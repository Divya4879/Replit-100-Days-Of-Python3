# Day 27 Challenge

import random, os, time
from colorama import Fore
print("⚔️ CHARACTER BUILDER ⚔️")
time.sleep(2)
print()


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

def legend_stats():
  print("Name your legend:")
  legend_name = input("")
  time.sleep(1)
  print()

  print("Character Type (Human, Elf, Wizard, Orc):")
  legend_type = input("")
  time.sleep(1)
  print()
  print(f"{Fore.GREEN}{legend_name}{Fore.WHITE}")
  health = health_legend()
  strength = strength_legend()
  print(f"HEALTH STATUS: {Fore.GREEN}{health}{Fore.WHITE} lp")
  print(f"STRENGTH STATUS: {Fore.GREEN}{strength}{Fore.WHITE} lp")
  print("May your name go down in the history of legends!")
  print()

while True:
  
  legend_stats()
  user_prompt = input("Another legend? ")
  if user_prompt == "no":
    time.sleep(1)
    os.system("clear")
    exit()
    
  else:
    os.system("clear")
    continue
