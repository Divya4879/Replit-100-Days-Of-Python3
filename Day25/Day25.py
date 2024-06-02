"""
# Day 25 Code

#subroutine has parameter called `number`
#`number` shows how many numbers we want the pin to have
def pinPicker(number):
  import random
  pin = "" #this is the empty string
  for i in range(number): #for loop shows defined amount of random numbers
    pin += str(random.randint(0,9)) #we want a string of random numbers between 0-9
  return pin

print(pinPicker(4)) #4 means we want 4 random numbers

"""

"""
# Fix the Code

def area_square(side1,side2):
  area = side1 * side2
  return area

area = area_square(4, 12)
print(area)

"""

# Day 25 Challenge
import random

print("⚔️ Character Stats Generator ⚔️")
print()

print("Get to know the health stats of your fav character. If you want to exit the game, press no when prompted")
print()

def roll_dice(): 
  sides =  int(input("Enter the no of sides you wanna have on your special dice: "))
  roll_result = random.randint(1,sides)
  return roll_result


def health_stats():
  dice1 = random.randint(1,6)
  dice2 = random.randint(1,8)
  product = dice1 * dice2
  return product

while True:
  username = input("Name your warrior: ")
  product = health_stats()
  print(f"Your \033[1;34;20m{username} \033[0;34;0m's health is currently \033[0;35;20m{product}\033[0;35;0m hp🥳.")

  user_prompt = input("Want to have another character? ")
  if user_prompt == "no":
    exit()

